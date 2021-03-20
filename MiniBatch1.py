import sys, os
os.chdir('/Users/cocoa/Desktop/deep-learning-from-scratch-master/ch04')
sys.path.append(os.pardir) 
import numpy as np
from dataset.mnist import load_mnist
from cge import TwoLayerNet

(x_train,t_train),(x_test,t_test)=load_mnist(normalize=True,one_hot_label=True)
#notmalize:正規化　異なるものを一つの尺度に捉える

train_loss_list=[]
train_acc_list=[]
test_acc_list=[]

iters_num=10000
#iteration:回数のこと
train_size=x_train.shape[0]
batch_size=100
learning_rate=0.01
#学習率

iter_per_epoc=max(train_size/batch_size,1)
#1epocあたりの繰り返し数 少なくとも1ということ？

#x_train.shape[0]=60000で、ミニバッチとして100個のデータを取り出しそれぞれ勾配を求める作業を10000回繰り返す

network=TwoLayerNet(input_size=784,hidden_size=50,output_size=10)
#自分で設定できる

for i in range(iters_num):
    batch_mask=np.random.choice(train_size,batch_size)
    #train_sizeからbatch_size個ランダムに取り出す
    x_batch=x_train[batch_mask]
    t_batch=t_train[batch_mask]
    
    grad=network.numerical_gradient(x_batch,t_batch)

    for key in ('W1','b1','W2','b2'):
        network.params[key]-=learning_rate*grad[key]

        loss=network.loss(x_batch,t_batch)
        #学習経過の記録
        train_loss_list.append(loss)

        if i % iter_per_epoc==0:
            train_acc=network.accuracy(x_train,t_train)
            test_acc=network.accuracy(x_test,t_test)

            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)
            print(str(train_acc)+","+str(test_acc))

