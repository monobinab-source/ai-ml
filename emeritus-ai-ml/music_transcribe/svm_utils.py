# ------------------------------------------------------------------------------
#  © 2025 Monobina Bhowmick-Saha
#  Original Repo: https://github.com/monobinab-source/ai-ml/tree/main/emeritus-ai-ml/music_transcribe
#  Licensed under the MIT License. See the LICENSE file for details.
# ------------------------------------------------------------------------------


import os
import numpy as np
import librosa
from google.cloud import storage

storage_client = storage.Client()
INPUT_BUCKET   = "audio_and_midi_files"

def extract_153_features(mp3_path: str) -> np.ndarray:
    y, sr      = librosa.load(mp3_path, sr=22050)
    duration   = librosa.get_duration(y=y, sr=sr)
    onset_env  = librosa.onset.onset_strength(y=y, sr=sr)
    tempo, _   = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
    onset_rate = len(librosa.onset.onset_detect(y=y, sr=sr)) / duration

    rmse    = librosa.feature.rms(y=y).mean()
    zcr     = librosa.feature.zero_crossing_rate(y).mean()
    spec_c  = librosa.feature.spectral_centroid(y=y, sr=sr).mean()
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr).mean()
    contrast= librosa.feature.spectral_contrast(y=y, sr=sr).mean(axis=1)
    chroma  = librosa.feature.chroma_stft(y=y, sr=sr).mean(axis=1)

    melspec  = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    log_mel  = librosa.power_to_db(melspec, ref=np.max)
    mel_mean = log_mel.mean(axis=1)

    return np.concatenate([
      [tempo, onset_rate, rmse, zcr, spec_c, spec_bw],
      contrast,
      chroma,
      mel_mean
    ]).astype(float)

def run_svm_prediction(gcs_path: str, svm_endpoint) -> dict:
    # 1) Download MP3
    local_mp3 = "/tmp/input.mp3"
    bucket    = storage_client.bucket(INPUT_BUCKET)
    bucket.blob(gcs_path).download_to_filename(local_mp3)

    # 2) Extract 153‑dim features
    feats = extract_153_features(local_mp3)

    # 3) Call your SVM pipeline endpoint
    resp = svm_endpoint.predict(instances=[feats.tolist()])
    note = int(resp.predictions[0][0])

    return {"predicted_note": note}
