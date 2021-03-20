import sys, os
os.chdir('/Users/cocoa/Desktop/deep-learning-from-scratch-master/ch03')
sys.path.append(os.pardir) 
from dataset.mnist import load_mnist
 # 親ディレクトリのファイルをインポートするための設定
import numpy as np
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    #PIL用に変形
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

#flatten=Trueによって、一次元配列になっている
img = x_train[0]
label = t_train[0]
print(label)  # 5

print(img.shape)  # (784,)
img = img.reshape(28, 28)  # 形状を元の画像サイズに変形
print(img.shape)  # (28, 28)

img_show(img)
