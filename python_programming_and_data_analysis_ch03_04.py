# -*- coding: utf-8 -*-
"""python_programming_and_data_analysis_ch03_04

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nNGKax9gnxts4oU9MpdW7u4gAxIUwrZw

## 3.4 データ集計

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
pd.set_option("display.max_columns", None)

""" ### 3.4.2 ファイルダウンロード"""

# URL指定
zip_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip'
fn = 'bank-full.csv'

# 公開データのダウンロードと解凍
!wget $zip_url
!unzip -o bank.zip

# ファイルの先頭5行の内容確認
!head -5 bank.csv

"""* ヘッダ行あり
* 区切り文字はセミコロン
* NULL値は'unknown'
* True / Falseは'yes' / 'no'
* 文字列のクオートはダブルクオート(これはオプション指定不要)

### 3.4.3 CSVファイル読み込み

#### 読み込み
"""

# bank-full.csvをデータフレームに取り込み
df = pd.read_csv(
    fn,
    sep=';',
    na_values='unknown',
    true_values=['yes'],
    false_values=['no'])

# 結果確認
display(df.head(2))

"""### 3.4.4 データ確認・加工

#### 項目名差し替え
"""

# 項目名の日本語定義
columns = [
    '年齢', '職業', '婚姻', '学歴', '債務不履行', '平均残高',
    '住宅ローン', '個人ローン', '連絡手段', '最終通話日',
    '最終通話月', '最終通話秒数', '通話回数_販促中',
    '前回販促後_経過日数', '通話回数_販促前', '前回販促結果',
    '今回販促結果'
]
# 項目名差し替え
df2 = df.copy()
df2.columns = columns

# 項目順番入れ替え
# 一番うしろの「今回販促結果」を一番前にする
# 「個人ローン」より後ろの項目を落とす
columns1 = list(df2.columns)
print(columns1)
columns2 = columns1[-1:] + columns1[:-9]
print(columns2)
df2 = df2[columns2]

"""#### データ内容確認"""

# データ内容確認
display(df2.head())

display(df2.tail())

"""#### データ型確認

"""

# データ型確認
df2.dtypes

"""#### 欠損値確認"""

#　欠損値確認
df2.isnull().sum()

df2.notnull().sum()

"""#### 統計値確認　数値項目"""

# 統計値
df2.describe()

"""#### 統計値確認　文字列型"""

# 統計値(文字列型)
df2.describe(include='O')

df2.value_counts()

"""### 3.4.5 グループごとの集計(groupbyメソッド)"""

# 学歴による集計結果
df_gr1 = df2.groupby('学歴').mean()

# 結果確認
display(df_gr1)

#  職業による集計結果
df_gr2 = df2.groupby('職業').mean(
).sort_values('今回販促結果', ascending=False)

# 結果確認
display(df_gr2)

"""### 3.4.6 出現頻度のクロス集計(crosstabメソッド)"""

# 出現頻度のクロス集計
# 「職業」「学歴」の2軸で頻度を集計する
df_crosstab = pd.crosstab(
    index=df2['職業'],
    columns=df2['学歴'],
    margins=True)

# 結果確認
display(df_crosstab)

# 出現頻度のクロス集計
# 「職業」「学歴」の2軸で頻度を集計する
df_crosstab = pd.crosstab(
    index=df2['職業'],
    columns=df2['学歴'],
   )

# 結果確認
display(df_crosstab)

# 出現頻度のクロス集計
# 「職業」「学歴」の2軸で頻度を集計する
#  行方向の比率計算とする
df_crosstab2 = pd.crosstab(
    index=df2['職業'],
    columns=df2['学歴'],
    normalize='index',
    margins=True)

# 結果確認
display(df_crosstab2)

# 出現頻度のクロス集計
# 「職業」「学歴」の2軸で頻度を集計する
#  行方向の比率計算とする
df_crosstab2 = pd.crosstab(
    index=df2['職業'],
    columns=df2['学歴'],
    normalize='columns',
    margins=True)

# 結果確認
display(df_crosstab2)

"""### 3.4.7 項目値のクロス集計(povot  メソッド)"""

# 職業と学歴を軸とした、今回販促結果のクロス集計
df_pivot = df2.pivot_table(
    index='職業',
    columns='学歴',
    values='今回販促結果',
    aggfunc='mean')

# 結果確認
display(df_pivot)

"""### 演習問題

1. 「住宅ローン」の有無が、今回販促結果に影響するかどうかを、groupbyメソッドで調べて下さい
2. 「住宅ローン」「学歴」の2軸で頻度分析をして下さい
3. 「住宅ローン」「学歴」の2軸で「今回販促結果」のクロス集計をして下さい
"""

# 1. 住宅ローンの有無が、今回販促結果に影響するか
df_gr = df2.groupby('住宅ローン').mean()

# 結果確認
display(df_gr)

# 2. 「住宅ローン」「学歴」の2軸で頻度分析
df_crosstab = pd.crosstab(
    index=df2['住宅ローン'],
    columns=df2['学歴'],
    margins=True
)



# 結果確認
display(df_crosstab)

# 3. 「住宅ローン」「学歴」の2軸で「今回販促結果」のクロス集計
df_pivot = df2.pivot_table(
    index='住宅ローン',
    columns='学歴',
    values='今回販促結果',
    aggfunc='mean'
)



# 結果確認
display(df_pivot)

