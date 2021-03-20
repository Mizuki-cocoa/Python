import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

n=1000000
# 乱数を生成,それ自体がリストになっている
x = np.random.rand(n)*2*math.pi
y = np.random.rand(n)*6

xy=[]
yy=[]
xn=[]
yn=[]

def f(x):
    return x*(np.sin(x))**2

i=0
cnt=0

for i in range(n):
    if(y[i]<=f(x[i])):
        xy.append(x[i])
        yy.append(y[i])
        cnt+=1
    else:
        xn.append(x[i])
        yn.append(y[i])

print(cnt/n*2*math.pi*6)

plt.scatter(xy, yy,color="r",s=1.0)
plt.scatter(xn, yn,color="b",s=1.0)


xr = np.arange(0,6.5,0.1)
yr = f(xr)

plt.plot(xr, yr)

plt.show()