import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
from scipy.io.wavfile import read
from scipy import signal
import wave



# Number of samplepoints
N = 100 
# sample spacing
T = 1.0 / 10 #greater deo --> more spread x axis
x = np.linspace(0.0, N*T, N)
y = np.sin(1*2.0*np.pi*x)+np.cos(2*2.0*np.pi*x)
#y = signal.unit_impulse(50, 'mid')
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)

fig, ax = plt.subplots()
ax.plot(xf, 2.0/N * np.abs(yf[:N//2]))
#plt.plot(x, y)
plt.grid(color = 'black', linestyle = '--', linewidth = 0.5)
plt.xlabel(r"frequency (Hz)")
#plt.xlabel("time")
plt.ylabel("strength of frequency in g(x)")
#plt.ylabel("amplitude")
plt.title("Freq Domain")
#plt.title("Spatial Domain")
txt="Number of sample points: " + str(N)
plt.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=12)
plt.show()
