import numpy as np
import matplotlib.pyplot as plt
import random

n=200
kr=100000
x=0
i=0


dicel=[]
xl=[]
xk=[]

dicel.append(x)
xl.append(i)

for k in range(kr):
    for i in range(n):
        dice=random.randint(1,6)
        if(dice==1):
            x=x+1
        elif(dice==6):
            x=x-1
        dicel.append(x)
        xl.append(i)
        #print(x)
    #print("--------")
    xk.append(x)
    x=0#初期化

#print(xk)
cnt=[]
xr=[]

for r in range(200):
    rr=r-100
    cnt.append(xk.count(rr))
    xr.append(rr)

plt.bar(xr,cnt)
plt.show()