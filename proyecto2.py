# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 13:24:26 2019

@author: ASUS I5
"""

from tkinter import * # el asterisco significa importar todas las clases. tkinder es para interfaces graficas 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def grafica():
    num1=float(ampl.get())
    num2=float(frec.get())
    num3=float(fase.get())
    m=float(muestra.get())
    tmin=-0.5
    tmax=0.5
    t=np.linspace(tmin,tmax,400)
    x=num1*np.cos(2*np.pi*num2*t)+num3
    nmin=np.ceil(tmin/(1/(m*num2)))     #aproximar al decimal mas bajo = ceil.
    nmax=np.floor(tmax/(1/(m*num2))) 
    n=np.arange(nmin,nmax)
    x1=num1*np.cos(2*np.pi*num2*n*(1/(m*num2))+num3)
    f=Figure(figsize=(4.7,4.7),dpi=80)
    img=f.add_subplot(211)
    img1=f.add_subplot(212)
    img.plot(x,'r')
    img1.plot(n*(1/(m*num2)),x1,'m.')
    canvas=FigureCanvasTkAgg(f,frame)
    canvas.draw() #grafico el cambas
    canvas.get_tk_widget().place(x=60,y=280)
    #l.set(float(ampl.get())*np.cos((2*np.pi*float(frec.get())*t)+float(fase.get())))
    # h.set("l")
    h.set((num1,"cos(2pi",num2,"t)+",num3))
    ampl.set("")
    frec.set("")
    fase.set("")
    
def graficacompleja():
    
    frec1=int(frec11.get())
    frec2=int(frec22.get())
    frec3=int(frec33.get())
    
    menor=min(frec1,frec2,frec3)
    for i in range(1,menor):
        if(frec1%i==0 and frec2%i==0 and frec3%i==0  ):
            mcd=i
            mcm=((frec1*frec2*frec3)/mcd)
            
    ampl1=int(ampl11.get())
    ampl2=int(ampl22.get())
    ampl3=int(ampl33.get())
    
    fase1=float(fase11.get())
    fase2=float(fase22.get())
    fase3=float(fase33.get())
    m1=float(muestra1.get())
    
    sumaf=fase1+fase2+fase3
    
    suma=ampl1+ampl2+ampl3
    
    tmini=-1
    tmaxi=1
    t=np.linspace(tmini,tmaxi,400)
    xc=(suma*np.cos(2*np.pi*frec1*t)+sumaf)+(suma*np.cos(2*np.pi*frec2*t)+sumaf)+(suma*np.cos(2*np.pi*frec3*t)+sumaf)
    nmin=np.ceil(tmini/(1/(m1*mcm)))     #aproximar al decimal mas bajo = ceil.
    nmax=np.floor(tmaxi/(1/(m1*mcm))) 
    n=np.arange(nmin,nmax)
    xc1=suma*np.cos(2*np.pi*frec1*n*(1/(m1*mcm)))+suma*np.cos(2*np.pi*frec2*n*(1/(m1*mcm)))+suma*np.cos(2*np.pi*frec3*n*(1/(m1*mcm)))
    f=Figure(figsize=(4.7,4.7),dpi=80)
    img=f.add_subplot(211)
    img1=f.add_subplot(212)
    img.plot(xc)
    img1.plot(n*(1/(m1*mcm)),xc1,'m.')
    canvas=FigureCanvasTkAgg(f,frame)
    canvas.draw() #grafico el cambas
    canvas.get_tk_widget().place(x=610,y=280)
    #l.set(float(ampl.get())*np.cos((2*np.pi*float(frec.get())*t)+float(fase.get())))
    # h.set("l")
    j.set((ampl1,"cos(2pi",frec1,"t)+",ampl2,"cos(2pi",frec2,"t)+",ampl3,"cos(2pi",frec3,"t"))
    ampl.set("")
    frec.set("")
    fase.set("")

    
#set enviar datos #get traer datos
root=Tk() #es una raiz 
#interfaz
root.title("Generación de señales continuas y muestreadas")
frec= StringVar()
fase=StringVar()
ampl=StringVar()
h=StringVar()
l=StringVar()
num1=StringVar()
num2=StringVar()
num3=StringVar()
frec1=StringVar()
frec2=StringVar()
frec3=StringVar()
tmin=float()
tmax=float()
tmini=float()
tmaxi=float()
ampl1=StringVar()
ampl2=StringVar()
ampl3=StringVar()
fase11=StringVar()
fase22=StringVar()
fase33=StringVar()
muestra=StringVar()
m=StringVar()
muestra1=StringVar()
m1=StringVar()
fase1=StringVar()
fase2=StringVar()
fase2=StringVar()
frec11=StringVar()
frec22=StringVar()
frec33=StringVar()
ampl11=StringVar()
ampl22=StringVar()
mcm=int()
j=StringVar()
ampl33=StringVar()
T=StringVar()
nmin=StringVar()
nmax=StringVar()
n=float()
suma=float()
#x=StringVar()
#limitar el espacio de la interfaz
root.resizable(0,0)
root.geometry("1130x700")

frame=Frame(root,bg="black",width=1130, height=700)
frame.pack(fill='both', expand=1)
frame.config(relief="sunken")
frame.config(cursor="pirate")
root.config(cursor="arrow")
root.config(bg="white")
root.config(bd=15)
root.config(relief="ridge")
frame.pack()

labelt=Label(frame,text=" UNIVERSIDAD TÉCNICA DEL NORTE  ",font=("Arial Black",25),fg="Salmon",bg="black",width=33, height=1).place(x=190, y=1)
labelU=Label(frame,text=" PROCESAMIENTO DIGITAL DE SEÑALES  ",font=("Arial Black",15),fg="white",bg="black",width=33, height=1).place(x=330, y=52)

label2=Label(frame,text=" Amplitud  ",font=("Arial Black",10),fg="black",width=11, height=1).place(x=40, y=150)

amplitud1=Entry(frame,textvariable=ampl,font=("Arial Black",10),width=8).place(x=150, y=150)


label1=Label(frame,text=" Frecuencia",font=("Arial Black",10),fg="black",width=11, height=1).place(x=40, y=180)
frecuencia1=Entry(frame,textvariable=frec,font=("Arial Black",10),width=8).place(x=150, y=180)

label3=Label(frame,text="   Fase   ",font=("Arial Black",10),fg="black",width=11, height=1).place(x=40, y=210)
fase3=Entry(frame,textvariable=fase,font=("Arial Black",10),width=8).place(x=150, y=210)

label4=Label(frame,text="  Señal   ",font=("Arial Black",10),fg="black",width=11, height=1).place(x=40, y=240)
resultado1=Entry(frame,textvariable=h,font=("Arial Black",10),width=32).place(x=150, y=240)

boton1=Button(frame,text="GRAFICAR Y MUESTREAR",font=("Arial Black",8),bg="light blue",fg="BLUE",command=grafica).place(x=250, y=210)

label5=Label(frame,text="  SEÑALES COMPLEJAS  ",font=("Arial Black",13),fg="Salmon",bg="black",width=25, height=1).place(x=480, y=110)
labelcontinua=Label(frame,text="  SEÑALES CONTINUAS  ",font=("Arial Black",13),fg="Salmon",bg="black",width=25, height=1).place(x=115, y=110)

label5=Label(frame,text="  Frecuencia 1  ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=530, y=150)
frecuencia2=Entry(frame,textvariable=frec11,font=("Arial Black",10),width=5).place(x=648, y=150)

label6=Label(frame,text="  Frecuencia 2  ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=530, y=180)
frecuencia3=Entry(frame,textvariable=frec22,font=("Arial Black",10),width=5).place(x=648, y=180)

label7=Label(frame,text="  Frecuencia 3 ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=530, y=210)
frecuencia4=Entry(frame,textvariable=frec33,font=("Arial Black",10),width=5).place(x=648, y=210)

label5=Label(frame,text="  Amplitud 1  ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=710, y=150)
frecuencia2=Entry(frame,textvariable=ampl11,font=("Arial Black",10),width=5).place(x=828, y=150)

label6=Label(frame,text="  Amplitud 2  ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=710, y=180)
frecuencia3=Entry(frame,textvariable=ampl22,font=("Arial Black",10),width=5).place(x=828, y=180)

label7=Label(frame,text="  Amplitud 3 ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=710, y=210)
frecuencia4=Entry(frame,textvariable=ampl33,font=("Arial Black",10),width=5).place(x=828, y=210)


label9=Label(frame,text="  Fase 1  ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=890, y=150)
frecuencia2=Entry(frame,textvariable=fase11,font=("Arial Black",10),width=5).place(x=1008, y=150)

label10=Label(frame,text="  Fase 2  ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=890, y=180)
frecuencia3=Entry(frame,textvariable=fase22,font=("Arial Black",10),width=5).place(x=1008, y=180)

label11=Label(frame,text="  Fase 3 ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=890, y=210)
frecuencia4=Entry(frame,textvariable=fase33,font=("Arial Black",10),width=5).place(x=1008, y=210)

label8=Label(frame,text="  Señal   ",font=("Arial Black",10),fg="black",width=12, height=1).place(x=530, y=240)
resultado1=Entry(frame,textvariable=j,font=("Arial Black",10),width=25).place(x=648, y=240)

label9=Label(frame,text="  Muestreo ",font=("Arial Black",10),fg="black",width=8, height=1).place(x=250, y=150)
resultado9=Entry(frame,textvariable=muestra,font=("Arial Black",10),width=5).place(x=335, y=150)

label10=Label(frame,text="  Muestreo ",font=("Arial Black",10),fg="black",width=8, height=1).place(x=780, y=113)
resultado10=Entry(frame,textvariable=muestra1,font=("Arial Black",10),width=5).place(x=860, y=113)

boton1=Button(frame,text="GRAFICAR Y MUESTREAR",font=("Arial Black",8),bg="light blue",fg="BLUE",command=graficacompleja).place(x=890, y=240)

imagenL=PhotoImage(file="captura.gif")
labelimagen=Label(frame,image=imagenL,width=111, height=111).place(x=37,y=15)


root.mainloop()   #ciclo de funcionamiento ce la interfaz 