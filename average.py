import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import csv
from scipy.signal import find_peaks
import matplotlib.patches as mpatches

#read data from csv

df_1=pd.read_csv("undamaged_220120_01.CSV")
df_2=pd.read_csv("undamaged_220120_02.CSV")
#df_3=pd.read_csv("undamaged_220120_03.CSV")
df_4=pd.read_csv("undamaged_220120_04.CSV")
df_5=pd.read_csv("undamaged_220120_05.CSV")
df_6=pd.read_csv("undamaged_220120_06.CSV")
df_7=pd.read_csv("undamaged_220120_07.CSV")
df_8=pd.read_csv("undamaged_220120_08.CSV")
df_9=pd.read_csv("undamaged_220120_09.CSV")
df_10=pd.read_csv("undamaged_220120_10.CSV")
t=df_1['Time_ADC0']

df_1_values_ADC0=df_1['ADC0']
df_2_values_ADC0=df_2['ADC0']
#df_3_values_ADC0=df_3['ADC0']
df_4_values_ADC0=df_4['ADC0']
df_5_values_ADC0=df_5['ADC0']
df_6_values_ADC0=df_6['ADC0']
df_7_values_ADC0=df_7['ADC0']
df_8_values_ADC0=df_8['ADC0']
df_9_values_ADC0=df_9['ADC0']
df_10_values_ADC0=df_10['ADC0']

df_1_values_ADC2=df_1['ADC2']
df_2_values_ADC2=df_2['ADC2']
#df_3_values_ADC2=df_3['ADC2']
df_4_values_ADC2=df_4['ADC2']
df_5_values_ADC2=df_5['ADC2']
df_6_values_ADC2=df_6['ADC2']
df_7_values_ADC2=df_7['ADC2']
df_8_values_ADC2=df_8['ADC2']
df_9_values_ADC2=df_9['ADC2']
df_10_values_ADC2=df_10['ADC2']

df_1_values_ADC4=df_1['ADC4']
df_2_values_ADC4=df_2['ADC4']
#df_3_values_ADC4=df_3['ADC4']
df_4_values_ADC4=df_4['ADC4']
df_5_values_ADC4=df_5['ADC4']
df_6_values_ADC4=df_6['ADC4']
df_7_values_ADC4=df_7['ADC4']
df_8_values_ADC4=df_8['ADC4']
df_9_values_ADC4=df_9['ADC4']
df_10_values_ADC4=df_10['ADC4']

df_1_values_ADC7=df_1['ADC7']
df_2_values_ADC7=df_2['ADC7']
#df_3_values_ADC7=df_3['ADC7']
df_4_values_ADC7=df_4['ADC7']
df_5_values_ADC7=df_5['ADC7']
df_6_values_ADC7=df_6['ADC7']
df_7_values_ADC7=df_7['ADC7']
df_8_values_ADC7=df_8['ADC7']
df_9_values_ADC7=df_9['ADC7']
df_10_values_ADC7=df_10['ADC7']

df_avg_values_ADC0=[None]*200
df_avg_values_ADC2=[None]*200
df_avg_values_ADC4=[None]*200
df_avg_values_ADC7=[None]*200

for i in range(200):
    df_avg_values_ADC0[i]=(df_1_values_ADC0[i]+df_2_values_ADC0[i]+df_4_values_ADC0[i]+df_5_values_ADC0[i]+df_6_values_ADC0[i]+df_7_values_ADC0[i]+df_8_values_ADC0[i]+df_9_values_ADC0[i]+df_10_values_ADC0[i])/9

for i in range(200):
    df_avg_values_ADC2[i]=(df_1_values_ADC2[i]+df_2_values_ADC2[i]+df_4_values_ADC2[i]+df_5_values_ADC2[i]+df_6_values_ADC2[i]+df_7_values_ADC2[i]+df_8_values_ADC2[i]+df_9_values_ADC2[i]+df_10_values_ADC2[i])/9

for i in range(200):
    df_avg_values_ADC4[i]=(df_1_values_ADC4[i]+df_2_values_ADC4[i]+df_4_values_ADC4[i]+df_5_values_ADC4[i]+df_6_values_ADC4[i]+df_7_values_ADC4[i]+df_8_values_ADC4[i]+df_9_values_ADC4[i]+df_10_values_ADC4[i])/9

for i in range(200):
    df_avg_values_ADC7[i]=(df_1_values_ADC7[i]+df_2_values_ADC7[i]+df_4_values_ADC7[i]+df_5_values_ADC7[i]+df_6_values_ADC7[i]+df_7_values_ADC7[i]+df_8_values_ADC7[i]+df_9_values_ADC7[i]+df_10_values_ADC7[i])/9


a=pd.Series(df_avg_values_ADC0)
b=pd.Series(df_avg_values_ADC2)
c=pd.Series(df_avg_values_ADC4)
d=pd.Series(df_avg_values_ADC7)


# mean=np.mean(df_avg_values_ADC0)
# peak_x=np.where(df_avg_values_ADC0>mean)[0]
# peak_y=df_avg_values_ADC0[np.where(df_avg_values_ADC0>mean)[0]]
# peak_edges=np.where(np.diff(peak_x)>1)[0]
# peak_list = []
# for i in range(0,len(peak_edges)):
#     try:
#         y_values=peak_y[peak_edges[i]:peak_edges[i+1]].tolist()
#         peak_list.append(peak_x[peak_edges[i]+y_values.index(max(y_values))])
#     except:
#         pass

# peaks, _ = find_peaks(a, height=0)
# b=[None]*len(peaks)
# b=t[peaks]

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

# c=pd.Series(X_mag_ADC0)
# peaks2, _ = find_peaks(c, height=0)
# d=[None]*len(peaks2)
# d=freq_axis[peaks2]


#set figure layout
#plt.rcParams['figure.figsize']=(10,10)
#fig,ax=plt.subplots(4,1)

#plotting the graphs
#plt.plot(t,df_avg_values_ADC0)
#plt.plot(b, a[peaks], "xr"); plt.plot(t,df_avg_values_ADC0)

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
        
        
    
    
    

