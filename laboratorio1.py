#-
 -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 06:19:59 2019

@author: ASUS I5
"""

import numpy as np 
import pylab as plt
# =============================================================================
                               #SEÑALES CONTINUAS
# =============================================================================
# =============================================================================
# señal x1=4*cos(t)
# =============================================================================
t1=np.arange(0,10,1/100)
amplitud1=4
frecuencia1=1/(2*np.pi)
x1=amplitud1*np.cos(2*np.pi*frecuencia1*t1)
plt.plot(x1,label="4cos(t)",color='blue')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal continua sinusoidal x1(t)")
plt.legend(loc='best')
plt.grid()
plt.show
# =============================================================================
# señal x2=4cos(6t)
# =============================================================================
t1=np.arange(-10,0.5,1/100)
amplitud2=4
frecuencia2=6/(2*np.pi)
x2=amplitud2*np.cos(2*np.pi*frecuencia2*t)
plt.plot(x2,label="4cos(6t)",color='red')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal continua sinusoidal x2(t)")
plt.legend(loc='best')
plt.grid()
plt.show
# =============================================================================
# señal x3=4cos(6t+pi)
# =============================================================================
fase3=(-np.pi)/6
amplitud3=4
frecuencia3=6/(2*np.pi)
x3=amplitud3*np.cos((2*np.pi*frecuencia3*t)+fase3)
plt.plot(x3,label="x3=4cos(6t+pi)", color='yellow')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal continua sinusoidal x3(t)")
plt.legend(loc='best')
plt.grid()
plt.show
# =============================================================================
# señal x4=4cos(6t)+3sin(5t+2*pi/3)
# =============================================================================
amplitud4=4
frecuencia4=6/(2*np.pi)
x4=amplitud4*np.cos(2*np.pi*frecuencia4*t)
#fase5=(-2*np.pi)/15
fase5=(2*np.pi)/3
amplitud5=3
frecuencia5=5/(2*np.pi)
x5=amplitud5*np.sin((2*np.pi*frecuencia5*t)+fase5)
xt=x4+x5
plt.plot(xt,label="x4=4cos(6t)+3sin(5t+2*pi/3)", color='green')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Señal sinusoidal continua x4(t)")
plt.legend(loc='best')
plt.grid()
plt.show
# =============================================================================
                              #SEÑALES DISCRETAS
# =============================================================================
# ============================================================================= 
# señal x1=2sin(n), n=100
# =============================================================================
ampli=2
frecu=1/(2*np.pi)
n1=np.linspace(0,19*np.pi*frecu,100)
x5=ampli*np.sin(n1)
plt.stem(n1,x5,'c',label="x1=2sin(n),n=100",use_line_collection=True)
plt.title("Señal sinusoidal discreta x1(n)")
plt.legend(loc='best')
plt.grid()
plt.show()
# =============================================================================
# señal x1=2sin(4n+pi), n=100
# =============================================================================
ampli=2
frecu=4/(2*np.pi)
n2=np.linspace(0,10*np.pi*frecu,100)
x6=ampli*np.sin(n2+np.pi) #generar señal 
plt.stem(n2,x6,'r',label="x1=2sin(4n+pi), n=100",use_line_collection=True)
plt.xlabel("Y")
plt.ylabel("X")
plt.title("Señal sinusoidal discreta x2(n)")
plt.legend(loc='best')
plt.grid()
plt.show()

# =============================================================================
# Varie la frecuencia de x3(t) a un numero mayor y 
#compruebe graﬁcamente el postulado A2
# =============================================================================
t12=np.arange(0,6,1/100)
ampli31=4
frecuencia31=2
x2=ampli31*np.cos(2*np.pi*frecuencia31*t12)
plt.plot(x2,label="frecuencia mayor",color='c')
plt.xlabel("Y")
plt.ylabel("X")
plt.title("Señal x3(t) frecuencia mayor")
plt.legend(loc='best')
plt.grid()
plt.show

t1=np.arange(0,4,1/100)
amplitud2=4
frecuencia2=6/(2*np.pi)
x2=amplitud2*np.cos(2*np.pi*frecuencia2*t1)
plt.plot(x2,label="frecuencia mayor",color='brown')
plt.xlabel("Y")
plt.ylabel("X")
ampli31=4
frecuencia31=2
x2=ampli31*np.cos(2*np.pi*frecuencia31*t1)
plt.plot(x2,label="frecuencia normal",color='green')
plt.title("Señal x3(t) frecuencia mayor y frecuencia calculada")
plt.legend(loc='best')
plt.grid()
plt.show
# =============================================================================
# Demuestre graﬁcamente el postulado A3
# =============================================================================
# señal x2(t)=5cos(6t)
ts=np.arange(0,1,1/50)
amplits=5
fre1=2
fre2=0
fre3=5
x21=amplits*np.cos(2*np.pi*fre1*ts)
x22=amplits*np.cos(2*np.pi*fre2*ts)
x23=amplits*np.cos(2*np.pi*fre3*ts)
plt.plot(x21,label="5cos(8t)",color='blue')
plt.plot(x22,label="5cos(8t)",color='red')
plt.plot(x3,label="5cos(8t)",color='green')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Demostración postulado A3")
plt.legend(loc='best')
plt.grid()
plt.show

# =============================================================================
# Compruebe graﬁcamente el postulado B2.
# =============================================================================
#señal 1  x(1)=5cos(8n)
amplitudb2=5
frecuenciab2=4/(np.pi)
nb2=np.linspace(0,2*np.pi*frecuenciab2,70)
b2=amplitudb2*np.cos(nb2)
plt.stem(nb2,b2,'c',use_line_collection=True, label='Señal en fase')
frecuenciab22=(8+2*np.pi)/(2*np.pi)
nb22=np.linspace(0,1.1*np.pi*frecuenciab22,50)
b22=amplitudb2*np.cos(nb22)
plt.stem(nb22,b22,'y',use_line_collection=True, label='Señal en desfase')
plt.xlabel("Tiempo")
plt.ylabel("Voltios")
plt.title("Demostración postulado B2")
plt.legend(loc='best')
plt.grid()
plt.show

# =============================================================================
# Compruebe graﬁcamente el postulado B3. 
# =============================================================================
# primera señal= x(n)=5cos(6n)
frecuenciab3=4
amplitudb3=5
nb3=np.linspace(0,1*np.pi*frecuenciab3,50)
b3=amplitudb3*np.cos(nb3)
plt.stem(nb3,b3,use_line_collection=True, label='Señal 1 con frecuencia<5')
#segunda señal = x(n)=9sen(4n)
frecuenciab31=2
amplitudb31=9
nb31=np.linspace(0,1*np.pi*frecuenciab31,50)
b31=amplitudb31*np.sin(nb31)
plt.stem(nb31,b31,'g',use_line_collection=True, label='Señal 2 con frecuencia<5')
#tercera señal = x(n)=8cos(n)
frecuenciab32=5
amplitudb32=8
nb32=np.linspace(0,1*np.pi*frecuenciab32,50)
b32=amplitudb32*np.cos(nb32)
plt.stem(nb32,b32,'r',use_line_collection=True, label='Señal 3 con frecuencia=5')
#cuarta señal = x(n)=6sin(n)
frecuenciab33=8
amplitudb33=6
nb33=np.linspace(0,1*np.pi*frecuenciab33,50)
b33=amplitudb32*np.sin(nb33)
plt.stem(nb33,b33,'b',use_line_collection=True, label='Señal 4 con frecuencia 5<f<10')
# quinta señal = x(n)=3cos(7n)
frecuenciab34=8
amplitudb34=6
nb34=np.linspace(0,1*np.pi*frecuenciab34,50)
b34=amplitudb32*np.cos(nb34)
plt.stem(nb34,b34,'y',use_line_collection=True, label='Señal 5 con frecuencia 5<f<10')
plt.grid()
plt.show
plt.xlabel("Y")
plt.ylabel("X")
plt.title("Demostración postulado B3")
plt.legend(loc='best')
plt.show()

frecuenciab2=1/(2*np.pi)
amplitudb2=5
nb2=np.linspace(0.1*np.pi*frecuenciab2,50)
b2=amplitudb2*np.sin(nb2)
plt.stem(nb2,b2,use_line_collection=True,label='en fase')
plt.legend()
plt.show()

frecuencia22=2*np.pi/(2*np.pi)
amplitudb22=5
nb22=np.arange(0.1*np.pi*frecuencia22,50)
b22=amplitudb22*np.sin(nb22)
plt.stem(nb22,b22,use_line_collection=True,label='en desfase')
plt.legend()

f8=1/2
A8=6
n8=np.linspace(0.1*np.pi*f8,50)
x8=A8*np.cos(np.pi*n8)
plt.stem(n8,use_line_collection=True)
plt.grid()
plt.show
plt.xlabel("Y")
plt.ylabel("X")
plt.title("Demostración postulado B2")
plt.legend(loc='best')
plt.show()


