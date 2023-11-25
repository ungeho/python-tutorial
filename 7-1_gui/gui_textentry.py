# http:docs.python.jp/3.5/library.tkinter.html
# Tool Kit Interface の略
# pythonでGUIアプリケーションを作る為の標準ライブラリ
import tkinter as tk

# ベースとなる画面
base = tk.Tk();

# 文字列のみを扱うオブジェクト
string = tk.StringVar();

# テキスト入力欄を生成する
entry = tk.Entry(base, textvariable=string).pack();
# ラベルを生成する
label = tk.Label(base, textvariable=string).pack();
# 結果、テキスト入力欄に入力したものが、そのままラベルの文字に反映される。


# ベースとなる画面の表示を維持する。
# また、ベースとなる画面に置いた部品に対する操作、プログラムで書いた処理の画面への反映を受け付けている状態にしておくメソッド
base.mainloop();
