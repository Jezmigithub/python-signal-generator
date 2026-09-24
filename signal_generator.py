import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)

frequency = float(input("Enter frequency (Hz): "))
amplitude = float(input("Enter amplitude: "))

choice = input(
    "Choose waveform (1=Sine, 2=Square, 3=Triangle): "
)


if choice == "1":
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    name = "Sine Wave"

elif choice == "2":
    signal = amplitude * np.sign(
        np.sin(2 * np.pi * frequency * t)
    )
    name = "Square Wave"

elif choice == "3":
    signal = amplitude * (
        2 * np.abs(
            2 * (
                frequency * t
                - np.floor(frequency * t + 0.5)
            )
        ) - 1
    )
    name = "Triangle Wave"

else:
    print("Invalid choice. Please choose 1, 2, or 3.")
    signal = None
    
if signal is not None:
    plt.plot(t, signal)
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title(name)
    plt.savefig("signal_plot.png")
    plt.grid()
    plt.show()