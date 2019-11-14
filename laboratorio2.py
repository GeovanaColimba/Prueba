# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:14:35 2019

@author: ASUS I5
"""

import numpy as np
import pylab as plt
# =============================================================================
# EJERCICIO 1
# =============================================================================
"""Generar la señal"""
#parametros de la señal x(t) = 2cos(60πt)
frecuencia=30 #Hz
tmin=-0.2
tmax=0.2
amplitud=2
t=np.linspace(tmin,tmax,500)
#definir la señal
x=amplitud*np.cos(2*np.pi*frecuencia*t)
#graficar la señal
plt.plot(t,x, label="2cos(60πt)",color='blue')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal continua x(t) = 2cos(60πt)")
plt.legend(loc='best')
plt.grid()
plt.show
"""muestreo de la señal"""
T=1/(2*frecuencia)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x1=amplitud*np.cos(2*np.pi*frecuencia*n*T)
plt.plot(n*T,x1,'r.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada")
plt.legend(loc='best')
plt.grid()
plt.show

"""muestree la señal a 2B"""
frecuencia=30 #Hz
tmin=-0.2
tmax=0.2
amplitud=2
t=np.linspace(tmin,tmax,400)
#definir la señal
x=amplitud*np.cos(2*np.pi*frecuencia*t)
#graficar la señal
plt.plot(t,x, label="2cos(60πt)",color='red')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal continua sinusoidal x1(t)")
plt.legend(loc='best')
plt.grid()
plt.show
"""muestreo de la señal"""
T=1/(4*frecuencia)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x2=amplitud*np.cos(2*np.pi*frecuencia*n*T)
plt.plot(n*T,x2,'b.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada a 2B")
plt.legend(loc='best')
plt.grid()
plt.show
"""muestree la señal a 4B"""
frecuencia=30 #Hz
tmin=-0.2
tmax=0.2
amplitud=2
t=np.linspace(tmin,tmax,400)
#definir la señal
x=amplitud*np.cos(2*np.pi*frecuencia*t)
#graficar la señal
plt.plot(t,x, label="2cos(60πt)",color='c')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal continua sinusoidal x1(t)")
plt.legend(loc='best')
plt.grid()
plt.show
"""muestreo de la señal"""
T=1/(8*frecuencia)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x3=amplitud*np.cos(2*np.pi*frecuencia*n*T)
plt.plot(n*T,x3,'b.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada a 4B")
plt.legend(loc='best')
plt.grid()
plt.show

"""muestree la señal a 6B"""
frecuencia=30 #Hz
tmin=-0.2
tmax=0.2
amplitud=2
t=np.linspace(tmin,tmax,400)
#definir la señal
x=amplitud*np.cos(2*np.pi*frecuencia*t)
#graficar la señal
plt.plot(t,x, label="2cos(60πt)",color='yellow')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal continua sinusoidal x1(t)")
plt.legend(loc='best')
plt.grid()
plt.show
"""muestreo de la señal"""
T=1/(12*frecuencia)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x3=amplitud*np.cos(2*np.pi*frecuencia*n*T)
plt.plot(n*T,x3,'g.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada a 6B")
plt.legend(loc='best')
plt.grid()
plt.show



# =============================================================================
# Ejercicio 2 x(t) = 2cos(60πt)+2cos(80πt)+2cos(90πt)
# =============================================================================

ft=720 #Hz
f1=30
f2=40
f3=45
tmin=-0.02
tmax=0.02
amplitud=2
t=np.linspace(tmin,tmax,400)
#definir la señal
x2b=amplitud*np.cos(2*np.pi*f1*t)+amplitud*np.cos(2*np.pi*f2*t)+amplitud*np.cos(2*np.pi*f3*t)
plt.plot(t,x2b,color="green")
T=1/(2*f3)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x22b=amplitud*np.cos(2*np.pi*f1*n*T)+amplitud*np.cos(2*np.pi*f2*n*T)+amplitud*np.cos(2*np.pi*f3*n*T)
plt.plot(n*T,x22b,'b.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada")
plt.legend(loc='best')
plt.grid()
plt.show

"""muestree la señal a 2B"""
ft=720 #Hz
f1=30
f2=40
f3=45
tmin=-0.02
tmax=0.02
amplitud=2
t=np.linspace(tmin,tmax,100)
#definir la señal
x2b=amplitud*np.cos(2*np.pi*f1*t)+amplitud*np.cos(2*np.pi*f2*t)+amplitud*np.cos(2*np.pi*f3*t)
plt.plot(t,x2b, color='c')
T=1/(4*f3)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x22b=amplitud*np.cos(2*np.pi*f1*n*T)+amplitud*np.cos(2*np.pi*f2*n*T)+amplitud*np.cos(2*np.pi*f3*n*T)
plt.plot(n*T,x22b,'m.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada a 2B")
plt.legend(loc='best')
plt.grid()
plt.show

"""muestree la señal a 4B"""
ft=720 #Hz
f1=30
f2=40
f3=45
tmin=-0.02
tmax=0.02
amplitud=2
t=np.linspace(tmin,tmax,100)
#definir la señal
x2b=amplitud*np.cos(2*np.pi*f1*t)+amplitud*np.cos(2*np.pi*f2*t)+amplitud*np.cos(2*np.pi*f3*t)
plt.plot(t,x2b)
T=1/(8*f3)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x22b=amplitud*np.cos(2*np.pi*f1*n*T)+amplitud*np.cos(2*np.pi*f2*n*T)+amplitud*np.cos(2*np.pi*f3*n*T)
plt.plot(n*T,x22b,'r.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada a 4B")
plt.legend(loc='best')
plt.grid()
plt.show
"""muestree la señal a 10B"""

ft=720 #Hz
f1=30
f2=40
f3=45
tmin=-0.02
tmax=0.02
amplitud=2
t=np.linspace(tmin,tmax,100)
#definir la señal
x2b=amplitud*np.cos(2*np.pi*f1*t)+amplitud*np.cos(2*np.pi*f2*t)+amplitud*np.cos(2*np.pi*f3*t)
plt.plot(t,x2b)
T=1/(20*f3)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x22b=amplitud*np.cos(2*np.pi*f1*n*T)+amplitud*np.cos(2*np.pi*f2*n*T)+amplitud*np.cos(2*np.pi*f3*n*T)
plt.plot(n*T,x22b,'r.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada a 10B")
plt.legend(loc='best')
plt.grid()
plt.show

# =============================================================================
# EJERICIO 3
# =============================================================================

f1=300
f2=400
f3=450
tmin=-0.02
tmax=0.02
amplitud=6
t=np.linspace(tmin,tmax,400)
#definir la señal
x2b=amplitud*np.cos(2*np.pi*f1*t)+amplitud*np.cos(2*np.pi*f2*t)+amplitud*np.cos(2*np.pi*f3*t)
#graficar la señal
plt.plot(t,x2b, color='yellow')
T=1/(2*f3)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x22b=amplitud*np.cos(2*np.pi*f1*n*T)+amplitud*np.cos(2*np.pi*f2*n*T)+amplitud*np.cos(2*np.pi*f3*n*T)
plt.plot(n*T,x22b,'c.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada ")
plt.legend(loc='best')
plt.grid()
plt.show

"""muestree la señal a 2B"""

f1=300
f2=400
f3=450
tmin=-0.02
tmax=0.02
amplitud=2
t=np.linspace(tmin,tmax,400)
#definir la señal
x2b=amplitud*np.cos(2*np.pi*f1*t)+amplitud*np.cos(2*np.pi*f2*t)+amplitud*np.cos(2*np.pi*f3*t)
#graficar la señal
plt.plot(t,x2b, color='r')
T=1/(4*f3)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x22b=amplitud*np.cos(2*np.pi*f1*n*T)+amplitud*np.cos(2*np.pi*f2*n*T)+amplitud*np.cos(2*np.pi*f3*n*T)
plt.plot(n*T,x22b,'b.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada a 2B")
plt.legend(loc='best')
plt.grid()
plt.show

"""muestree la señal a 4B"""

f1=300
f2=400
f3=450
tmin=-0.02
tmax=0.02
amplitud=2
t=np.linspace(tmin,tmax,400)
#definir la señal
x2b=amplitud*np.cos(2*np.pi*f1*t)+amplitud*np.cos(2*np.pi*f2*t)+amplitud*np.cos(2*np.pi*f3*t)
#graficar la señal
plt.plot(t,x2b, color='m')
T=1/(8*f3)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x22b=amplitud*np.cos(2*np.pi*f1*n*T)+amplitud*np.cos(2*np.pi*f2*n*T)+amplitud*np.cos(2*np.pi*f3*n*T)
plt.plot(n*T,x22b,'r.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada a 4B")
plt.legend(loc='best')
plt.grid()
plt.show
"""muestree la señal a 8B"""

f1=300
f2=400
f3=450
tmin=-0.02
tmax=0.02
amplitud=6
t=np.linspace(tmin,tmax,400)
#definir la señal
x2b=amplitud*np.cos(2*np.pi*f1*t)+amplitud*np.cos(2*np.pi*f2*t)+amplitud*np.cos(2*np.pi*f3*t)
#graficar la señal
plt.plot(t,x2b, color='green')
T=1/(16*f3)
nmin=np.ceil(tmin/T)     #aproximar al decimal mas bajo = ceil.
nmax=np.floor(tmax/T)    #aproximar al decimal mas ALTO = floor.
n=np.arange(nmin,nmax)
x22b=amplitud*np.cos(2*np.pi*f1*n*T)+amplitud*np.cos(2*np.pi*f2*n*T)+amplitud*np.cos(2*np.pi*f3*n*T)
plt.plot(n*T,x22b,'r.')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal x(t) muestreada a 8B")
plt.legend(loc='best')
plt.grid()
plt.show



