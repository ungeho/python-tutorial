# http:docs.python.jp/3.5/library.tkinter.html
# Tool Kit Interface の略
# pythonでGUIアプリケーションを作る為の標準ライブラリ
import tkinter as tk
# メッセージボックス
import tkinter.messagebox as msg

# ベースとなる画面
base = tk.Tk();
# 立ち上がったウィンドウを隠す
base.withdraw();

# タイトル部分に大変！！！
# メッセージ部分に大丈夫ですか？
# と表示され、はい or いいえ　のボタンが表示される。
response = msg.askyesno('大変！！！', '大丈夫ですか？');

# ダイアログは以下の8種類が用意されている
# askokchansel:OK/キャンセル
# askquestion :はい/いいえ
# askretrycansel:再試行/キャンセル
# askyesno:はい/いいえ
# askyesnocansel:はい/いいえ/キャンセル
# showerror:エラーアイコンをメッセージを表示（ウィンドウをクローズする為のOKのみ）
# showinfo:インフォメーションアイコンとメッセージを表示（ウィンドウをクローズする為のOKのみ）
# showwarning:警告アイコンとメッセージを表示（ウィンドウをクローズする為のOKのみ）


# yesならTrue No ならFalse
if(response==True):
    print('大丈夫');
else:
    print('大丈夫ではない');

