<small>
------------------------------------------------------------------------------
 
© 2025 Monobina Bhowmick-Saha  
Original Repo: https://github.com/monobinab-source/ai-ml/tree/main/emeritus-ai-ml/music_transcribe  
Licensed under the MIT License. See the LICENSE file for details.  

------------------------------------------------------------------------------
</small>



## Overview
Automatically transforming music signals in audio recording into notes or score representation of a music piece is a challenge that artists achieve over many years of learning and practising music. For beginner musicians it is a challenge to find notes of music unless their teachers help them or they find one done by someone else on the internet.  The goal of Automatic Music Transcription (AMT) is to produce a score representation of a music piece, by analyzing a sound signal. A processing pipeline is designed that can transform classical piano audio files in .mp3 format into a music score representation.

### What Is Included Here
1. Deep learning models e.g. CNN and sequnetial models e.g. LSTM to transcribe piano music from MP3 to MIDI
2. Used classical ML to detect note patterns
3. Used Gemini LLM to summarize mood and structure
4. Tried synthesizing back to audio from predicted MIDI (which needs more experimentation)
5. All built and deployed on Google Cloud (Vertex AI, GCS, Cloud Functions)

<img width="644" alt="image" src="https://github.com/user-attachments/assets/0a500e36-e63a-4cb1-944c-b3dabc2fcea9" />


## Data Needed to solve the use case
Music audio files and corresponding MIDI files for training and testing. MIDI files contain symbolic musical information (notes, duration, velocity, etc.).
For simplicity we will consider monophonic music meaning one source e.g. one instrument.
MP3 and MIDI files for classical Piano performances:
https://www.kaggle.com/datasets/jackvial/themaestrodatasetv2/data


## Data processing:

1. Audio files cannot be fed to the model as they are too large and complex for model input. Convert audio to spectrogram, which is a visual representation of the spectrum of frequencies in the audio over time. The spectrogram captures the essential features in a compact and structured format. Spectrogram is a 2D array that shows how the frequency content of the sound changes over time.

2. MIDI files will be converted to piano roll representation (a 2D matrix), which is numerical matrices.

3. Spectrograms derived from audio files will act as features for the model and piano roll matrices are the output. The training will be supervised learning where the model will be fed with features and expected output.

4. The training pipeline will contain the Audio (waveform) conversion to spectrogram and MIDI to Piano roll, which is target or label.

5. The waveform and MIDI file are split into pieces to create the training dataset. 

## Feature Extraction
We can extract Mel Spectrogram and MFCCs (Mel-Frequency Cepstral Coefficients), which are widely used for audio classification. Why use these features?

Mel Spectrogram represents how sound energy is distributed across frequencies over time.

1. MFCCs: This is useful for distinguishing different sounds (used in speech recognition and music classification). They capture the spectral envelope of the sound and are robust to variations in loudness and recording conditions.

2. Spectral Centroid: This feature represents the "center of mass" of the spectrum, indicating the average frequency weighted by amplitude.

3. Spectral Bandwidth: This measures the width of the spectrum, indicating the range of frequencies present in the sound.

4. Zero-Crossing Rate: This feature counts the number of times the audio waveform crosses zero, providing information about the frequency content and noisiness of the sound.

5. Chroma Features: These represent the distribution of energy across the 12 chromatic pitches (C, C#, D, etc.), providing information about the harmonic content of the music.

6. Note Onsets and Offsets: You can extract the time points where notes start (onsets) and end (offsets) to analyze rhythmic patterns.



## Classical ML Modeling and training:

### SVM
SVM is good at small-sample, high dimensional tasks. It is a reliable and interpretable algorithm for classification tasks. It is used to classify each audio slice by predicting its most frequent MIDI note using Support Vector Machine (SVM). It can summarize about the audio.

### Convolutional Neural Network (CNN) Model
CNN is used for music transcription after extracting the mel-spectogram from the audio.
It can be used for modeling because it can process 2D (time-frequency) data and it is good for complex information processing. CNNs are popularly used in image classification, object detection and speech recognition. It is also in learning features like onsets and offsets when notes start and end, harmonic structures to identify relationships between fundamental frequencies and their harmonics. Hence the training will be done using spectrogram feature matrices and piano roll output matrices. Hyperparameter tuning is performed by adjusting number of filters, kernel size, dropout and learning rate. The F1 score of the best model architecture was analysed and while F1 is pretty low as expected for this range of multilabel classification task, it can be used as a baseline model.

### Long Short Term Memory (LSTM) Model
LSTM model is a type of Recurrent Neural Network (RNN) designed to handle sequential data and capture long-term dependencies more effectively than traditional RNNs. Since there is time component in my dataset, it may perform better than CNN.
A few architecture was starting with simple and by increasing complexity by stacking more layers and using unidirectional and bidirectional layer, which can give past and future context for each frame, it is found that simpler architecture is better as baseline model based on the dataset used.

## Evaluation:
A portion of audio files will be kept aside for model evaluation. Once the model is trained I will generate predictions using the spectrograms of evaluation audio files. The output will be piano rolls and these piano rolls can be converted back to MIDI files to find the loss function and compare the accuracy of prediction.

## Model Deployment
I used Google Cloud to develop and deploy. GCS is used as data lake to store raw data files, processed data, X and Y numpy files and saved models once they are built. I deployed the model endpoints in Vertex AI. I built an application in Cloud Functions which can be invoked for model inference.

![image](https://github.com/user-attachments/assets/a0bf1b59-c768-4073-8b4e-653debd9c782)


## Gen AI Implementation
Generative AI library, Gemini, is integrated in the application, which enables user to ask questions about a song by passing as parameters a mp3 formated song and a prompt e.g. "Transcribe my audio file and tell me the most common note". Deployed the Gen AI app in Cloud Run Functions of GCP.

An example curl command to invoke this application:

curl -X POST https://audio2midi-model-call-353746728936.us-central1.run.app \
-H "Authorization: bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
"prompt": "Transcribe my audio file and tell me the most common note",
"audio_file": "2018/MIDI-Unprocessed_Chamber1_MID--AUDIO_07_R3_2018_wav--2.mp3"
}'

Response:
{"response": "Prediction complete! Most common note is 10.", 
"piano_roll_npy_gcs_path": "gs://predicted_piano_roll/2018/MIDI-Unprocessed_Chamber1_MID--AUDIO_07_R3_2018_wav--2_piano_roll.npy", 
"embedding_npy_gcs_path": "gs://predicted_piano_roll/2018/MIDI-Unprocessed_Chamber1_MID--AUDIO_07_R3_2018_wav--2_embedding.npy", 
"piano_roll_summary": "The piano roll has 88 active notes out of 88 possible keys, over a duration of 100 time steps, with an average note density of 2.88 notes per time step.", 
"audio_caption": "A cascading tapestry of sound, woven from the full spectrum of the piano, with a persistent pulse of the note 10 echoing throughout. This is a piece that feels both expansive and intimate, full of life and nuanced detail. \n", 
"music_mood": "Energetic \n"}

The app first calls the Vertex AI model endpoints and predict the MIDI file output and Gemini analyzes the MIDI output to detect the mood and the audio caption of the audio.

## Model Inference:
The SVM and CNN models are saved in Vertex AI endpoint and can be invoked for inference. The app is deployed in Google Cloud Run Funtions, which invokes these model endpoints, and the app can be invoked using curl command or python library. The app also generates a summary using Gemini.

## Future Enhancements to Improve Accuracy
1. Try transformer model, transfer learning for better music trasncription using model prediction for MIDI notes.
2. Enhance pre and post processings and experiment with different sizes of time slices.
3. Train with more data. Check if simpler songs and midi files can be collected for better training purposes.
4. USe feedback loop for fine tuning.

## Automated Retraining: 
1. Use Vertex AI Pipelines to periodically retrain models as new data becomes available.
2. Monitoring & Alerts: Set up model monitoring to track drift and raise alerts when performance degrades.

