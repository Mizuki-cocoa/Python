import matplotlib.pyplot as plt
import numpy as np

a=0.4
b=1.8
e=10**(-10)

cnt=0

xlists=[]
ylists=[]

ax=plt.gca()
ax.set_yscale('log')

def f(x):
    return x**3-x**2

while(abs(a-b)>e):
    cnt+=1
    xlists.append(cnt)

    c=(a+b)/2
    ylists.append(abs(1.0-c))#正解の解が1.0とわかっている状態
    #絶対値表示をしないと

    print('c：{0}'.format(c))
    if(f(a)*f(c)>0):
        a=c
        print('f(a)：{0}'.format(f(a)))
    elif(f(b)*f(c)>0):
        b=c
        print('f(b)：{0}'.format(f(b)))
    elif(f(c)==0):
        print('c：{0}'.format(c))
        break

plt.plot(xlists, ylists, marker="o", color = "blue", linestyle = "--")
plt.show()