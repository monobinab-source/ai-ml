## Overview
Automatically transforming music signals in audio recording into notes or score representation of a music piece is a challenge that artists achieve over many years of learning and practising music. For beginner musicians it is a challenge to find notes of music unless their teachers help them or they find one done by someone else on the internet.  The goal of Automatic Music Transcription (AMT) is to produce a score representation of a music piece, by analyzing a sound signal. A processing pipeline needs to be designed that can transform classical piano audio files in .wav format into a music score representation.

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



## Modeling and training:
### K Nearest Neighbor Classifier


### Convolutional Neural Network (CNN) 
It can be used for modeling because it can process 2D (time-frequency) data and it is good for complex information processing. CNNs are popularly used in image classification, object detection and speech recognition. It is also in learning features like onsets and offsets when notes start and end, harmonic structures to identify relationships between fundamental frequencies and their harmonics. Hence the training will be done using spectrogram feature matrices and piano roll output matrices.

Evaluation:
A portion of audio files will be kept aside for model evaluation. Once the model is trained I will generate predictions using the spectrograms of evaluation audio files. The output will be piano rolls and these piano rolls can be converted back to MIDI files to find the loss function and compare the accuracy of prediction.


