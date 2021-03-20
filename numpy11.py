import numpy as np

#a=np.array([1,2,3])
#print(a)
#print('Shape:',a.shape)#形
#print('Rank:',a.ndim)#ランク

b=np.array(
    [[1,2,3],
     [4,5,6],
     [7,8,9]]
)

print(b)
print('Shape:',b.shape)#行＊列
print('Rank:',b.ndim)#n次元数
print('Size:',b.size)#サイズ

c=np.eye(5)#単位行列
print(c)

d=np.random.random((4,5))#0.0~1.0のランダム
print(d)
val=d[0,1]
print(val)

center=d[1:3,1:4]#dからの切り取り
print(center)
print(center.dtype)#属性の確認

a = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
])

b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
ab=a*b#四則演算すべてできる
print(ab)
#ブロードキャストで自動的に計算もできる

y=np.random.randint(0,10,(8,10))
#0-10までのランダム(int型),8行10列
#0から数えると8-1番目まで、単純に数で数えると8番目まで数があると考えることができる
print(y)