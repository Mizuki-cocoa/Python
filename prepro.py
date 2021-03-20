from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer

dataset=load_boston()

x=dataset.data
t=dataset.target

x_train,x_test,t_train,t_test=train_test_split(x,t,test_size=0.3,random_state=0)
scaler=PowerTransformer()
#PowerTransformerメゾットはべき変換を行うもの
#べき変換の変換手法は2種類あり、Box-CoxとYeo-Johnsonがある。
#scikit-learnのPowerTransformerではYeo-Johnsonの手法を採用している
#べき変換とは、データを正規分布に近くなるように正規化すること
#正規分布とは平均値、最頻値、中央値が一致する分布のこと
scaler.fit(x_train)

x_train_scaled = scaler.transform(x_train)
x_test_scaled = scaler.transform(x_test)

reg_model=LinearRegression()

a=reg_model.fit(x_train_scaled, t_train)
print(a)

b=reg_model.score(x_train_scaled,t_train)
c=reg_model.score(x_test_scaled,t_train)
print(b)
print(c)