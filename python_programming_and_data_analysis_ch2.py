# -*- coding: utf-8 -*-
"""python programming and data analysis ch2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NQiuJZ3YGb9WmEqsHQihykJH7Y7L-9se

## 2.1 ライブラリ

### 2.1.2 import文
"""

# 標準ライブラリmathを利用することの宣言
import math

# mathライブラリのsqrt関数は「math.sqrt」の形で呼び出す
r2 = math.sqrt(2)

# 計算結果の確認 (2の平方根)
print(r2)

# ライブラリ中の特定の関数のみ利用する場合は下記の方法も可
from math import sqrt

# この場合は、「sqrt」だけで関数を呼び出せる
r2 = sqrt(2)

# 結果確認
print(r2)

# 外部ライブラリnumpyを利用することの宣言
# 「as np」は別名定義　利用時は「np.xxx」の形で呼び出すことになる
import numpy as np

# numpy上の1次元配列宣言(0から2まで0.2刻みの等差数列)
x = np.linspace(0, 2, 11)

# 結果確認
print(x)

# numpyのsqrt関数呼び出し
y = np.sqrt(x)

# 結果確認 (1から10までの平方根が同時に計算できている)
print(y)

# 外部ライブラリのバージョン確認方法
import numpy
print(numpy.__version__)

"""### コラム　メソッドと間違えやすい関数"""

# 関数呼び出しの例
# npはimport文で定義されている

import numpy as np
n1 = np.array([1, 7, 5, 2])
print(n1)

# メソッド呼び出しの例
# s1は代入文で定義されている

s1 = 'I like an apple.'
s1.upper()
print(s1)

"""### 2.1.3 !pipコマンド"""

# matplotlib日本語化ライブラリの導入
!pip install japanize-matplotlib | tail -n 1

# matplotlib日本語化ライブラリのインポート
import japanize_matplotlib

"""### コラム Python変数の値をOSコマンドに渡す"""

# 条件を満たすファイル名リストを取得する

import glob
files = glob.glob('sample_data/*.csv')
print(files)

# filesの2番目の要素を抽出

file = files[1]
print(file)

# 変数fileの内容を!headコマンドに渡す

!head -2 $file