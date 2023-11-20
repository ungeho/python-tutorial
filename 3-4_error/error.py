# 例外処理
# try:
    # 処理A（エラーが発生するかもしれない処理）
# except:
    # 処理B（想定されたエラーをキャッチした時の処理）


try:
    # 構文エラー
    prin('例外が発生してしまう処理');
except:
    print('例外をキャッチしました。');
print('');

# 例外の内容を例外処理で取得する
try:
    prin('a');
# exception型の例外をキャッチして、キャッチしたデータを変数eにセットする。
except Exception as e:
    # prinは定義されていないと表示される。
    print(e.args);