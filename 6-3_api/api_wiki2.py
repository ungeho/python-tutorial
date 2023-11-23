import requests
import codecs
import os

api_base_url = 'https://ja.wikipedia.org/w/api.php';

api_params = {
    # xml形式のデータをhtml形式に成型したものを取得する
    'format': 'xmlfm',
    'action': 'query',
    'titiles': '椎名林檎',
    'prop': 'revisions',
    'rvprop': 'content'
};

wiki_data = requests.get(api_base_url,params=api_params);

# 任意の場所にhtmlで書き込む
fo = codecs.open('C:\\Users\\' + os.environ['USERNAME'] +
                 '\\Documents\\GitHub\\python-tutorial\\6-3_api\\wiki\\wiki.html',
                 mode='w',encoding='utf-8');
fo.write(wiki_data.text);
fo.close();
