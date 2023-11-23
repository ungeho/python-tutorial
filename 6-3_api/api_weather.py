# 本の天気予報のAPI whether hacks は2020年7月にサービス終了している為、OpenWeatherMapで試してみる。
# https://openweathermap.org/current
import os
import requests
import json
import pprint
# OpenWeatherMapのAPIのラッパーライブラリ
# OpenWeatherMapのAPIで取得できるデータをシンプルなオブジェクトモデルとして扱える
from pyowm.owm import OWM
from pyowm.utils import formatting
from pyowm.utils.config import get_default_config



API_TOKEN = os.environ['OPENWEATHERMAP_KEY']

# ジオコーディングAPI
# http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
# q : 都市名,州コード（米国のみ）,国コードを区切る。国コードはISO3166を使用。都市名は日本語でも可能
# appid : API_TOKEN
# limit : APIレスポンスに含まれる場所の数（最大5件の結果を返す事が出来る。）
# URLのパラメーターを見やすく指定できる。
# URLパラメータとして同じ名前の物を繰り返し指定する場合は、辞書の値をリストにする。
urlGeo = 'http://api.openweathermap.org/geo/1.0/direct';
paramsGeo = {
    'q': '東京都',
    'limit': 5,
    'appid': API_TOKEN
}
# APIリクエスト
# jsonで取得
responseGeo = requests.get(urlGeo, params = paramsGeo).json();
# retGeo = json.loads(responseGeo.text);

# 取得出来た中身を表示する
# jsonはpythonでは読み込んだ時に辞書型に変換されている為、辞書型として扱う事が出来る
pprint.pprint(responseGeo);
print();

# pprintで出力された結果を見ると、リストの0番の中に辞書型が入っている形だったため、以下のように指定してキーのみを得る。
print(responseGeo[0].keys());
print();

# 欲しいのは東京都の緯度（lat）と経度（lon）の情報なので
print('東京の緯度:' + str(responseGeo[0]['lat']));
print('東京の経度:' + str(responseGeo[0]['lon']));

# OpenWeatherMapAPI
urlWeather = 'https://api.openweathermap.org/data/2.5/weather';
paramsWeather = {
    # 緯度
    'lat': responseGeo[0]['lat'],
    # 経度
    'lon': responseGeo[0]['lon'],
    'appid': API_TOKEN,
    # 日本語で取得
    'lang':'ja'
    # modeは指定しなければjson、htmlやxmlも選べる。
};
# APIリクエスト
# jsonで取得
# 得られた辞書型のデータを元に現在の天気などを表示する事が出来る。
responseWeather = requests.get(urlWeather, params=paramsWeather).json();
pprint.pprint(responseWeather);
print();



# ここからは便利なOpenWeatherMapのAPIのラッパーライブラリの設定
#  PyOWMのコンフィグ設定
config_dict = get_default_config()
config_dict["language"] = "ja"  # 取得データの言語設定

# PyOWMライブラリの初期化
owm = OWM(API_TOKEN, config_dict)
mgr = owm.weather_manager()

# 現在の気象データを取得
observation = mgr.weather_at_place("Tokyo,JP")

w = observation.weather
print("気象データの計測日次時間(unixTime): {}".format(w.ref_time))
print("気象データの計測日次時間(date): {}".format(formatting.to_date(w.ref_time)))
print("天気コード: {}".format(w.weather_code))
print("天気: {}".format(w.status))
print("天気詳細: {}".format(w.detailed_status))
print("気温(K): {}".format(w.temperature()))
print("気温(℃): {}".format(w.temperature("celsius")))
print("湿度(%): {}".format(w.humidity))
print("気圧(hPa): {}".format(w.barometric_pressure()))
print("風: {}".format(w.wind()))
print("雲量: {}".format(w.clouds))
print("雨量: {}".format(w.rain))
print("積雪量: {}".format(w.snow))
