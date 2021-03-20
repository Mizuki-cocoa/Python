import sys, os
os.chdir('/Users/cocoa/Desktop/deep-learning-from-scratch-master/ch05')
sys.path.append(os.pardir) 
from common.layers import *
from collections import OrderedDict
from common.gradient import numerical_gradient

class TwoLayerNet:
    def __init__(self,input__size,hidden__size,output__size,weight_init_std=0.01):
        #初期化を行う関数
        #__init__は初期化メゾット、コンストラクタ、selfを第一引数にとる
        self.params={}
        #関数に渡される具体的な値のプレースホルダ,ニューラルネットワークのパラメータを保持するディレクショナリ変数
        self.params['W1']=weight_init_std*np.random.randn(input_size,hidden__size)
        #randnrandnは標準正規分布（ガウス分布）でランダムな数値を出力する。標準正規分布（ガウス分布）は、平均0, 標準偏差1の正規分布
        self.params['b1']=np.zeros(hidden__size)
        self.params['W2']=weight_init_std*np.random.randn(hidden_size, output__size)
        self.params['b2']=np.zeros(output__size)

        self.layers=OrderedDict()
        #順序付き辞書,ディレクショナリに追加した要素の順番を覚えておくことができる
        #forwardとbackforwardの順番を機にすることなく実行することができる
        self.layers['Affine1']=Affine(self.params['W1'],self.params['b1'])
        self.layers['Relu1']=Relu()
        self.layers['Affine2']=Affine(self.params['W2'],self.params['b2'])

        self.lastLayer=SoftmaxWithLoss()

   def predict(self,x):
       for layer in self.layers.values():
           x=layer.forward(x)
     return x
    
    def loss(self,x,t):
        #損失函数
        #xは入力データ、tは教師データ
        y=self.predict(x)
        return cross_entropy_error(y,t)
    
    def accuracy(self,x,t):
        #accuracy:正確さ 認識精度について
        y=self.predict(x)
        y=np.argmax(y,axis=1)
        t=np.argmax(t,axis=1)
        #axis=1は行に沿った、axis=0は列に沿った
        #argmax:最大値をとる定義域の元全体の成す集合
        accuracy=np.sum(y==t)/float(x.shape[0])
        return accuracy
    
    def numerical_gradient(self,x,t):
        loss_W=lambda W: self.loss(x,t)
        #重みパラメータに対する勾配
        #lamba式
        grads={}
        #dL/dW:
        grads['W1']=numerical_gradient(loss_W,self.params['W1'])
        grads['b1']=numerical_gradient(loss_W,self.params['b1'])
        grads['W2']=numerical_gradient(loss_W,self.params['W2'])
        grads['b2']=numerical_gradient(loss_W,self.params['b2'])

        return grads

    def gradient(self, x, t):

        self.loss(x,t)
        
        W1, W2 = self.params['W1'], self.params['W2']
        b1, b2 = self.params['b1'], self.params['b2']
        grads = {}
        
        batch_num = x.shape[0]
        
        # forward
        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)
        
        # backward
        dy = (y - t) / batch_num
        grads['W2'] = np.dot(z1.T, dy)
        grads['b2'] = np.sum(dy, axis=0)
        
        dz1 = np.dot(dy, W2.T)
        da1 = sigmoid_grad(a1) * dz1
        grads['W1'] = np.dot(x.T, da1)
        grads['b1'] = np.sum(da1, axis=0)

        return grads
