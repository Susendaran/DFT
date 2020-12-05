# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 01:36:39 2020

@author: susen
"""
import math as m
from matplotlib import pyplot as plt
import numpy as np

def func(t):
    if (t<0):
        f=-1
    else:
        f=1
    return f
n=500
dt=1/n
x_t=np.zeros((n,1),dtype=float)
y_t=np.zeros((n,1),dtype=complex)
x_f=np.zeros((n,1),dtype=float)
y_f=np.zeros((n,1),dtype=complex)
mag=np.zeros((n,1),dtype=float)
phase=np.zeros((n,1),dtype=float)
dft=np.ones((n,n),dtype=complex)

a=-0.5
for i in range(0,n):
    x_t[i][0]=a
    y_t[i][0]=func(x_t[i][0])
    if(i<n/2):
        x_f[i][0]=i
    a+=dt
    
#print(x_t)
#print(y_t)
#print(x_f)

    
j=complex('j')
omega=pow(m.e,((-2*m.pi*j)/n))


for i in range(1,n):
    for j in range(1,n):
        om=pow(omega,i*j)
        dft[i][j]=om


y_f=dft.dot(y_t)
for i in range(0,int(n/2)):
    mag[i][0]=(abs(y_f[i][0]))/(n/2)
    p=(y_f[i][0].imag)/(y_f[i][0].real)
    phase[i][0]=m.atan(p)


plt.plot(x_t,y_t)
plt.show()
plt.plot(x_f,mag)
plt.show()


