# ------------------------------------------------------------------------------
#  © 2025 Monobina Bhowmick-Saha
#  Original Repo: https://github.com/monobinab-source/ai-ml/tree/main/emeritus-ai-ml/music_transcribe
#  Licensed under the MIT License. See the LICENSE file for details.
# ------------------------------------------------------------------------------

import functions_framework
from google.cloud import aiplatform, storage
from vertexai.preview import generative_models
import json
from utils import run_vertex_ai_prediction
from svm_utils import run_svm_prediction

project_id = 'monobina-saha'
location = 'us-central1'
audio_to_midi_endpoint_id = '8135775816588984320'
svm_endpoint = '1340547666328682496'


aiplatform.init(project=project_id, location=location)
audio_to_midi_endpoint = aiplatform.Endpoint(audio_to_midi_endpoint_id)
model = generative_models.GenerativeModel("gemini-1.5-flash")

@functions_framework.http
def audio_to_midi(request):
    request_json = request.get_json(silent=True)

    user_prompt = request_json.get("prompt")
    audio_file_name = request_json.get("audio_file")

    gemini_response = model.generate_content(user_prompt)

    if "transcribe" in gemini_response.text.lower() and audio_file_name:
        prediction = run_vertex_ai_prediction(audio_file_name, audio_to_midi_endpoint)

        most_common_note = prediction['most_common_note']

        # svm_out = run_svm_prediction(audio_file_name, svm_endpoint)
        # note_svm = svm_out['predicted_note']

        # Generate caption & mood from predicted piano roll notes
        caption_prompt = f"""This is piano music extracted from the audio file: {audio_file_name}.
        The piano roll shows:
        - {prediction['piano_roll_summary']}
        Most common note is {prediction['most_common_note']}.
        Generate a short creative caption describing this music.
        """

        mood_prompt = f"""Given this music with pattern:
        - {prediction['piano_roll_summary']}
        What is a likely single-word mood for this music? Reply with only one word like Calm / Energetic / Sad / Happy / Aggressive.
        """

        caption_response = model.generate_content(caption_prompt)
        mood_response = model.generate_content(mood_prompt)


        reply = f"Prediction complete! Most common note is {most_common_note}."

        return json.dumps({
            "response": reply,
            "piano_roll_npy_gcs_path": prediction["piano_roll_npy_gcs_path"],
            "embedding_npy_gcs_path": prediction["embedding_npy_gcs_path"],
            "piano_roll_summary": prediction['piano_roll_summary'],
            "audio_caption": caption_response.text,
            "music_mood": mood_response.text,
            # "svm_note": note_svm
        })

    return json.dumps({"response": gemini_response.text})
