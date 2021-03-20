import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

A=100
x=0
y=0
kr=10000

fig, ax = plt.subplots()
artists=[]

xn1=np.zeros(kr,dtype = int)
yn1=np.zeros(kr,dtype = int)
pos=np.zeros([2*A+1,2*A+1],dtype = int)

for t in range(100):
    for n in range(10000):
        dice=random.randint(1,5)
        if(dice==1 and xn1[n]<A):
            if(pos[xn1[n]+A+1][yn1[n]+A]==0):
                xn1[n]=xn1[n]+1
                pos[xn1[n]+A][yn1[n]+A]=0
                pos[xn1[n]+A+1][yn1[n]+A]=1
            else:
                pos[xn1[n]+A][yn1[n]+A]=1
        elif(dice==2 and -A<xn1[n]):
            if(pos[xn1[n]+A-1][yn1[n]+A]== 0):
                xn1[n]=xn1[n]-1
                pos[xn1[n]+A][yn1[n]+A]=0
                pos[xn1[n]+A-1][yn1[n]+A]=1
            else:
                pos[xn1[n]+A][yn1[n]+A]=1
        elif(dice==3 and yn1[n]<A):
            if(pos[xn1[n]+A][yn1[n]+A+1] == 0):
                yn1[n]=yn1[n]+1
                pos[xn1[n]+A][yn1[n]+A]=0
                pos[xn1[n]+A][yn1[n]+A+1]=1
            else:
                pos[xn1[n]+A][yn1[n]+A]=1
        elif(dice==4 and -A<yn1[n]):
            if(pos[xn1[n]+A][yn1[n]+A-1] == 0):
                yn1[n]=yn1[n]-1
                pos[xn1[n]+A][yn1[n]+A]=0
                pos[xn1[n]+A][yn1[n]+A-1]=1
            else:
                pos[xn1[n]+A][yn1[n]+A]=1
    xn1=0
    yn1=0
    n=0

# for i in range(10):
#     sum12=sum1[i*10]
#     sum22=sum2[i*10]
#     artists.append(ax.plot(sum12,sum22,marker="o", color = "blue"))

ani =animation.ArtistAnimation(fig,artists, interval=500, repeat_delay=1000)
plt.show()