import matplotlib.pyplot as plt
import numpy as np

tmin=5
tmax=6.5

dt=0.01
y=1.0

tlists=[]
ylists=[]

def f(t,y):
    return y/t+t**3

def g(t):
    return t*((t**3)/3-(622/15))

while(tmin<=tmax):
    y=y+dt*f(tmin,y)

    tmin+=dt
    ylists.append(abs(y-g(tmin)))
    tlists.append(tmin)

plt.plot(tlists, ylists, marker="o", color = "blue", linestyle = "--")

plt.show()