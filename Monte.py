import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

n=100000
# 乱数を生成,それ自体がリストになっている
x = np.random.rand(n)
y = np.random.rand(n)

axe=[]
xv=[]
yv=[]
i=0
cnt=0

for i in range(n):
    a=((x[i])**2+(y[i])**2)**(0.5)
    if(a<=1.0):
        cnt+=1
    else:
        xv.append(x[i])#円以外の部分の記述
        yv.append(y[i])

#print(cnt)
print(math.pi-cnt/n*4)
#誤差

plt.scatter(x, y,color="r",s=1.0)
plt.scatter(xv, yv,color="b",s=1.0)
ax = plt.axes()

# fc = face color, ec = edge color
c = patches.Circle(xy=(0, 0), radius=1.0, fc='w', ec='k',fill=False)
ax.add_patch(c)

ax.set_aspect('equal')

plt.show()