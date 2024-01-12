# EEG-signal-processing
EEG signal processing practice

## About this project
EEG signal pre-processing and evaluation after feature extraction using python mne

## Keywords
signal processing, feature extraction, python, mne, TSNE

## Methods

1. get EEG dataset (related to the project)
2. EEG signal pre-processing
3. EEG feature extraction
4. evaluate the extracted feature

### 1. EEG dataset

- Dataset: Data set *‹self-paced 1s›*
- Source: https://www.bbci.de/competition/ii/berlin_desc.html
- Description: the goal is to predict the laterality of upcoming finger movements (left vs. right hand) 130 ms before keypress

### 2. EEG signal pre-processing

- Re-reference: CAR(Common Average Rereference)
- Notch Filter: 50Hz (denoising power line noise of 50Hz)
- Band Pass Filter: 0.01 ~ 50.0Hz (common EEG frequency)
- Down Sampling: 1000Hz -> 500Hz | 1000Hz -> 100Hz

### 3. EEG feature extraction
- Statistical Feature Extraction
- Wavelet Transform
- Principal components analysis
- Singular value decomposition
- Independent component analysis
- Common spatial pattern
- Power Spectral Density

### 4. Evaluation
- t-SNE
- Random Forest
