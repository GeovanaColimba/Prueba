# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 10:29:05 2019

@author: ASUS I5
"""

import pandas as pd  
import signals as sigs
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import numpy as np
from matplotlib import style
import math
from scipy import signal
from scipy.ndimage import gaussian_filter  

"""Datos ruido_1KHz"""
#Elegir la lista a evaluar  
a=sigs.ruido_1KHz
plt.plot(a,label="Señal datos ruido_1KHz",color='g')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal datos ruido_1KHz")
plt.legend(loc='best')
plt.grid()
plt.show() 
series = pd.Series(a) 
cumsum = series.cumsum() 
cumsum
plt.plot(cumsum,label="Suma acumulada",color='y')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Suma acumulada")
plt.legend(loc='best')
plt.grid()
plt.show()

"""Datos ruido_100Hz"""
#Elegir la lista a evaluar  
a=sigs.ruido_100Hz
plt.plot(a,label="Señal datos ruido_100Hz",color='r')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal datos ruido_100Hz")
plt.legend(loc='best')
plt.grid()
plt.show() 
series = pd.Series(a) 
cumsum = series.cumsum() 
cumsum
plt.plot(cumsum,label="Suma acumulada",color='b')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Suma acumulada")
plt.legend(loc='best')
plt.grid()
plt.show()


"""Datos ruido_extra_100Hz"""
#Elegir la lista a evaluar  
a=sigs.ruido_extra_100Hz
plt.plot(a,label="Señal datos ruido_extra_100Hz",color='c')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal datos ruido_extra_100Hz")
plt.legend(loc='best')
plt.grid()
plt.show() 
series = pd.Series(a) 
cumsum = series.cumsum() 
cumsum
plt.plot(cumsum,label="Suma acumulada",color='m')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Suma acumulada")
plt.legend(loc='best')
plt.grid()
plt.show()

"""Datos ecg_100Hz"""
#Elegir la lista a evaluar  
a=sigs.ecg_100Hz
plt.plot(a,label="Señal datos ecg_100Hz",color='pink')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal datos ecg_100Hz")
plt.legend(loc='best')
plt.grid()
plt.show() 
series = pd.Series(a) 
cumsum = series.cumsum() 
cumsum
plt.plot(cumsum,label="Suma acumulada",color='b')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Suma acumulada")
plt.legend(loc='best')
plt.grid()
plt.show()


"""Datos airflow_calibrated_100Hz"""
#Elegir la lista a evaluar  
a=sigs.airflow_calibrated_100Hz
plt.plot(a,label="Señal datos airflow_calibrated_100Hz",color='brown')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal datos airflow_calibrated_100Hz")
plt.legend(loc='best')
plt.grid()
plt.show() 
series = pd.Series(a) 
cumsum = series.cumsum() 
cumsum
plt.plot(cumsum,label="Suma acumulada",color='r')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Suma acumulada")
plt.legend(loc='best')
plt.grid()
plt.show()


"""Datos airflow_100Hz"""
#Elegir la lista a evaluar  
a=sigs.airflow_100Hz
plt.plot(a,label="Señal datos airflow_100Hz",color='black')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal datos airflow_100Hz")
plt.legend(loc='best')
plt.grid()
plt.show() 
series = pd.Series(a) 
cumsum = series.cumsum() 
cumsum
plt.plot(cumsum,label="Suma acumulada",color='y')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Suma acumulada")
plt.legend(loc='best')
plt.grid()
plt.show()

"""DIEFERENCIA"""
import pandas as pd  
import signals as sigs
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft
import numpy as np
from matplotlib import style
import math
from scipy import signal
from scipy.ndimage import gaussian_filter  


"""Datos ruido_1KHz"""

a=sigs.ruido_1KHz
s=pd.Series(a)
b=s.diff()
plt.plot(b,label="Diferencia",color='y')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Diferencia")
plt.legend(loc='best')
plt.grid()
plt.show()


"""Datos ruido_100Hz"""
a=sigs.ruido_100Hz
s=pd.Series(a)
b=s.diff()
plt.plot(b,label="Diferencia",color='r')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Diferencia")
plt.legend(loc='best')
plt.grid()
plt.show()

"""Datos ruido_extra_100Hz"""
a=sigs.ruido_extra_100Hz
s=pd.Series(a)
b=s.diff()
plt.plot(b,label="Diferencia",color='b')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Diferencia")
plt.legend(loc='best')
plt.grid()
plt.show()


"""Datos ecg_100Hz"""
a=sigs.ecg_100Hz
s=pd.Series(a)
b=s.diff()
plt.plot(b,label="Diferencia",color='g')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Diferencia")
plt.legend(loc='best')
plt.grid()
plt.show()

"""Datos airflow_calibrated_100Hz"""
a=sigs.airflow_calibrated_100Hz
s=pd.Series(a)
b=s.diff()
plt.plot(b,label="Diferencia",color='c')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Diferencia")
plt.legend(loc='best')
plt.grid()
plt.show()

"""Datos airflow_100Hz"""
a=sigs.airflow_100Hz
s=pd.Series(a)
b=s.diff()
plt.plot(b,label="Diferencia",color='black')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Diferencia")
plt.legend(loc='best')
plt.grid()
plt.show()