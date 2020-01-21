# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 07:36:19 2020

@author: ASUS I5
"""
import numpy as np
import matplotlib.pyplot as plt
import tes as sigs # Chapter 0
from scipy.fftpack import fft,ifft
from scipy import signal

# fft transformation to detect frequency spectral for each time series signal
freq_domain_signal = fft(sigs.prueba_Dataset)
plt.stem(freq_domain_signal)
plt.xlim(0,100)
plt.show()
#valor max de x =175
#grafica está dividida en 7 segmentos
#frecuencia de muestreo es de 100Hz

#50 -> 14.5 Hz
#25-> 7.25  Hz
#5-> 1.45   Hz

######filtros FIR
#vector de analisis normalizado
signal_pruebadata=np.zeros(len(sigs.prueba_Dataset))

#normalizar la señal de entrada
for i,num in enumerate (sigs.prueba_Dataset):
    signal_pruebadata[i]=float(sigs.prueba_Dataset[i]/max(sigs.prueba_Dataset))
    
#grafica normalizada
plt.plot(signal_pruebadata)
plt.legend(loc='best')
plt.grid()
plt.show()    

#generación de filtro por ventana
###############################################################################
"""FILTRO PASA BANDA"""
bandpas_coef=signal.firwin(43,[2,20],nyq=100,pass_zero=False,window='blackman')

#grafica de coeficientes
plt.plot(bandpas_coef)
plt.legend(loc='best')
plt.grid()
plt.show()

###############################################################################
#convolucion
signal_output=signal.convolve(signal_pruebadata,bandpas_coef,mode='same')
#grafica de resultados

f,plt_arr=plt.subplots(2,sharex=True)
f.suptitle('Aplicaciones de ventanas')
plt_arr[0].plot(signal_pruebadata,color='m')
plt_arr[0].set_title('Señal de entrada')
plt_arr[1].plot(signal_output,color='c')
plt_arr[1].set_title('filtro pasa banda de 2 a 10 Hz')

###############################################################################


"""FILTRO PASA BAJO"""

lowpass_coef=signal.firwin(21,2,pass_zero=False,nyq=100,window='blackman')
plt.plot(lowpass_coef, label='Señal de entrada')
plt.grid()
plt.legend(loc='best')
plt.show()

signal_output1=signal.convolve(signal_pruebadata,lowpass_coef,mode='same')
f,plt_arr=plt.subplots(2,sharex=True)
f.suptitle('Aplicaciones de ventanas')
plt_arr[0].plot(signal_pruebadata,color='blue')
plt_arr[0].set_title('señalde entrada')
plt_arr[1].plot(signal_output1,color='green')
plt_arr[1].set_title('Filtro pasa bajo 2Hz')



"""FILTRO PASA ALTO"""
highpass_coef=signal.firwin(43,2,pass_zero=True,nyq=100,window='blackman')
plt.plot(lowpass_coef, label='Señal de entrada')
plt.grid()
plt.legend(loc='best')
plt.show()
signal_output2=signal.convolve(signal_pruebadata,highpass_coef,mode='same')
f,plt_arr=plt.subplots(2,sharex=True)
f.suptitle('Aplicaciones de ventanas')
plt_arr[0].plot(signal_pruebadata,color='red')
plt_arr[0].set_title('señal de entrada')
plt_arr[1].plot(signal_output2,color='yellow')
plt_arr[1].set_title('filtro pasa alto 2Hz')












"""                Butter,chev,bessel               """


import tes as sigs
from matplotlib import pyplot as plt
import numpy as np
from scipy.fftpack  import fft, fftshift
from numpy import cos,sin,pi,arange,absolute
from scipy import signal


freq_domain_signal = fft(sigs.prueba_Dataset)
plt.stem(freq_domain_signal)
plt.xlim(0,100)
plt.show()
#valor max de x =175
#grafica está dividida en 7 segmentos
#frecuencia de muestreo es de 100Hz

#50 -> 14.5 Hz
#25-> 7.25  Hz
#5-> 1.45   Hz

######filtros FIR
#vector de analisis normalizado
signal_pruebadata=np.zeros(len(sigs.prueba_Dataset))

#normalizar la señal de entrada
for i,num in enumerate (sigs.prueba_Dataset):
    signal_pruebadata[i]=float(sigs.prueba_Dataset[i]/max(sigs.prueba_Dataset))
    
#grafica normalizada
plt.plot(signal_pruebadata)
plt.legend(loc='best')
plt.grid()
plt.show()    


##chevy
lowpass_filter = signal.cheby1(8, 5,40,'lp', fs=100,analog=False, output='sos')
lowpass_filter
filtered=signal.sosfilt(lowpass_filter,signal_pruebadata)

f,plt_arr=plt.subplots(2,sharex=True)
f.suptitle("Filtro IIR")
plt_arr[0].plot(signal_pruebadata,color='blue')
plt_arr[0].set_title('señal de entrada')
plt_arr[1].plot(filtered,color='red')
plt_arr[1].set_title('señal filtrada')


#butter
lowpassbutter = signal.butter(1, 5, 'lp', fs=100,analog=False, output='sos')
lowpass_filter
filtered=signal.sosfilt(lowpassbutter,signal_pruebadata)

f,plt_arr=plt.subplots(2,sharex=True)
f.suptitle("Filtro IIR")
plt_arr[0].plot(signal_pruebadata,color='blue')
plt_arr[0].set_title('señal de entrada')
plt_arr[1].plot(filtered,color='yellow')
plt_arr[1].set_title('señal filtrada')

#bessel
lowpassbessel = signal.bessel(5, 3, 'lp', fs=100,analog=False, output='sos')
lowpass_filter
filtered=signal.sosfilt(lowpassbessel,signal_pruebadata)

f,plt_arr=plt.subplots(2,sharex=True)
f.suptitle("Filtro IIR")
plt_arr[0].plot(signal_pruebadata,color='blue')
plt_arr[0].set_title('señal de entrada')
plt_arr[1].plot(filtered,color='green')
plt_arr[1].set_title('señal filtrada ')
