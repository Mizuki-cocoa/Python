import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

A=10
x=0
y=0
r=0
sum=0
n=100

fig, ax = plt.subplots()
dicex=[]
dicey=[]
artists=[]
rn=[]
nx=[]
title=[]

dicex.append(x)
dicey.append(y)
rn.append(r)
nx.append(0)

ax.grid(True)
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
        
        dicex.append(x)
        dicey.append(y)
        
        #artists.append(ax.text(0.5, 1.1, f'TITLE {i}',transform=plt.gca().transAxes))
        artists.append(ax.plot(dicex,dicey,marker="o", color = "blue"))
        #artists.append(ax.text(0.1,0.5,i))
        print(i)

ani =animation.ArtistAnimation(fig,artists, interval=500, repeat_delay=1000)
#plt.plot(dicex,dicey,marker="o", color = "blue", linestyle = "--")
plt.show()