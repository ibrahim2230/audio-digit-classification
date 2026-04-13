import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt


def load_audio(file_path):
    """
    Load a WAV audio file.

    Parameters:
        file_path (str): Path to the WAV file.

    Returns:
        sample_rate (int): Sampling frequency.
        signal (np.ndarray): Audio signal as float array.
    """
    sample_rate, signal = wavfile.read(file_path)

    if signal.ndim > 1:
        signal = signal[:, 0]

    signal = signal.astype(np.float64)

    max_val = np.max(np.abs(signal))
    if max_val > 0:
        signal = signal / max_val

    return sample_rate, signal


def compute_fft(signal, sample_rate):
    """
    Compute one-sided FFT magnitude spectrum.

    Parameters:
        signal (np.ndarray): Input signal.
        sample_rate (int): Sampling frequency.

    Returns:
        freqs (np.ndarray): Frequency axis.
        magnitude (np.ndarray): FFT magnitude.
    """
    n = len(signal)
    spectrum = np.fft.rfft(signal)
    magnitude = np.abs(spectrum)
    freqs = np.fft.rfftfreq(n, d=1 / sample_rate)
    return freqs, magnitude


def plot_spectrum(freqs, magnitude, title="Magnitude Spectrum"):
    """
    Plot frequency spectrum.

    Parameters:
        freqs (np.ndarray): Frequency axis.
        magnitude (np.ndarray): Magnitude spectrum.
        title (str): Plot title.
    """
    plt.figure(figsize=(10, 4))
    plt.plot(freqs, magnitude)
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
