import matplotlib.pyplot as plt
import numpy as np
import math

tmin=0.0
tmax=1.0

dt=0.1
y0=1.0
n=20
eps=0.01

h=(tmax-tmin)/n

t=tmin
y=y0

tlists=[]
ylists=[]
tylists=[]

def f(y):
    return -25*y

def df(y):
    return -25

def g(t):#解析解
    return math.exp(-25*t)
#y0=1.0とする

tlists.append(t)
tylists.append(g(t))
ylists.append(y)

while(t<tmax):
    yk = y
    g1 = yk-dt*f(yk)-y
    gf = 1-dt*df(yk)
    yk = yk-g1/gf
    y = yk
    t = t+dt

    tylists.append(g(t))
    ylists.append(y)
    tlists.append(t)
    if(math.fabs(g/gf) < eps or math.fabs(g1) < eps):
        break

print(ylists)

plt.plot(tlists, ylists, marker="*", color = "blue", linestyle = "--",label="direct")
plt.plot(tlists, tylists, marker="o", color = "red", linestyle = "--",label="truth")

plt.legend()
plt.show()