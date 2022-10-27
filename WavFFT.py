import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
import numpy as np
fs, data = wavfile.read(r'C:\Users\Ishaan Ganti\Desktop\Everything\python\math\440 Hz (10 seconds of A).wav') #replace with the path to the audio file
#plt.plot(data.T[0])
a = data.T[0] # Take first track
b=[(ele/2**8.)*2-1 for ele in a] # Normalize
c = fft(b)
d = len(c)//2  #Real signal symmetry; only take 1/2
k = np.arange(3, len(data), 2)
T = len(data)/fs  #fs = sampling frequency
frqLabel = k/(T*2)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Strength of frequency in wav file")
plt.plot(frqLabel, abs(c[:(d-1)]),'r')
plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)
plt.title("A Note Fourier Transformed")

plt.show()
