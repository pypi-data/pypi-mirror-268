import wave
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

class Plot:
    
    @staticmethod
    def plot_line(diffrence, seconds):
        plt.figure(figsize=(10, 6))
            
        plt.plot(seconds, diffrence, color='b', linestyle='-')

        plt.title('Frequency Difference Progression Over Time')
        plt.xlabel('Seconds')
        plt.ylabel('Frequency Difference (Hz)')
        
        
        plt.grid(True, linestyle='--', alpha=0.5)

        plt.legend(['Frequency Difference'], loc='upper right')
        
        # Show the plot
        plt.show()

    @staticmethod
    def visualize_audio(audio_path):
        # Load audio file
        y, sr = librosa.load(audio_path)

        # Create a time array
        time = librosa.times_like(y, sr=sr)

        # Plot waveform
        plt.figure(figsize=(10, 4))
        librosa.display.waveshow(y, sr=sr)
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title('Waveform')
        plt.show()
    
    @staticmethod
    def plot_waveform(audio_path):

        y, sr = librosa.load(audio_path)
        # Plot the waveform
        plt.figure(figsize=(12, 6))
        plt.subplot(3, 1, 1)
        librosa.display.waveshow(y, sr=sr, color='blue')  # Explicitly specify the color
        plt.title('Waveform')
        plt.show()

    @staticmethod
    def plot_waveform2(audio_path, sample_rate=44100):
        # Load audio file
        y, sr = librosa.load(audio_path, sr=sample_rate, mono=False)

        # Calculate time axis
        time = np.linspace(0, len(y[0]) / sr, len(y[0]))

        # Calculate frequency difference between the two channels
        freq_diff = np.abs(librosa.core.piptrack(y=y, sr=sr, hop_length=512)[1] - librosa.core.piptrack(y=y, sr=sr, hop_length=512)[0])
        
        # Take the mean across time frames
        freq_diff_mean = np.mean(freq_diff, axis=1)

        # Plot the waveform
        plt.figure(figsize=(12, 6))
        plt.plot(time, freq_diff_mean, color='blue')  # Plot time against frequency difference
        plt.title('Frequency Difference Between Channels Over Time')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency Difference (Hz)')
        plt.grid(True)
        plt.show()