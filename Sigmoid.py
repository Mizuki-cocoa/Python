import numpy as np
import matplotlib.pylab as plt

def sigmoid1(x):
    return 1/(1+np.exp(-x))

x1=np.arange(-5.0,5.0,0.1)
y1=sigmoid1(x1)

plt.plot(x1,y1)
plt.ylim(-0.1,1.1)
plt.show()


def step_function(x):
    return np.array(x>0,dtype=np.int)

x=np.arange(-5.0,5.0,0.1)
y=step_function(x)

plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()