from math import factorial
#ここでは分子について計算する
sum=0
for i in range(21):
    print('不正解数：{0}'.format(i))
    numerator=3**i
    #不正解の確率である3/4の3を(不正解数乗)した数
    C= factorial(20) / factorial(i) / factorial(20-i)
    #組み合わせ
    mult=numerator*C
    #numeratorとCの掛け算
    print('組み合わせと3の累乗をかけた数：{0}'.format(mult))
    sum+=mult

print('分子の合計：{0}'.format(sum))
print(4**20)
print(514236959/549755813888)
