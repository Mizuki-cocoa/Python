import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

x0=0.4
e=10**(-10)
cnt=0

xlists=[]
ylists=[]

ax=plt.gca()
ax.set_yscale('log')

def f(x):
    return x**3-x**2
    
def d(x):
    return 3*x**2-2*x

xlists.append(cnt)#初期状態
ylists.append(x0)

while(abs(x0)>e):
    cnt+=1
    xlists.append(cnt)

    x=x0-f(x0)/d(x0)
    x0=x
    ylists.append(x0)
    
    print('x：{0}'.format(x0))
    if(f(x0)==0):
        print('x：{0}'.format(x0))
        break

plt.plot(xlists, ylists, marker="o", color = "blue", linestyle = "--")
plt.show()