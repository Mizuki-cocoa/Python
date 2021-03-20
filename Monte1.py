import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

n=100000
# 乱数を生成,それ自体がリストになっている
x = np.random.rand(n)
y = np.random.rand(n)
z = np.random.rand(n)

axe=[]
xv=[]
yv=[]
i=0
cnt=0

for i in range(n):
    a=(((x[i])**2+(y[i])**2+(z[i])**2))**(2)
    if(a<=1.0):
        cnt+=1
    else:
        xv.append(x[i])#円以外の部分の記述
        yv.append(y[i])


print(6*cnt/n)
print(math.pi)
print(6*cnt/n-math.pi)#誤差

plt.show()