import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import random

A=10
x=0
y=0
r=0
sum=0
n=100

dicex=[]
dicey=[]
rn=[]
nx=[]

dicex.append(x)
dicey.append(y)
rn.append(r)
nx.append(0)

fig = plt.figure()
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
    else:
        if(-A>x):
            x=2*A+x-1
            dicex.append(x)
            dicey.append(y)
        if(y>A):
            y=-2*A+y-1
            dicex.append(x)
            dicey.append(y)

    if(-A<=x and y<=A):
        dicex.append(x)
        dicey.append(y)


print(dicex)
print(dicey)
print(len(dicex))
print(len(dicey))
#print(len(rn))

#print(len(nx))
#print(len(rn))

plt.plot(dicex,dicey,marker="o", color = "blue", linestyle = "--")
plt.grid(which='major',color='black',linestyle='-')
#ani = animation.ArtistAnimation(fig,dicex,interval=50)
plt.show()