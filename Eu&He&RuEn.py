import matplotlib.pyplot as plt
import numpy as np
import math

tmin=0.0
tmax=6.0

om=1.0
dt=0.1
r=1.0
x1,xe,xh,xr=r,r,r,r
y1,ye,yh,yr=0.0,0.0,0.0,0.0

tlists=[]

xlists=[]
eulerxlists=[]
heunyxlists=[]
rungexlists=[]

ylists=[]
eulerylists=[]
heunyylists=[]
rungeylists=[]

#ax=plt.gca()
#ax.set_yscale('log')

#定数は関数に入れない

def xk(t):
    return r*math.cos(om*t)

def yk(t):
    return r*math.sin(om*t)

def dxdt(y):
    return -om*y

def dydt(x):
    return (om)*x

def eulerx(x,y):
    return x+dt*dxdt(y)

def eulery(x,y):
    return y+dt*dydt(x)

def heunx(x,y):
    k1=dxdt(y)
    ky=dydt(x)
    k2=dxdt(y+ky*dt)
    return x+0.5*(k1+k2)*dt

def heuny(x,y):
    k1=dydt(x)
    kx=dxdt(y)
    k2=dydt(x+kx*dt)
    return y+0.5*(k1+k2)*dt

def rungex(x,y):
    k1=dxdt(y)
    ky1=dydt(x)
    k2=dxdt(y+ky1*dt/2)

    ky2=dydt(x+k1*dt/2)
    k3=dxdt(y+ky2*dt/2)

    ky3=dydt(x+k2*dt/2)
    k4=dxdt(y+ky3*dt)
    return x+dt/6*(k1+2*k2+2*k3+k4)

def rungey(x,y):
    k1=dydt(x)
    kx1=dxdt(y)

    k2=dydt(x+kx1*dt/2)
    kx2=dxdt(y+k1*dt/2)

    k3=dydt(x+kx2*dt/2)
    kx3=dxdt(y+k2*dt/2)

    k4=dydt(x+kx3*dt)
    return y+dt/6*(k1+2*k2+2*k3+k4)

while(tmin<=tmax):
    x1=xk(tmin)#tminでの解析解
    xlists.append(x1)
    y1=yk(tmin)
    ylists.append(y1)

    eulerxlists.append(xe)#xeは初期値でしか求められない、dtだけ進まないと数値解を求められないから
    tmpx=eulerx(xe,ye)#xの値を一時保存
    eulerylists.append(ye)
    tmpy=eulery(xe,ye)#yの値を一時保存

    heunyxlists.append(xh)
    tmpxh=heunx(xh,yh)
    heunyylists.append(yh)
    tmpyh=heuny(xh,yh)

    rungexlists.append(xr)
    tmpxr=rungex(xr,yr)
    rungeylists.append(yr)
    tmpyr=rungey(xr,yr)

    #xe=eulerx()にするとtmin+dtだけ進んだ値が入ってしまう
    #その後のyeを求める際にyeはtminでの値なのにxeはtmin+dtの値なので誤差が生じてしまう

    #tmpで一時保存をしてdtだけ足したあとにxe,yeに代入していく

    tmin+=dt

    xe=tmpx
    ye=tmpy

    xh=tmpxh
    yh=tmpyh

    xr=tmpxr
    yr=tmpyr

    #tlists.append(tmin)
    
    #eulerxlists.append(abs(xe-x1))
    #heunyxlists.append(abs(xh-x1))
    #rungexlists.append(abs(xr-x1))

    #eulerylists.append(abs(ye-y1))
    #heunyylists.append(abs(yh-y1))
    #rungeylists.append(abs(yr-y1))


#print(heunyxlists)
print(xlists)
print(rungexlists)
plt.plot(xlists, ylists, marker="o", color = "black", linestyle = "--",label="normal")
#plt.plot(eulerxlists, eulerylists, marker="o", color = "red", linestyle = "--",label="euler")
plt.plot(heunyxlists, heunyylists, marker="*", color = "green", linestyle = "--",label="heun")
plt.plot(rungexlists, rungeylists, marker="+", color = "blue", linestyle = "--",label="runge")

#plt.plot(tlists, eulerxlists, marker="o", color = "red", linestyle = "--",label="euler")
#plt.plot(tlists, heunyxlists, marker="*", color = "green", linestyle = "--",label="heun")
#plt.plot(tlists, rungexlists, marker="+", color = "blue", linestyle = "--",label="runge")

plt.legend()
plt.show()


#誤差を求めるなら距離で出せ