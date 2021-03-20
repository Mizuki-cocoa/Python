import numpy as np
X = np.array([
    [2, 3],
    [2, 5],
    [3, 4],
    [5, 9],
])
print(X)
ones=np.ones((X.shape[0],1))
X=np.concatenate((ones,X),axis=1)
#concatenateの意味は連結

print(X)
#先頭に1が付け加わったデザイン行列、bの省略を行うため

t=np.array([1,5,6,8])
#目標値

#転置行列＊行列,X**TとXの内積
xx=np.dot(X.T,X)#dotは内積の計算に使われる
print(xx)#単純に掛け算は＊を使う

xx_inv=np.linalg.inv(xx)#逆行列の計算
print(xx_inv)

xt=np.dot(X.T,t)#X**Tとtの内積
print(xt)

w=np.dot(xx_inv,xt)#正期方程式
print(w)

