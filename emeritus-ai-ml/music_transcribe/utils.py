# ------------------------------------------------------------------------------
#  © 2025 Monobina Bhowmick-Saha
#  Original Repo: https://github.com/monobinab-source/ai-ml/tree/main/emeritus-ai-ml/music_transcribe
#  Licensed under the MIT License. See the LICENSE file for details.
# ------------------------------------------------------------------------------

import librosa
import numpy as np
from google.cloud import storage, aiplatform
import json
import os

storage_client = storage.Client()
input_bucket_name = "audio_and_midi_files"
output_bucket_name = "predicted_piano_roll"

def summarize_piano_roll(piano_roll):
    note_density = np.sum(piano_roll) / piano_roll.shape[1]
    active_notes = np.count_nonzero(np.sum(piano_roll, axis=1))
    duration = piano_roll.shape[1]

    return f"The piano roll has {active_notes} active notes out of 88 possible keys, over a duration of {duration} time steps, with an average note density of {note_density:.2f} notes per time step."


def run_vertex_ai_prediction(gcs_path, audio_to_midi_endpoint):
    # Download audio from GCS
    local_file = '/tmp/input.mp3'
    bucket = storage_client.bucket(input_bucket_name)
    blob = bucket.blob(gcs_path)
    blob.download_to_filename(local_file)

    # Extract features
    y, sr = librosa.load(local_file, sr=22050)
    mel_spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    log_mel = librosa.power_to_db(mel_spec, ref=np.max)

    input_array = log_mel[:, :100][np.newaxis, ..., np.newaxis].tolist()

    # Prediction
    response = audio_to_midi_endpoint.predict(instances=input_array)

    # Process response
    piano_roll = np.array(response.predictions[0])
    most_common_note = int(np.argmax(np.sum(piano_roll, axis=1)))
    piano_roll_summary = summarize_piano_roll(piano_roll)

    # Prepare output paths
    output_base = os.path.splitext(gcs_path.split('/')[-1])[0]
    folder = gcs_path.split('/')[0]

    # Upload piano_roll npy
    piano_roll_file = f"/tmp/{output_base}_piano_roll.npy"
    np.save(piano_roll_file, piano_roll)

    piano_roll_gcs_path = f"{folder}/{output_base}_piano_roll.npy"
    storage_client.bucket(output_bucket_name).blob(piano_roll_gcs_path).upload_from_filename(piano_roll_file)

    # Upload embedding npy
    embedding_file = f"/tmp/{output_base}_embedding.npy"
    np.save(embedding_file, log_mel)

    embedding_gcs_path = f"{folder}/{output_base}_embedding.npy"
    storage_client.bucket(output_bucket_name).blob(embedding_gcs_path).upload_from_filename(embedding_file)

    return {
        "most_common_note": most_common_note,
        "piano_roll_summary": piano_roll_summary,
        "piano_roll_npy_gcs_path": f"gs://{output_bucket_name}/{piano_roll_gcs_path}",
        "embedding_npy_gcs_path": f"gs://{output_bucket_name}/{embedding_gcs_path}"
    }
