import requests,pprint

# https://www.mediawiki.org/wiki/API:Main_page/ja
api_url = 'https://www.mediawiki.org/w/api.php';
# クエリ（問い合わせる）パラメータ（urlの?以降の部分）
api_params = {
    'format': 'json',
    'action': 'query',
    'titles': '椎名林檎',
    'prop': 'revisions',
    'rvprop': 'content'
};
wiki_data = requests.get(api_url, params=api_params).json();
pprint.pprint(wiki_data);