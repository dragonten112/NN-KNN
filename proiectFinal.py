from tkinter import *
from tkinter import messagebox
import math 
from sympy import *
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import numpy as np
import cv2



root = Tk()

root.title("Aproximarea si Interpolarea unui polinom")
root.geometry("300x200")
root.resizable(False,False)




lValori= Label(root,text="Introdu valori:")
lFunctie=Label(root,text="Functie (f= ):")
lA=Label(root,text="a :")
lB=Label(root,text="b :")
lIter=Label(root,text="Numar iteratii:")
lMetoda = Label(root,text="Alege o Metoda:")


def erori_bern():
    try:
        bernstein()
    except ValueError:
        popupAB()

def erori_lagrange():
    try:
        lagrange()
    except ValueError:
        popupAB()


def popupFunctie():
    
    response=messagebox.showerror("Eroare","Functia este incorecta!")
    Label(root,text=response)
    
def popupAB():
    response=messagebox.showerror("Eroare","(a) trebuie sa fie mai  mic decat (b)!")
    Label(root,text=response)
    
def popupIter():
    response=messagebox.showerror("Eroare","Valoare introdusa la iteratii nu este integer")
    Label(root,text=response)

def bernstein():
    # Bernstein pe [a,b]
   
    
    metadata = dict(title = 'Bernstein02', artisti = 'Matplotlib',
                    comment = 'Bernstein Approximation Polynomials on [a,b]')
    Writer = writers['ffmpeg']
    writer = Writer(fps = 1, metadata=metadata)
    fig = plt.figure()
    
    fs=eFunc.get()

    x = Symbol('x')
    f = lambdify(x, fs)
    

    a=int(eA.get())
    b=int(eB.get())
    if(a>=b):
        raise ValueError
    x_val = np.linspace(a,b,100)
    t = (x_val - a) / (b - a)

    ax = plt.axes()
    
    try:
        ax.scatter(x_val, f(x_val))
    except NameError:
        popupFunctie()
    
    try:
        nmax =int(eIter.get())
    except ValueError:
        popupIter()
      

    def bern_frame(n):
        bern = np.zeros_like(x_val)
        for k in range(n + 1):
            bern += f(k/n * (b-a) + a)*math.comb(n,k)*t**k*(1-t)**(n-k)
        ax.plot(x_val, bern)
        plt.title('Degree ' + str(n))
        
    anim = FuncAnimation(fig, func = bern_frame, interval = 10, frames = np.arange(1,nmax+1))
    anim.save('Bernstein02.mp4', writer)
    

    cap=cv2.VideoCapture('Bernstein02.mp4')
    
    if(cap.isOpened()==False):
        response=messagebox.showerror("Eroare","Videoclip indisponibil")
        Label(root,text=response)
    while(cap.isOpened()):
        ret, frame= cap.read()
        
        if ret ==  True:
            cv2.imshow('Frame', frame)
            
            if cv2.waitKey(1000) & 0xFF == ord(' '):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


def lagrange():
    metadata = dict(title = 'Lagrange', artisti = 'Matplotlib',
                    comment = 'Lagrange Approximation Polynomials on [a,b]')
    Writer = writers['ffmpeg']
    writer = Writer(fps = 1, metadata=metadata)
    fig = plt.figure()

    fs=eFunc.get()
    x = Symbol('x')
    
    f = lambdify(x, fs)
  
    
    
    a=int(eA.get())
    b=int(eB.get())
    if(a>=b):
        raise ValueError
    
    
    x_val = np.linspace(a,b,100)
    t = (x_val - a) / (b - a)

    ax = plt.axes()
    try:
        ax.scatter(x_val, f(x_val))
    except NameError:
        popupFunctie()

    try:
        nmax =int(eIter.get())
    except ValueError:
        popupIter()



    def lagrange_frame(n):
        xi = np.linspace(a,b,n+1)
        ax.scatter(xi, f(xi))
        l = np.zeros_like(x_val)
        for j in range(1,n+1):
            prod = 1
            for i in range(1, n+1):
                if i!=j:
                    prod*=(x_val - xi[i])/(xi[j] - xi[i])
            l+=f(xi[j])*prod
        ax.plot(x_val,l)
        plt.title('Degree ' + str(n))
            
    anim = FuncAnimation(fig, func = lagrange_frame, interval = 10, frames = np.arange(1,nmax+1))
    anim.save('Lagrange.mp4', writer)
    
    
    cap=cv2.VideoCapture('Lagrange.mp4')
    
    if(cap.isOpened()==False):
        response=messagebox.showerror("Eroare","Videoclip indisponibil")
        Label(root,text=response)
    while(cap.isOpened()):
        ret, frame= cap.read()
        
        if ret ==  True:
            cv2.imshow('Frame', frame)
            
            if cv2.waitKey(1000) & 0xFF == ord(' '):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()



buttonAprox=Button(root, text="Aproximare",command=erori_bern)
buttonInterpolare=Button(root,text="Interpolare",command=erori_lagrange)
eFunc=Entry(root)
eA=Entry(root,width=10)
eB=Entry(root,width=10)
eIter=Entry(root,width=20)


lMetoda.place(relx=0.3,rely=0.75)
lValori.place(relx=0.3,rely=0)
lFunctie.place(relx=0.1,rely=0.15)
lA.place(relx=0.1,rely=0.30)
lB.place(relx=0.5,rely=0.30)
lIter.place(relx=0.1,rely=0.45)



eFunc.place(relx=0.4,rely=0.15)
eA.place(relx=0.2,rely=0.30)
eB.place(relx=0.6,rely=0.30)
eIter.place(relx=0.40,rely=0.45)

buttonAprox.place(relx=0.2,rely=0.85)
buttonInterpolare.place(relx=0.5,rely=0.85)
root.mainloop()


