import numpy as np
import matplotlib.pyplot as plt
import random

n=100
x=0
i=0

xl=[]
xk=[]

xl.append(i)
xk.append(x)

#random.seed(2)

for i in range(n):
    dice=random.randint(1,6)
    if(dice==1):
        x=x+1
    elif(dice==6):
        x=x-1
    xl.append(i)
    xk.append(x)

plt.plot(xl,xk,marker="o", color = "blue", linestyle = "--")
plt.show()