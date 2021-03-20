import pandas as pd
import chainer
df=pd.read_csv('california_housing_train.csv')
#csvファイルを読み込む dfはデータフレーム
type(df)

df['longitude'].head()
#先頭の5項目を表示
#項目の選択もできる

df.shape
#行数と列数を確認

df.mean()
#それぞれの項目の平均値を調べる

df.var()
#それぞれの項目の分散を調べる

df.count()
#各列のNone,NaN,NaTでもない値の数

df.describe
#データの概要　describeは描く、記述する

df.corr()
#相関係数の算出

df_as=df.sort_values(by='total_rooms')
#sortで並び替え
#昇順(だんだん値が大きくなる)ascensing　デフォルトだと昇順になるようになっている
#byで並び替え隊列数の項目を指定

print(df_as.head())

df_de=df.sort_values(by='total_rooms',ascending=False)
#降順(だんだん値が小さくなる)　descending 
print(df_de.head())

#一番右の項目とそれ以外の項目に分ける
t=df.iloc[:,-1]

x=df.iloc[:,0:-1]

mask=df['median_house_value']>70000

print(mask.head())
#条件を見たいしているかTrue,False判定　maskと呼ぶ

df[mask].head()
#条件を見たいしているmaskを表示

mask2=(df['median_house_value']<70000)|(df['median_house_value']>80000)
#またはが|

mask3=(df['median_house_value']<70000)&(df['median_house_value']>80000)
#かつは&

df['target']=None
#新たにtargetの項目を追加

print(type(df.values))


