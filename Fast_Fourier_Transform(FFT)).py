import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import csv
from scipy.signal import find_peaks
import matplotlib.patches as mpatches

#read data from csv
df_1=pd.read_csv("undamaged_220120_01.CSV")
t=df_1['Time_ADC0']
df_1_values_ADC0=df_1['ADC0']
df_1_values_ADC2=df_1['ADC2']
df_1_values_ADC4=df_1['ADC4']
df_1_values_ADC7=df_1['ADC7']

a=pd.Series(ADC0)
b=pd.Series(ADC2)
c=pd.Series(ADC4)
d=pd.Series(ADC7)

#Applying Fast Fourier Transfrom (FFT) on the recorded data
#BLOCK SIZE
N=200
n=N/2
#SAMPLING RATE
Fs=1000000/(t[1]-t[0]) #Number of samples per second
#TIME FRAME
T=t[N-1]/1000000 #Total time

SL=N/2 #Spectral lines
#MAX FREQUENCY
Fmax=Fs/2 #This should be the stop of freq axis
#frequency res
FR=Fmax/SL #Frequency resolution

#generate frequency axis
freq_axis=np.linspace(0,Fmax,int(SL))

#calculate FFT
X_ADC0=np.fft.fft(a)
X_mag_ADC0=np.abs(X_ADC0)/N
X_mag_ADC0[0]=0

X_ADC2=np.fft.fft(b)
X_mag_ADC2=np.abs(X_ADC2)/N
X_mag_ADC2[0]=0

X_ADC4=np.fft.fft(c)
X_mag_ADC4=np.abs(X_ADC4)/N
X_mag_ADC4[0]=0

X_ADC7=np.fft.fft(d)
X_mag_ADC7=np.abs(X_ADC7)/N
X_mag_ADC7[0]=0

#set figure layout
plt.rcParams['figure.figsize']=(9,12)
fig,ax=plt.subplots(4,2)

#plotting the graphs
ax[0,0].plot(t,a)
ax[0,0].set_xlabel("Time (us)",fontsize=8)
ax[0,0].set_ylabel("Amplitude (ADC0) [a.u]",fontsize=8)
ax[0,0].set_title("Time series Graphs",fontsize=10)
blue_patch = mpatches.Patch(color='blue', label='Sensor Data at 12 O clock')
ax[0,0].legend(handles=[blue_patch])

ax[0,1].fill_between(freq_axis,X_mag_ADC0[0:int(n)],facecolor='C0',alpha=0.87)
ax[0,1].set_ylabel("Magnitude (ADC0)",fontsize=8)
ax[0,1].set_xlabel("Frequency (Hz)",fontsize=8)
#ax[0,1].set_title(r'$ x[k] = \sum_{n=0}^{N-1} x[n] e^{ \frac{-j 2 \pi k n}{N}} $' ,fontsize=20)
ax[0,1].set_title("Frequency series Graphs",fontsize=10)
blue_patch = mpatches.Patch(color='blue', label='Sensor Data at 12 O clock')
ax[0,1].legend(handles=[blue_patch])

ax[1,0].plot(t,b,'tab:green')
ax[1,0].set_xlabel("Time (us)",fontsize=8)
ax[1,0].set_ylabel("Amplitude (ADC2) [a.u]",fontsize=8)
green_patch = mpatches.Patch(color='green', label='Sensor Data at 10 O clock')
ax[1,0].legend(handles=[green_patch])
ax[1,1].fill_between(freq_axis,X_mag_ADC2[0:int(n)],facecolor='C2',alpha=0.8)
ax[1,1].set_ylabel("Magnitude (ADC2)",fontsize=8)
ax[1,1].set_xlabel("Frequency (Hz)",fontsize=8)
green_patch = mpatches.Patch(color='green', label='Sensor Data at 10 O clock')
ax[1,1].legend(handles=[green_patch])

ax[2,0].plot(t,c,'tab:orange')
ax[2,0].set_xlabel("Time (us)",fontsize=8)
ax[2,0].set_ylabel("Amplitude (ADC4) [a.u]",fontsize=8)
orange_patch = mpatches.Patch(color='orange', label='Sensor Data at 8 O clock')
ax[2,0].legend(handles=[orange_patch])
ax[2,1].fill_between(freq_axis,X_mag_ADC4[0:int(n)],facecolor='C1',alpha=0.8)
ax[2,1].set_ylabel("Magnitude (ADC4)",fontsize=8)
ax[2,1].set_xlabel("Frequency (Hz)",fontsize=8)
orange_patch = mpatches.Patch(color='orange', label='Sensor Data at 8 O clock')
ax[2,1].legend(handles=[orange_patch])

ax[3,0].plot(t,d,'tab:red')
ax[3,0].set_xlabel("Time (us)",fontsize=8)
ax[3,0].set_ylabel("Amplitude (ADC7) [a.u]",fontsize=8)
red_patch = mpatches.Patch(color='red', label='Sensor Data at 6 O clock')
ax[3,0].legend(handles=[red_patch])
ax[3,1].fill_between(freq_axis,X_mag_ADC7[0:int(n)],facecolor='C3',alpha=0.8)
ax[3,1].set_ylabel("Magnitude (ADC7)",fontsize=8)
ax[3,1].set_xlabel("Frequency (Hz)",fontsize=8)
red_patch = mpatches.Patch(color='red', label='Sensor Data at 6 O clock')
ax[3,1].legend(handles=[red_patch])
# for ax in ax.flat:
#     ax.set(xlabel='Frequency (Hz)',ylabel='Amplitude')    
plt.show()
