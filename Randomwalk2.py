import numpy as np
import matplotlib.pyplot as plt
import random

A=100
x=0
y=0
r=0
n=100
kr=10000

dicex=[]
dicey=[]
rn=[]
nx=[]
sum1=[0]*n
sum2=[0]*n
ave=[0]*n
ave1=[0]*n
ave2=[0]*n

#sum1.apend(0)

dicex.append(x)
dicey.append(y)

for k in range(kr):
    for i in range(n):
        dice=random.randint(1,5)
        if(-A<=x and y<=A):
            if(dice==1):
                x=x+1
            elif(dice==2):
                    x=x-1
            elif(dice==3):
                    y=y+1
            elif(dice==4):
                    y=y-1
            #dicex.append(x)
            #dicey.append(y)
            #r=x**2+y**2#最後範囲を超えたときに距離をとるかどうか
            sum1[i]=sum1[i]+x#sumは途中で終わった場合と最後まで繰り返した場合と分けないといけない
            sum2[i]=sum2[i]+y
    x=0
    y=0

for i in range(n):
    #ave[i]=sum1[i]/kr
    ave1[i]=sum1[i]/kr
    ave2[i]=sum2[i]/kr

#print(dicex)
#print(dicey)
#print(len(rn))

#print(len(nx))
#print(len(rn))

#plt.plot(dicex,dicey,marker="o", color = "blue", linestyle = "--")

plt.plot(ave1)
plt.show()