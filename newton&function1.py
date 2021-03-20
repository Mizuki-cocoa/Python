import matplotlib.pyplot as plt
import numpy as np

ax=plt.subplots()
x0=0.6
e=10**(-10)

def f(x):
    return x**3-x**2

def d(x):
    return 3*(x**2)-2*x

xlists=[]
ylists=[]

while(abs(f(x0))>e):
    xlists.append(x0)
    y=f(x0)
    ylists.append(y)

    x=x0-f(x0)/d(x0)
    x0=x
    print('x：{0}'.format(x0))
    if(f(x0)==0):
        print('x：{0}'.format(x0))
        break

x1lists=[]
y1lists=[]

x = np.linspace(-0.75, 1.7, 100)
plt.plot(x,f(x),label="function")

plt.plot(xlists, ylists, marker="o", color = "blue", linestyle = "--",label="Newton low")
plt.grid(True)
#plt.plot(x1lists, y1lists, marker="+", color = "red", linestyle = "--")
plt.legend()
plt.show()