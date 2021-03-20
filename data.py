from pandas_datareader import data
import pandas as pd
import matplotlib.pyplot as plt

start='2019-06-01'
end='2020-06-01'

df=data.DataReader('^N225','yahoo',start,end)
#print(df.head(10))
#print(df.index)#時系列で扱いやすい

time=df.index
price=df['Adj Close']#調整後の終値

span01=5
span02=25
span03=50

df['span01']=price.rolling(window=span01).mean()
df['span02']=price.rolling(window=span02).mean()
df['span03']=price.rolling(window=span03).mean()
#print(df.head(100))

#plt.figure(figsize=(30,10))
plt.subplot(2,1,1)
plt.plot(time,df['span01'],label='span01')
plt.plot(time,df['span02'],label='span02')
plt.plot(time,df['span03'],label='span03')
plt.plot(time,price)
plt.legend()

plt.subplot(2,1,2)
plt.bar(time,df['Volume'],label='Volume',color='grey')

plt.show()