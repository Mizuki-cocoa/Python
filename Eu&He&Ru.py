import matplotlib.pyplot as plt
import numpy as np

tmin=1.0
tmax=4.0

dt=0.01
ye,yh,yr=1.0,1.0,1.0

tlists=[]
eulerylists=[]
heunyylists=[]
rungeylists=[]

ax=plt.gca()
ax.set_yscale('log')

def f(t,y):
    return y/t+t**3
#微分方程式の形

def d(t):
    return t*((t**3)/3+2/3)
#解析解

def euler(ye,dt,tmin):
    return ye+dt*f(tmin,ye)

def heun(yh,dt,tmin):
    k1=f(tmin,yh)
    k2=f(tmin+dt,yh+k1*dt)
    return yh+0.5*(k1+k2)*dt

def runge(yr,dt,tmin):
    k1=f(tmin,yr)
    k2=f(tmin+dt/2,yr+dt/2*k1)
    k3=f(tmin+dt/2,yr+dt/2*k2)
    k4=f(tmin+dt,yr+dt*k3)
    return yr+dt/6*(k1+2*k2+2*k3+k4)

while(tmin<=tmax):
    ye=euler(ye,dt,tmin)
    yh=heun(yh,dt,tmin)
    yr=runge(yr,dt,tmin)

    tmin+=dt
    tlists.append(tmin)

    eulerylists.append(abs(ye-d(tmin)))#誤差を加える
    rungeylists.append(abs(yr-d(tmin)))
    heunyylists.append(abs(yh-d(tmin)))

plt.plot(tlists, eulerylists, marker="o", color = "red", linestyle = "--",label="euler")
plt.plot(tlists, heunyylists, marker="*", color = "blue", linestyle = "--",label="heun")
plt.plot(tlists,rungeylists, marker="+", color = "green", linestyle = "--",label="runge")

plt.legend()
plt.show()