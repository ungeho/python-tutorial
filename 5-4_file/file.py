# 標準ライブラリのosモジュール　環境変数の為に使用
import os


# open("ファイル名","モード")
# モードの種類
# r :read 指定したファイルを読み込む
# w :write 指定したファイルに新しく書き込む（上書き）
# a :append 指定したファイルに追記する
# r+:読み込み + 書き込み
# 何も指定しなかった場合は r となる。

# 上書きモードでファイルオブジェクトを開く（なければ新規作成）
file_object = open('python.txt','w');
# 内容を書き込む
file_object.write('this is sample of python.');
# 実際にファイルへの書き込みを実行する（ここまでの内容を実際に書き込むタイミングを任意に決める。）
# flushメソッドを使わなかった場合、closeした時には必ず書き込みが行われる。
file_object.flush();
# ファイルオブジェクトを閉じる
file_object.close()

# 読み込みモードでファイルオブジェクトを開く
file_object = open('python.txt','r');
# 内容の文字を変数に格納
str = file_object.read();
# ファイルオブジェクトを閉じる。
file_object.close();
print(str);

# 読み込みモードでファイルオブジェクトを開く
# 絶対パスでも指定する事が出来る。
file_object = open('C:\\Users\\' + os.environ['USERNAME'] +
                   '\\Documents\\GitHub\\python-tutorial\\5-4_file\\python.txt', 'r')
# 内容の文字を変数に格納
str = file_object.read()
# ファイルオブジェクトを閉じる。
file_object.close()
print(str)


# 追記モード
file_object = open('python.txt', 'a');
# 追加で文字の書き込みが行われる
file_object.write('Add data from program!!');
file_object.close();

# 読み込み+書き込み
file_object = open('python.txt', 'r+');
# ファイルの中身を読み込み出力
print(file_object.read());
# 返ってくる数字は書き込んだ文字の数
print(file_object.write('Add data from program!!'));
# ここでさらに読み込んだ場合、ファイルを読み込みを始める場所（シーク）が移動している為、空の文字列が返される。
# イメージ的には文字列を読み込む為のカーソルが一番左側にある状態。そこから右側の文字を読み取ろうとする為、空の文字列が返される。
print(file_object.read())
# 書き込んだ内容（全体）を確認する為には、seekメソッドをつあって、ファイルを読み込み始める場所を先頭に戻す。
file_object.seek(0);
# 書き込んだ内容を全て確認出来る。
print(file_object.read())
file_object.close();


# withを使ったファイルの書き込み（ファイルオブジェクトが自動的にcloseされるようにする）
# with open('ファイル名', 'モード') as ファイルオブジェクト名:
#      ファイルへの操作
with open('with.txt', 'w') as file_object:
    file_object.write('using with!');
# withのブロックを抜けると、ファイルオブジェクトが自動的にcloseされる。