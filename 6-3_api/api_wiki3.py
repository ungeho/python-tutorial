import requests , sys
import codecs
import os

# py api_wiki3.py aaa
# 上記の場合0番目にはプログラム名,1番目にはaaaが入る。
# print(sys.argv);

search_word = sys.argv[1];


api_base_url = 'https://ja.wikipedia.org/w/api.php'

api_params = {
    # xml形式のデータをhtml形式に成型したものを取得する
    'format': 'xmlfm',
    'action': 'query',
    'prop': 'revisions',
    'rvprop': 'content'
}
# 辞書型のparamsに追加
api_params['titles'] = search_word;

wiki_data = requests.get(api_base_url, params=api_params)

# 任意の場所にhtmlで書き込む
fo = codecs.open('C:\\Users\\' + os.environ['USERNAME'] +
                 '\\Documents\\GitHub\\python-tutorial\\6-3_api\\wiki\\' + search_word + '.html',
                 mode='w', encoding='utf-8')
fo.write(wiki_data.text)
fo.close()
