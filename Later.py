import matplotlib.pyplot as plt
import numpy as np
import math

tmin=0.0
tmax=10.0

dt=1.0
y=1.0

tlists=[]
ylists=[]
tylists=[]

# def f(t,y):
#     return y/t+t**3
# #微分方程式の形

# def g(t):
#     return t*((t**3)/3+2/3)

def f(y):
    return -25*y

def g(t):#解析解
    return math.exp(-25*t)
 #y0=1.0とする

tlists.append(tmin)
tylists.append(g(tmin))
ylists.append(y)

while(tmin<tmax):
    y=y/(1+25*dt)

    tmin+=dt

    tylists.append(g(tmin))
    ylists.append(y)
    tlists.append(tmin)

plt.plot(tlists, ylists, marker="o", color = "blue", linestyle = "--",label="direct")
plt.plot(tlists, tylists, marker="o", color = "red", linestyle = "--",label="truth")

plt.legend()
plt.show()