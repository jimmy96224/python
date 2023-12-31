# -*- coding: utf-8 -*-
"""python_programming_and_data_analysis_ch2_3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/181190c5CFG9JdaHsQ2b1RgBWfFb4QF6n

## 2.3 Matplotlib入門

### 2.3.2 ライブラリの利用と日本語化
"""

# 事前処理

# 必要ライブラリのimport
import numpy as np

# NumPy表示形式の設定
np.set_printoptions(
    suppress=True, precision=4, floatmode='fixed'
)

# 日本語化ライブラリ導入
!pip install japanize-matplotlib | tail -n 1

# Matplotlib中のpyplotライブラリのインポート
import matplotlib.pyplot as plt

# matplotlib日本語化対応ライブラリのインポート
import japanize_matplotlib

# グラフのデフォルトフォント指定(pt)
plt.rcParams["font.size"] = 14

# サイズ設定(幅×高さ、インチ)
plt.rcParams['figure.figsize'] = (6, 6)

"""### 2.3.3 scatter(散布図)

#### データ準備
"""

# グラフ描画用のデータをライブラリを用いて取得する
from sklearn.datasets import load_iris
iris = load_iris()
x, y = iris.data, iris.target
columns = iris.feature_names

# x, y, columnsの型を確認
print(type(x), type(y), type(columns))

# 読み込んだデータの確認

# xとyのshape確認
print(x.shape, y.shape)

# xの先頭5行
print(x[:5])

# yの先頭5行
print(y[:5])

# columnsの内容
print(columns)

"""#### 簡単な散布図"""

# 簡単な散布図

# scatter関数呼び出し
plt.scatter(x[:,0], x[:,2])

# 描画
plt.show()

"""#### やや複雑な散布図"""

#　やや複雑な散布図

# scatter関数呼び出し　（yの値で色を変える,c=color）
plt.scatter(x[:,0], x[:,2], c=y, cmap='rainbow')

# 方眼表示
plt.grid()

# 軸名称表示
plt.xlabel(columns[0])
plt.ylabel(columns[2])

# タイトル表示
plt.title('アイリスデータセットによる散布図')

# 描画
plt.show()

"""### 2.3.4 plot(関数グラフ)

#### データ準備
"""

# xの配列の準備
x = np.linspace(0, 2, 11)
print(x)

# y=sqrt(x)の計算
y = np.sqrt(x)
print(y)

"""#### 簡単な関数グラフ"""

# 簡単な関数グラフ描画

# plot関数呼び出し
plt.plot(x, y)

# 描画
plt.show()

"""#### やや複雑な関数グラフ"""

# データ準備

# xの配列の準備
x = np.linspace(0, 2, 101)

# yの配列の準備
y1 = np.sqrt(x) # ルート関数
y2 = x ** 2    # ２次関数

# やや複雑な関数グラフの描画

# plot関数を2回続けて呼び出すと重ね描きになる
# label引数は、凡例表示をする場合に必要
plt.plot(x, y1, label='ルート関数')
plt.plot(x, y2, label='2次関数')

# 凡例表示
plt.legend()

plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title('2つの関数グラフの重ね描き')
plt.show()

"""### 2.3.5 複数グラフ表示

#### データ準備
"""

from sklearn.datasets import load_iris
iris = load_iris()
x, y = iris.data, iris.target
columns = iris.feature_names
print(x[:5])
print(columns)

print(iris.DESCR)

print(iris.target_names)

"""#### 複数グラフ描画"""

# サイズ指定
plt.figure(figsize=(15, 5))

# 3回ループを回す
for i in range(1, 4):

    # i 番目のax変数取得
    ax = plt.subplot(1, 3, i)

    # 散布図表示
    ax.scatter(x[:,0], x[:,i], c=y, cmap='rainbow')

    # タイトル表示
    ax.set_title(columns[0] + ' vs ' + columns[i])

    ax.grid()
# 隣接オブジェクトとぶつからないようにする
plt.tight_layout()

# 表示
plt.show()

"""### 演習問題
 アイリスデータセットの変数x, y, columnsを前提に、4つの項目すべての組み合わせで、 4x4の散布図を表示するプログラムをコーディングしなさい。  
(ヒント) Matplotlibのsubplot関数を利用します。  
同じ項目同士の散布図は統計的には意味がないのですが、実装を簡単にするため、そのまま表示して構わないものとします。

"""

# 項目数の計算
N = x.shape[1]

# figsize計算用パラメータ(1要素あたりの大きさ)
u = 5

#  描画領域全体の設定
plt.figure(figsize=(u*N, u*N))

for i in range(N):
    for j in range(N):
        # この計算は、図2-3-2をヒントに考える
        k = i * 4 + j + 1
        ax = plt.subplot(N, N, k)

        # 以下の3行は、2.3.5項　コード2-3-12参照
        ax.scatter(x[:, i], x[:, j], c=y, cmap='rainbow')
        ax.set_title(columns[i] + ' vs ' + columns[j])
        ax.grid()

# 隣接オブジェクトとぶつからないようにする
plt.tight_layout()

# 表示
plt.show()

print(N)

# 項目数の計算
N = x.shape[1]

# figsize計算用パラメータ(1要素あたりの大きさ)
u = 5

#  描画領域全体の設定
plt.figure(figsize=(u*N, u*N))

for i in range(N):
    for j in range(N):
        # この計算は、図2-3-2をヒントに考える
        k = i * 4 + j + 1
        ax = plt.subplot(N, N, k)

        # 以下の3行は、2.3.5項　コード2-3-12参照
        ax.scatter(x[:, i], x[:, j], c=y, cmap='rainbow')
        ax.set_title(columns[i] + ' vs ' + columns[j])
        ax.grid()

# 隣接オブジェクトとぶつからないようにする
plt.tight_layout()

# 表示
plt.show()