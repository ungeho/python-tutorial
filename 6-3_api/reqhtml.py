# pip install requests
import requests
# 大量のデータを見やすくする為の標準モジュール
import pprint

r = requests.get('http://www.yahoo.co.jp');
# 読み込んだhtmlがテキストで表示される
# print(r.text);
# 読み込んだhtmlが改行込みの見やすい形のテキストで表示される
pprint.pprint(r.text);