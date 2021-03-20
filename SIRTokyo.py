import random
import math
import numpy as np
import matplotlib.pyplot as plt
data=[5,13,34,12,28,20,26,14,13,12,18,22,25,24,47,48,27,16,41,35,39,34,29,31,55,48,54,57,60,58,54,67,107,124,131,111]
#5/30-7/5:0日目が5/30
ds=[0]*(len(data))
runge1=[]
dr=2*10**(-3)

tmin=0
tmax=len(data)-1
dt=0.01
nr=14000000#変更しない

a=3.5*0.07/nr
b=0.07
kr=1
n22=10000

def dsdt(sr,ir):
    return -a*sr*ir

def didt(sr,ir):
    return a*sr*ir-b*ir

def drdt(ir):
    return b*ir

def runge(s,i,r):#ルンゲクッタ法
    k1=dsdt(s,i)
    ki1=didt(s,i)
    kr1=drdt(i)

    k2=dsdt(s+k1*dt/2,i+ki1*dt/2)#k2から始める
    ki2=didt(s+k1*dt/2,i+ki1*dt/2)
    kr2=drdt(i+ki1*dt/2)

    k3=dsdt(s+k2*dt/2,i+ki2*dt/2)
    ki3=didt(s+k2*dt/2,i+ki2*dt/2)
    kr3=drdt(i+ki2*dt/2)

    k4=dsdt(s+k3*dt,i+ki3*dt)
    ki4=didt(s+k3*dt,i+ki3*dt)
    kr4=drdt(i+ki3*dt)
    return s+dt/6*(k1+2*k2+2*k3+k4),i+dt/6*(ki1+2*ki2+2*ki3+ki4),r+dt/6*(kr1+2*kr2+2*kr3+kr4)


ir=data[0]#病気にかかった人
sr=nr-ir#東京の人口から病気にかかった人を引く
rr=0#回復した人
Si1=sr
day=1

tmin=0

while(tmin<=tmax):
    tmpsr,tmpir,tmprr=runge(sr,ir,rr)

    tmin+=dt
    if(tmin>=day):
        ds[day]=Si1-tmpsr
        Si1=tmpsr
        day+=1

    sr=tmpsr
    ir=tmpir
    rr=nr-sr-ir

Rup=0
Rdown=0

for i in range(len(data)-1):#Rupは分子,Rdownは分母
    Rup+=(ds[i+1]-data[i+1])**2
    Rdown+=(data[i+1])**2+(ds[i+1])**2#dsの処理

R=Rup/Rdown#初期値としてRをだす

Rmin=R
amin=a
bmin=b
random.seed(1)

ds[0]=data[0]
for k in range(1000):
    r=random.random()
    dice=random.randint(1,2)#変更するのをaにするかbにするか決める

    if(dice==1):
        tmpa=a
        a=a+a*dr*(r-0.5)
    if(dice==2):
        tmpb=b
        b=b+b*dr*(r-0.5)

    ir=data[0]#病気にかかった人
    sr=nr-ir#まだ感染していない人
    rr=0#回復した人
    Si1=sr
    day=1

    tmin=0

    while(tmin<=tmax):
        tmpsr,tmpir,tmprr=runge(sr,ir,rr)

        tmin+=dt
        if(tmin>=day):#tminがdayを超えたらひとますsrを保存する
            ds[day]=Si1-tmpsr
            Si1=tmpsr
            day+=1

        sr=tmpsr
        ir=tmpir
        rr=nr-sr-ir

    Rup=0
    Rdown=0
    for i in range(len(data)-1):
        Rup+=(ds[i+1]-data[i+1])**2
        Rdown+=(data[i+1])**2+(ds[i+1])**2

    Rnext=Rup/Rdown

    dR=Rnext-R

    if(dR<=0):#パラメータ更新を確定
        R=Rnext
        if(Rnext<Rmin):#RminをRnextに更新
            Rmin=Rnext
            amin=a
            bmin=b
            kmin=k
    else:
        r=random.random()#0-1の乱数を再び生成
        if(math.exp(-dR/kr)):#パラメータ更新を確定
            R=Rnext
            if(Rnext<Rmin):           
                Rmin=Rnext
                amin=a
                bmin=b
                kmin=k
        else:#パラメータ更新を却下、もとのaの値かbの値に戻す
            if(dice==1):
                a=tmpa
            if(dice==2):
                b=tmpb
            
a=amin
b=bmin
ir=data[0]#病気にかかった人
sr=nr-ir#東京の人口 変更していく
rr=0#回復した人
Si1=sr
day=1

tmin=0

while(tmin<=tmax):#得られたaminとbminを使いもう一度計算
    tmpsr,tmpir,tmprr=runge(sr,ir,rr)

    tmin+=dt
    if(tmin>=day):
        ds[day]=Si1-tmpsr
        Si1=tmpsr
        day+=1

    sr=tmpsr
    ir=tmpir
    rr=nr-sr-ir

print(ds)
print(Rmin)
print(amin,bmin,kmin)

plt.plot(ds, marker="o", color = "green", linestyle = "--",label="Real data")#実データのグラフ
plt.plot(data, marker="o", color = "red", linestyle = "--",label="Prediction")#予測グラフ
#出てきたamin,bminを使ってSIRモデルを計算して、実データと共に描画

plt.legend()
plt.show()
