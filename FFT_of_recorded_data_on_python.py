import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec
from scipy.fftpack import fft
from numpy.fft import fftfreq, ifft, fftshift
import numpy as np

#read data from csv
df=pd.read_csv("DATA.CSV")
df_values_ADC0=df['ADC0']
t=df['Time_ADC0']

df_values_ADC2=df['ADC2']
t_ACD2=df['Time_ADC2']

df_values_ADC4=df['ADC4']
t_ACD4=df['Time_ADC4']

df_values_ADC7=df['ADC7']
t_ACD7=df['Time_ADC7']

#SAMPLING RATE
Fs=1000000/(t[1]-t[0]) #Number of samples per second
#TIME FRAME
T=t[499]/1000000 #Total time
#BLOCK SIZE
N=500
SL=N/2 #Spectral lines
#MAX FREQUENCY
Fmax=Fs/2 #This should be the stop of freq axis
#frequency res
FR=Fmax/SL #Frequency resolution

#generate frequency axis
freq_axis=np.linspace(0,Fmax,int(SL))

#calculate FFT
X_ACD0=np.fft.fft(df_values_ADC0)
X_mag_ACD0=np.abs(X_ACD0)/N
X_mag_ACD0[0]=0

X_ACD2=np.fft.fft(df_values_ADC2)
X_mag_ACD2=np.abs(X_ACD2)/N
X_mag_ACD2[0]=0

X_ACD4=np.fft.fft(df_values_ADC4)
X_mag_ACD4=np.abs(X_ACD4)/N
X_mag_ACD4[0]=0

X_ACD7=np.fft.fft(df_values_ADC7)
X_mag_ACD7=np.abs(X_ACD7)/N
X_mag_ACD7[0]=0

#set figure layout
plt.rcParams['figure.figsize']=(20,18)
fig,ax =plt.subplots(4,2)

#plotting the graphs
ax[0,0].plot(t,df_values_ADC0, label='ACD0 Time series')
ax[0,0].set_xlabel("Time (ms)")
ax[0,0].set_ylabel("Amplitude (ADC0)")
ax[0,0].set_title("Time series")
ax[0,1].plot(freq_axis,X_mag_ACD0[1:251])
ax[0,1].set_ylabel("Magnitude (ADC0)")
ax[0,1].set_xlabel("Frequency (Hz)")
ax[0,1].set_title("Frequency series")

ax[1,0].plot(t,df_values_ADC2,'tab:green')
ax[1,0].set_xlabel("Time (ms)")
ax[1,0].set_ylabel("Amplitude (ADC2)")
ax[1,1].plot(freq_axis,X_mag_ACD2[1:251],'tab:green')
ax[1,1].set_ylabel("Magnitude (ADC2)")
ax[1,1].set_xlabel("Frequency (Hz)")

ax[2,0].plot(t,df_values_ADC4,'tab:orange')
ax[2,0].set_xlabel("Time (ms)")
ax[2,0].set_ylabel("Amplitude (ADC4)")
ax[2,1].plot(freq_axis,X_mag_ACD4[1:251],'tab:orange')
ax[2,1].set_ylabel("Magnitude (ADC4)")
ax[2,1].set_xlabel("Frequency (Hz)")

ax[3,0].plot(t,df_values_ADC7,'tab:red')
ax[3,0].set_xlabel("Time (ms)")
ax[3,0].set_ylabel("Amplitude (ADC7)")
ax[3,1].plot(freq_axis,X_mag_ACD7[1:251],'tab:red')
ax[3,1].set_ylabel("Magnitude (ADC7)")
ax[3,1].set_xlabel("Frequency (Hz)")

# for ax in ax.flat:
#     ax.set(xlabel='Frequency (Hz)',ylabel='Amplitude')    

plt.show()
