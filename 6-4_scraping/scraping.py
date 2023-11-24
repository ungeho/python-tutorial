# クローリング：Webサイトからそのまま情報を取得してくること
# クロール（crawl）：地面に横ばいで這う動き
# スクレイピング：クローリングして集めてきたデータから必要なものだけを抽出したり、成型する処理
# 欲しい情報がどのタグの中にあるかを予め確認しておき、取得しにいくなど
# スクレープ（scrape）：削って剥がす


import requests
# webページをごった煮のスープのように例え、クロールリングしたページのタグの閉じ忘れなどをキチンと閉じて処理してくれる。
from bs4 import BeautifulSoup

html_data = requests.get('https://yahoo.co.jp');
# html.parserはpythonに標準で入っている htmlを読み解く為に使うプログラム
soup = BeautifulSoup(html_data.text, "html.parser");

# タイトルタグとその中身を表示
print(soup.title);

# 型を表示
print(type(soup));

# findAll：HTMLの属性と属性値を指定し、該当する全ての要素を返す
# find：HTMLの属性と属性値を指定し、一つの要素だけ返す
# select：CSSセレクタを指定し、全ての要素を返す
# select_one：CSSセレクタを指定し、一つの要素だけ返す
# get 指定した属性の値を返す。（aタグのhref属性の値など）
# text 指定したタグのテキストを取得する
# print(soup.findAll('div'));

# Selenium + Beautiful Soup
# Javascriptによるクライアント側でページを書き換える動的なコンテンツはSeleniumも使う
# また、PHPのようなサーバー側でページを書き換えるものは、requestsでパラメータを渡す。
# https://qiita.com/Moh_no/items/a835f77b6b4e3972fbbe

# アマゾンのゲーム最新リリース
# game_ranking_html = requests.get(
    # 'https://www.amazon.co.jp/gp/new-releases/videogames/637394')
# soup = BeautifulSoup(game_ranking_html.text, "html.parser");
# htmlのclass名で検索する時は、class=ではなくclass_=
# findを繋げる事で、見つけた要素の中からさらに探す事が出来る。
# print(soup.find(class_='zgitemRow').find(class_='zg_title').find_one('a').string);

# 見つけた物を元に、findallとforで回す事も出来る。
# for game in soup.findAll(class_='zg_itemRow'):
    # print(game.find(class_='zg_rankNumber').string + game.find(class_='zg_title').find('a').string );


