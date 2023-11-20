# オンライン標準ライブラリのドキュメント
# python3
# http://docs.python.jp/3.5/library/index.html
# python2
# http://docs.python.jp/2.7/library/index.html

# calenderライブラリのimport
# asを使う事で、calendarライブラリを呼び出す時の名称をcalに省略
import calendar as cal
# from パッケージ名（モジュール名） import モジュール名（クラス名、関数など）
# fromを使う事で、メソッドがどこから呼ばれるかはっきりするため、モジュール名を書かずに呼び出せる。
from calendar import month, isleap

print(cal.month(2015, 8));

print(month(2015,9));

print(isleap(2012));

print();

# 今日の日付を取得
# datetimeモジュールのドキュメント
# http://docs.python.jp/3.5/library/datetime.html
# http://docs.python.jp/2.7/library/datetime.html
from datetime import date
today = date.today();
print(today.strftime('%Y年%m月%d日'));
print();
# 日付の形式
# %Y 年を西暦の4桁で表示
# %y 年を西暦の2桁で表示
# %m 月を2桁で表示
# %B 英語で月名を表示
# %b 英語で月名を短縮して表示
# %A 英語で曜日名を表示
# %a 英語で曜日名を短縮して表示

# 現在の日付を時刻を取得
from datetime import datetime as dt
now = dt.now();
print(now.strftime('%Y-%m-%d %H:%M:%S'));
print();
# 時間の形式
# %H 時を24時間表記で表示
# %I 時を12時間表記で表示
# %p 時刻がAMとPMのどちらかであるかを表示
# %M 分を2桁の数字で表示
# %S 秒を2桁の数字で表示

# 一週間後の日付を取得
from datetime import date, timedelta
today = date.today()
print(today);
# 七日分の時間を変数に
one_week = timedelta(days = 7);
# 七日後の日付
print(today + one_week);
# 七日前の日付
print(today - one_week);
print();

# zipファイルを作ったり解凍したり
# zipfileドキュメント
# http://docs.python.jp/3.5/library/zipfile.html
# http://docs.python.jp/2.7/library/zipfile.html
import zipfile
# zipファイルを指定
files = zipfile.ZipFile('aaa.zip');
# zipの中身を閲覧
print(files.namelist());
# 指定したものだけ解凍（files.namelistで返ってきたリストの要素と同じ形式で指定する。）
# files.extract('aaa/ccc.txt')
# 中身を全て解凍
files.extractall();
# zipfileオブジェクトを終了
files.close();

# ファイルを圧縮
# zipfile.ZipFile('圧縮後のファイル名', mode='w');
zip_file = zipfile.ZipFile('empty_txt.zip', mode='w');
# 第一引数で指定したものを第二引数で名前を指定して圧縮
zip_file.write('./aaa/ccc.txt', 'ddd.txt');
zip_file.close();
# 圧縮したものの中身を確認
file = zipfile.ZipFile('empty_txt.zip');
print(file.namelist());
