import matplotlib.pyplot as plt
import numpy as np

tmin=5
tmax=6.5

dt=0.01
y=1.0

tlists=[]
heunylists=[]

def f(t,y):
    return y/t+t**3

def g(t):
    return t*((t**3)/3-(622/15))

while(tmin<=tmax):
    k1=f(tmin,y)
    tmin+=dt
    k2=f(tmin,y+k1*dt)

    y=y+0.5*(k1+k2)*dt

    heunylists.append(abs(y-g(tmin)))
    tlists.append(tmin)

plt.plot(tlists,heunylists, marker="o", color = "blue", linestyle = "--")

plt.show()