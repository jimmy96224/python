# -*- coding: utf-8 -*-
"""python_programming_and_data_analysis_ch03_02

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r_W9xEvWRTIroUDcRGlso0t8C5Vqaf7z

## 3.2 データ読み込み

### 共通処理
"""

# 日本語化ライブラリ導入
!pip install japanize-matplotlib | tail -n 1

# ライブラリのimport

# NumPy用ライブラリ
import numpy as np

# Matplotlib中のpyplotライブラリのインポート
import matplotlib.pyplot as plt

# matplotlib日本語化対応ライブラリのインポート
import japanize_matplotlib

# pandas用ライブラリ
import pandas as pd

# データフレーム表示用関数
from IPython.display import display

# 表示オプション調整

# NumPy表示形式の設定
np.set_printoptions(
    suppress=True, precision=4, floatmode='fixed'
)

# グラフのデフォルトフォント指定
plt.rcParams["font.size"] = 14

# サイズ設定
plt.rcParams['figure.figsize'] = (6, 6)

# 方眼表示ON
plt.rcParams['axes.grid'] = True

# データフレームでの表示精度
pd.options.display.float_format = '{:.4f}'.format

# データフレームですべての項目を表示
pd.set_option("display.max_columns",None)

"""### 3.2.2 CSVファイルの読み込み
オリジナルサイト

https://archive.ics.uci.edu/ml/datasets/Pittsburgh+Bridges

項目説明

https://www.kaggle.com/datasets/heitornunes/pittsburgh-bridges-data-set

id: Bridge's Identifier.

river: River of the bridge.
{A : Allegheny,
M : Monongahela,
O : Ohio}

location: Bridge's Location. / 1 - 52

erected: Bridge's construction year. / 1818 - 1986
{CRAFTS: 1818 - 1866,
EMERGING: 1870 - 1889,
MATURE: 1890 - 1939,
MODERN: 1945 - 1986}

purpose: Bridge's purpose.
{WALK,
AQUEDUCT,
RR (Railroad),
HIGHWAY}

length: Bridge's length / 804-4558
{SHORT : 804 - 990,
MEDIUM : 1000 - 1850,
LONG : 2000 - 4558}

Lanes: Bridge's lanes / 1, 2, 4 and 6

clear-g: Vertical clearance requirement was enforced in the design.
{N: Not Enforced,
G: Enforced}

B) Design properties

t-or-d: The roadway location on the bridge.
{THROUGH,
DECK}

material: Bridge's predominant material.
{WOOD,
IRON,
STEEL}

span: Bridge's span.
{SHORT,
MEDIUM,
LONG}

rel-l: Relative length of the span to the crossing length.
{S: Short,
S-F: Short-Full,
F: Full}

type: Bridge's type.
{WOOD,
SUSPEN (Suspension),
SIMPLE-T (Simple Truss),
ARCH,
CANTILEV (Cantilever),
CONT-T (Continuous Truss)}

Source:
https://archive.ics.uci.edu/ml/datasets/Pittsburgh+Bridges

Reich, Yoram, and Steven J. Fenves. "The formation and use of abstract concepts in design." Concept Formation. Morgan Kaufmann, 1991. 323-353.
Reich, Yoram. "Combining nominal and continuous properties in an incremental learning system for design." (1989).

#### データの内容確認
"""

# データの内容確認

# URL指定
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/bridges/bridges.data.version1'

# ファイルダウンロード
!wget -nc $url

# 内容確認
!head -2 bridges.data.version1

"""#### read_csv関数の実行"""

# 列名定義
columns = [
 'ID', 'RIVER', 'LOCATION', 'ERECTED', 'PURPOSE',
 'LENGTH', 'LANES', 'CLEAR-G', 'T-OR-D', 'MATERIAL',
 'SPAN', 'REL-L', 'TYPE'
]

# データ読み込み
df1 = pd.read_csv(
    url, header=None, names=columns)
display(df1.head())

"""#### na_valuesオプションの追加"""

# na_valuesオプション追加
df2 = pd.read_csv(
    url, na_values='?', header=None,
    names=columns)
display(df2.head())

"""### index_colオプションの追加"""

# index_colオプションの追加
df3 = pd.read_csv(
    url, na_values='?', header=None,
    names=columns, index_col='ID')
display(df3.head())

"""### 3.2.4 CSV・Excelファイルへの出力"""

# データフレームdf2をCSVファイルとして保存
# この場合はindex=Falseオプションを付ける
df2.to_csv('bridge2.csv', index=False)

# データフレームdf3をCSVファイルとして保存
# 今回はIndex=Falseは付けない
df3.to_csv('bridge3.csv')

# データフレームdf2をExcelとして保存
df2.to_excel('bridge2.xlsx', index=False)

# 結果確認
!ls

"""### 演習問題"""

# 演習問題用ファイルのダウンロード
url = 'https://raw.githubusercontent.com/makaishi2/samples/main/data/ch03-02-exam.tsv'
!wget -nc $url

# 演習問題用ファイルの内容確認
!cat ch03-02-exam.tsv

"""#### 問題
ダウンロード済みのファイルch03-02-exam.tsvをデータフレームに読み込んで下さい。
"""

# 次の行を実装します
columns=['ID', '氏名', '性別', '身長', '体重']

df4 = pd.read_csv(
    url, skiprows=6, sep=',', header=  None , names=columns , index_col='ID'
)



# 結果確認
display(df4)

# 次の行を実装します

df4 = pd.read_csv(
    'ch03-02-exam.tsv', skiprows=6, sep='\t', dtype=object
)



# 結果確認
display(df4)



# 次の行を実装します

df4 = pd.read_csv(
    'ch03-02-exam.tsv', skiprows=6, sep='\t'
)



# 結果確認
display(df4)

# 別解
# このように列単位でdtype指定をすると、他の項目に影響を与えないです
# 文字列であることを明示的に示す場合objectの代わりにstrを使います
df5 = pd.read_csv(
    'ch03-02-exam.tsv',
    header=6, sep='\t', dtype={'ID': str})

# 結果確認
display(df5)