import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import copy

A=100
x=0
y=0
kr=100

#fig, ax = plt.subplots()
#artists=[]

xn1=np.zeros(kr,dtype = int)
yn1=np.zeros(kr,dtype = int)
pos=np.zeros([2*A+1,2*A+1],dtype = int)

for i in range(kr):
    dicex=random.randint(0,200)
    dicey=random.randint(0,200)

    if(pos[dicex][dicey]==0):
        xn1[i]=dicex-A
        yn1[i]=dicey-A
        pos[dicex][dicey]=1
    else:
        i=i-1


for t in range(100):
    for n in range(kr):
        dice=random.randint(1,5)
        if(dice==1 and xn1[n]<A):
            if(pos[xn1[n]+A+1][yn1[n]+A]==0):
                pos[xn1[n]+A][yn1[n]+A]=0
                pos[xn1[n]+A+1][yn1[n]+A]=1
                xn1[n]=xn1[n]+1
            else:
                pos[xn1[n]+A][yn1[n]+A]=1
        elif(dice==2 and -A<xn1[n]):
            if(pos[xn1[n]+A-1][yn1[n]+A]== 0):
                pos[xn1[n]+A][yn1[n]+A]=0
                pos[xn1[n]+A-1][yn1[n]+A]=1
                xn1[n]=xn1[n]-1
            else:
                pos[xn1[n]+A][yn1[n]+A]=1
        elif(dice==3 and yn1[n]<A):
            if(pos[xn1[n]+A][yn1[n]+A+1] == 0):
                pos[xn1[n]+A][yn1[n]+A]=0
                pos[xn1[n]+A][yn1[n]+A+1]=1
                yn1[n]=yn1[n]+1
            else:
                pos[xn1[n]+A][yn1[n]+A]=1
        elif(dice==4 and -A<yn1[n]):
            if(pos[xn1[n]+A][yn1[n]+A-1] == 0):
                pos[xn1[n]+A][yn1[n]+A]=0
                pos[xn1[n]+A][yn1[n]+A-1]=1
                yn1[n]=yn1[n]-1
            else:
                pos[xn1[n]+A][yn1[n]+A]=1

x = xn1.copy()
y = yn1.copy()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

plt.xlim(-100,100)
plt.ylim(-100,100)

ax.scatter(x,y,s=5)
fig.show()

#ani =animation.ArtistAnimation(fig,artists, interval=500, repeat_delay=1000)
plt.show()
