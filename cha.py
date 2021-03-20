#import chainer
#chainer.print_runtime_info()
#import chainer.links as L
#print(chainer.show_config())
import numpy as np
import matplotlib

x=np.array([2,3,1])
#入力値

t=np.array([20])

w1=np.array([[3,1,2],[-2,-3,-1]])
b1=np.array([0,0])
#簡略化のため重みベクトルは全て0にする

w2=np.array([[3,2]])
b2=np.array([0])

u1=w1.dot(x)+b1
#dotは行列の計算
h1=1.0/(1+np.exp(-u1))
#活性化関数(シグモイド関数)
#expは自然対数

y=w2.dot(h1)+b2

#更新量の計算
dLdy=-2*(t-y)
dydw2=h1

dLdw2=dLdy*dydw2

dydh1=h1*(1-h1)

dh1du1=w2
du1dw1=x

#一旦計算
dLdu1=dLdy*dydh1*dh1du1

#du1dw1(x)は(3,)というshapeなので、(1,3)の形に変形する必要がある
du1dw1=du1dw1[None]

dLdw1=dLdu1.T.dot(du1dw1)

print(dLdw1)
