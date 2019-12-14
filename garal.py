from bs4 import BeautifulSoup
from time import sleep
import urllib.request as req

# タイプ名のリスト
TYPE_LIST = ['ノーマル','ほのお','みず','でんき','くさ','こおり','かくとう','どく','じめん','ひこう','エスパー','むし','いわ','ゴースト','ドラゴン','あく','はがね','フェアリー']

# JSONを出力する変数
text = '{'

# URL.txtを開く
with open('URL.txt') as textFile:

    # 1行ずつURLを取得
    for url in textFile:

        # スクレイピングはサーバ負荷をかけてはいけないので
        # 必ず1秒間は待機する
        sleep(1)

        # 目的の要素を取得する
        res = req.urlopen(url)
        soup = BeautifulSoup(res , 'html.parser')

        # タイプ表
        typeInfo = soup.select('tr > td > span')

        # 種族名
        name = soup.find('span', class_='text-l text-bold')

        if name != None:
            text += '"{name}",'.format(name=name.string)

            # ファイルに書き込む
            with open('TYPE.json', mode='a') as f:
                f.write(text)
                print(text)
                # 変数初期化
                text = ""

# 全ポケの処理が終わったら
# 波括弧を閉じてファイルに書き込む
text += "}"
with open('TYPE.json', mode='a') as f:
    f.write(text)