from Mul import *

apple=100
apple_num=2
orange=150
orange_num=3
tax=1.1

mul_apple_layer=MulLayer()
mul_orange_layer=MulLayer()
add_apple_orange=AddLayer()
mul_tax_layer=MulLayer()

apple_price=mul_apple_layer.forward(apple,apple_num)
orange_price=mul_orange_layer.forward(orange,orange_num)
all_price=add_apple_orange.forward(apple_price,orange_price)
#mul_apple_layerがクラスになって、林檎の値段と林檎数をかけている
#合計金額：(林檎の値段)*(林檎の数)
price=mul_tax_layer.forward(all_price,tax)
#合算：(本体価格)＊(税率)

#forwardの順番とは、逆の順番でbckwardを実行
dprice=1
dall_price,dtax=mul_tax_layer.backward(dprice)
dapple_price,dorange_price=add_apple_orange.backward(dall_price)
dapple,dapple_num=mul_apple_layer.backward(dapple_price)
dorange,dorange_num=mul_orange_layer.backward(dorange_price)

print(dtax,dapple,dapple_num,dorange,dorange_num)


