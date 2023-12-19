# -*- coding: utf-8 -*-
"""ch01_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MEnKETMvNpyGg3dmEwpZLEMtQq8TkXgz

## 1.2 階乗計算
"""

# 階乗計算

# ループカウントNの定義
N = 10

# 階乗結果の保存先
fact = 1

# ループ処理
for i in range(1, N + 1):

    # 階乗計算
    fact *= i

   # 結果表示
    print(i, 'の階乗は', fact)

# 階乗計算

# ループカウントNの定義
N = 60

# 階乗結果の保存先
fact = 1

# ループ処理
for i in range(1, N + 1):

    # 階乗計算
    fact *= i

   # 結果表示
    print(i, 'の階乗は', fact)

"""演習問題"""

a = 3
b = 10

c = b - a

print(a)
print(b)
print(c)

a = 1000
b = 2000
c = 3000

d = a % 7

d += b % 7

d += c % 7

print(d)

x = 12

if x >= 10 and x % 3 == 0:
    print('Success!')
else:
    print('Fail!')

"""elseにも : <br>
文字列は ' '
"""



x = 9

if x >= 10 and x % 3 == 0:
    print('Success!')
else:
    print('Fail!')



x = 13

if x >= 10 and x % 3 == 0:
    print('Success!')
else:
    print('Fail!')

x = 15

if x >= 10 and x % 3 == 0:
    print('Success!')
else:
    print('Fail!')

s1 = 'I like an apple.'
 s2 = 'apple'

 p1 = s1. find(s2)

 print(p1)



s1 = 'I like an apple.'
 s2 = 'orange'

 p1 = s1. find(s2)

 print(p1)

"""find メソッドは、検索対象の文字列が存在しない場合、「-1」を返す"""

s1 = 'I like an apple.'
 s2 = 'apple'

if s2 == 'apple' and s1.find(s2) != -1:
    print('I like an apple.はappleを含んでいます。')
elif  s2 == 'orange' and s1.find(s2) == -1:
    print('I like an apple.はorangeを含んでいません。')

s1 = 'I like an apple.'
 s2 = 'apple'

if s1.find(s2) >= 0:
    m1 = 'を含んでいます。'
else:
    m1 = 'を含んでいません。'

print(s1, 'は', s2, m1)

