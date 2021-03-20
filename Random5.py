import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

A=10
x=0
y=0
r=0
n=100
kr=10000

fig= plt.figure()
artists=[]

sum1=np.zeros((10,kr))
sum2=np.zeros((10,kr))

for k in range(kr):
    for i in range(n):
        dice=random.randint(1,5)
        if(-A<=x and y<=A and x<=A and -A<=y):
            if(dice==1):
                x=x+1
            elif(dice==2):
                x=x-1
            elif(dice==3):
                y=y+1
            elif(dice==4):
                y=y-1
            
            if(-A>x):
                x=x+1
            elif(x>A):
                x=x-1
            if(y>A):
                y=y-1
            elif(-A>y):
                y=y+1
        if(i%10==9):
                sum1[r][k]=x
                sum2[r][k]=y
                r+=1
    x=0
    y=0
    r=0

for i in range(10):
    z=np.zeros([21,21])
    for j in range(10000):
        x=sum1[i][j]
        y=sum2[i][j]
        z[int(x+10),int(y+10)]=z[int(x+10),int(y+10)]+1
    im=plt.imshow(z,vmin=0,vmax=100)
    artists.append([im])

ani =animation.ArtistAnimation(fig,artists, interval=500, repeat_delay=1000)
plt.show()