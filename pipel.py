from sklearn.pipeline import Pipeline
#パイプライン、前処理と重回帰分析を同時に行う
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import time
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PowerTransformer

dataset=load_boston()

x=dataset.data
t=dataset.target

x_train,x_test,t_train,t_test=train_test_split(x,t,test_size=0.3,random_state=0)

pipeline=Pipeline([
    ('scaler',PowerTransformer()),
    ('reg',LinearRegression())
])

pipeline.fit(x_train,t_train)

a=pipeline.score(x_train,t_train)
print(a)
linear_result=pipeline.score(x_test,t_test)
print(linear_result)