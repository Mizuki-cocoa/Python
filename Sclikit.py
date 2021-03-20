from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer

dataset=load_boston()

x=dataset.data
t=dataset.target

x_train,x_test,t_train,t_test=train_test_split(x,t,test_size=0.3,random_state=0)
#テスト用のデータを30%,訓練用のデータが70%
#random_stateを0にすることで実行のたびに結果が変わるのを防いでいる

reg_model=LinearRegression()#重回帰分析
reg_model.fit(x_train,t_train)#モデルの訓練
#fitメゾットで訓練開始

w=reg_model.coef_
print(w)
#訓練後のパラメータ w

b=reg_model.intercept_
print(b)
#訓練後のバイアス　b

sc=reg_model.score(x_train,t_train)
print(sc)
#決定係数、モデルが与えられたデータにどれほど当てはまるか
#scoreメゾットで制度を計算

pr=reg_model.predict(x_test[:1])
print(pr)
#予測値

prmoku=t_test[0]
print(prmoku)
#目標値

test=reg_model.score(x_test,t_test)
print(test)

scaler=StandardScaler()
#データセットの各入力変数ごとの平均と分散の値を計算する
scaler.fit(x_train)

ave=scaler.mean_
print(ave)
#平均

bun=scaler.var_
print(bun)
#標準化を施す

