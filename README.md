
 Audio Digit Classification using DSP

 Project Overview

This project focuses on classifying spoken digits (0–9) using Digital Signal Processing (DSP) techniques. Multiple signal analysis approaches are implemented to extract meaningful features from audio signals and evaluate their effectiveness for classification.

Dataset used: **Free Spoken Digit Dataset (FSDD)** (8 kHz mono recordings)

---

 Methodology

The project is divided into three main analysis approaches:

---

 1. Time-Domain Analysis

This approach analyzes signals directly in the time domain to capture temporal characteristics of speech.

  Audio Loading and Preprocessing

* Signals are loaded from WAV files
* Converted to single channel
* Normalized for consistency
* Sampling rate: 8 kHz

 Extracted Features

 • Zero-Crossing Rate (ZCR)

Measures how frequently the signal crosses zero:

* High ZCR → more rapid variations
* Low ZCR → smoother signals

 • Signal Energy

Measures signal strength:

* High energy → louder signals
* Low energy → quieter signals

 • Signal Envelope

Represents the overall shape of the waveform:

* Smooths rapid oscillations
* Highlights speech regions
* Shows amplitude trends over time

---

 2. Frequency-Domain Analysis (DFT-Based)

This approach converts signals into the frequency domain using FFT to analyze spectral content.

 Fast Fourier Transform (FFT)

Transforms signals from time domain → frequency domain:

* Frequency axis (Hz)
* Magnitude spectrum

---

 Extracted Features

 • Spectral Centroid

“Center of mass” of the spectrum
→ Indicates where energy is concentrated

 • Spectral Bandwidth

Measures spread of frequencies
→ Narrow vs wide frequency distribution

• Peak Frequency

Frequency with highest magnitude
→ Dominant component

• Spectral Energy

Total signal energy in frequency domain

---

 Band Energy Features

Energy distribution across frequency bands:

* Low (0–500 Hz)
* Mid (500–2000 Hz)
* High (>2000 Hz)

---

 Spectral Rolloff

Frequency below which 85% of energy is contained
→ Indicates energy concentration

---

 DSP Concepts Studied

 Spectral Leakage & Windowing

* Leakage occurs when signals are not perfectly periodic
* Windowing (Hamming) reduces leakage

 Frequency Resolution

* Depends on signal length
* Longer signals → better resolution

Zero-Padding

* Increases FFT points
* Produces smoother spectra
* Does NOT add new information

---

 Advanced Features

 • MFCC (Mel-Frequency Cepstral Coefficients)

* Models human auditory perception
* Widely used in speech recognition

 • Formant Frequencies (LPC-Based)

* Represent vocal tract resonances
* Estimated using LPC for accuracy

 • Harmonic-to-Noise Ratio (HNR)

* Measures periodic vs noisy components
* Higher → cleaner signal

---

 3. STFT-Based Analysis

Short-Time Fourier Transform (STFT) provides time-frequency analysis.

 Tasks Performed

* Implemented STFT
* Generated spectrograms
* Extracted short-time spectral features

 Effects Studied

* Window type (Hamming, etc.)
* Window length
* Overlap between frames

---



  Steps

* Feature extraction (time, frequency, STFT)
* Dataset preparation
* Model training
* Performance evaluation

---

 Results & Observations

* Speech signals show strong low-frequency components
* Different digits exhibit distinct spectral characteristics
* Some overlap exists between classes
* Frequency-domain features are effective but not sufficient alone
* Combining multiple features improves classification

---

 Dataset

Download from:
https://github.com/Jakobovski/free-spoken-digit-dataset

Place in:

```
data/recordings/
```



 Output

* Feature dataset (`dft_features.csv`)
* Time-domain plots
* Frequency spectra
* Spectrograms (STFT)
* Feature visualizations
* Classification results

---

 Team Contributions

 Abdulmajeed Alhumaidi – Time-Domain Analysis

  * Implemented ZCR, energy, envelope
  * Analyzed temporal features

 Ibrahim Alradhyan – Frequency-Domain (DFT)

  * Implemented FFT-based feature extraction
  * Studied spectral properties, zero-padding, resolution

 Albara Alamasi – STFT Analysis

  * Implemented STFT
  * Extracted time-frequency features
  * Analyzed windowing effects

---

 AI Assistance

AI tools (ChatGPT) were used for:

* Code structuring and debugging
* Documentation formatting
* Concept clarification

All implementations were understood, verified, and modified by the team.

---

 Conclusion

DSP techniques provide valuable insights into speech signals.
While individual feature sets show useful patterns, combining multiple approaches yields better classification performance.

