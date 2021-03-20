import matplotlib.pyplot as plt
import math

tmin=0.0
tmax=80.0
dt=0.1
xk,xg,xr=1.0,1.0,1.0
vk,vg,vr=0.0,0.0,0.0

m=10.0

kk=0.4#rr>om 過減衰
rk=9.8
ak=kk/m
bk=rk/m

kg=9.8#rr<om 減衰振動
rg=4.0
ag=kg/m
bg=rg/m

kr=0.4#rr=om　臨界減衰
rr=4.0
ar=kr/m
br=rr/m

om=math.sqrt(ak)
rr=(1/2)*bk

print(rr)
print(om)

tlists=[]
kxlists=[]
gxlists=[]
rxlists=[]

def dxdt(v):
    return v

def dvdt(x,v,a,b):
    return -a*x-b*v

# def eulerx(x,v):
#     return x+dt*dxdt(v)

# def eulerv(x,v,a,b):
#     return v+dt*dvdt(x,v,a,b)

# def heunx(x,v,a,b):
#     k1=dxdt(v)
#     kv1=dvdt(x,v,a,b)
#     k2=dxdt(v+kv1*dt)
#     return x+0.5*(k1+k2)*dt

# def heunv(x,v,a,b):
#     k1=dvdt(x,v,a,b)
#     kx1=dxdt(v)
#     k2=dvdt(x+kx1*dt,v+k1*dt,a,b)
#     return v+0.5*(k1+k2)*dt 

def rungexv(x,v,a,b):
   k1=dxdt(v)
   kv1=dvdt(x,v,a,b)

   k2=dxdt(v+dt/2*kv1)
   kv2=dvdt(x+dt/2*k1,v+dt/2*kv1,a,b)

   k3=dxdt(v+dt/2*kv2)
   kv3=dvdt(x+dt/2*k2,v+dt/2*kv2,a,b)

   k4=dxdt(v+dt*kv3)
   kv4=dvdt(x+dt*k3,v+dt*kv3,a,b)
   return x+dt/6*(k1+2*k2+2*k3+k4),v+dt/6*(kv1+2*kv2+2*kv3+kv4)

# def rungev(x,v):
#     k1=dvdt(x,v)
#     kx1=dxdt(v)

#     k2=dvdt(x+kx1*dt/2,v+k1*dt/2)
#     kx2=dxdt(v+k1*dt/2)

#     k3=dvdt(x+kx2*dt/2,v+k2*dt/2)
#     kx3=dxdt(v+k2*dt/2)

#     k4=dvdt(x+kx3*dt,v+k3*dt/2)
#     return v+dt/6*(k1+2*k2+2*k3+k4)

while(tmin<=tmax):
    tlists.append(tmin)

#     eulerxlists.append(xe)#xeは初期値でしか求められない、dtだけ進まないと数値解を求められないから
#     tmpxe=eulerx(xe,ve)#xの値を一時保存
#     tmpve=eulerv(xe,ve)#vの値を一時保存

#     heunxlists.append(xh)
#     tmpxh=heunx(xh,vh)
#     tmpvh=heunv(xh,vh)

    kxlists.append(xk)
    gxlists.append(xg)
    rxlists.append(xr)

    tmpxk,tmpvk=rungexv(xk,vk,ak,bk)
    tmpxg,tmpvg=rungexv(xg,vg,ag,bg)
    tmpxr,tmpvr=rungexv(xr,vr,ar,br)

    tmin+=dt
    
    # xe=tmpxe
    # ve=tmpve

    # xh=tmpxh
    # vh=tmpvh

    xk=tmpxk
    vk=tmpvk

    xg=tmpxg
    vg=tmpvg

    xr=tmpxr
    vr=tmpvr
    
#print(heunxlists)
#print(rungexlists)

plt.plot(tlists, kxlists, marker="o", color = "red", linestyle = "--",label="kagensui")
plt.plot(tlists, gxlists, marker="o", color = "blue", linestyle = "--",label="gensuisindou")
plt.plot(tlists, rxlists, marker="o", color = "green", linestyle = "--",label="rinkaigensui")

plt.legend()
plt.show()