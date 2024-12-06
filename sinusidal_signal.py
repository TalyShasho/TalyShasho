import numpy as np
import matplotlib.pyplot as plt

def downsample_signal(signal, target_percentage):
    """
    Downsamples a sinusoidal signal while preserving all maxima and minima points.

    """
    # Find maxima and minima
    maxima_indices = (np.diff(np.sign(np.diff(signal))) < 0).nonzero()[0] + 1
    minima_indices = (np.diff(np.sign(np.diff(signal))) > 0).nonzero()[0] + 1
    extrema_indices = np.sort(np.concatenate((maxima_indices, minima_indices)))

    #  points to retain
    target_points = int(len(signal) * target_percentage)

    # Select points evenly spaced, including extrema
    evenly_spaced_indices = np.linspace(0, len(signal) - 1, target_points, dtype=int)
    selected_indices = np.unique(np.sort(np.concatenate((extrema_indices, evenly_spaced_indices))))

    return selected_indices, signal[selected_indices]


if __name__ == "__main__":
    #  sinusoidal signal
    t = np.arange(0, 1, 0.01)  # 0 to 1 seconds,  every 0.01 seconds
    frequency = 5  # Frequency 5 Hz
    signal = np.sin(2 * np.pi * frequency * t)

    # Downsample the signal
    target_percentage = 0.2  #  20% of points
    indices, downsampled_signal = downsample_signal(signal, target_percentage)

    # Plot original signal
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, signal, label="Original Signal", linewidth=2)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Original Signal")
    plt.grid()
    

    # Plot downsampled signal
    plt.subplot(2, 1, 2)
    plt.plot(t[indices], downsampled_signal, 'o-', label="Downsampled Signal", linewidth=2, color='orange')
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Downsampled Signal (20% of Original Points)")
    plt.grid()



    plt.tight_layout()
    plt.show()
