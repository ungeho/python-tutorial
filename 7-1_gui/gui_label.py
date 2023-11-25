# http:docs.python.jp/3.5/library.tkinter.html
# Tool Kit Interface の略
# pythonでGUIアプリケーションを作る為の標準ライブラリ
import tkinter as tk

# ベースとなる画面
base = tk.Tk()

# ラベルは文字を表示する為の部品
# 文字と背景色、幅を指定して設置している。
# bgはbackground（背景）の略、16進数で色を表現するカラーコードも指定できる。
tk.Label(base, text='赤', bg='red', width=20).pack();
tk.Label(base, text='緑', bg='green', width=20).pack();
tk.Label(base, text='青', bg='blue', width=20).pack();


# ベースとなる画面の表示を維持する。
# また、ベースとなる画面に置いた部品に対する操作、プログラムで書いた処理の画面への反映を受け付けている状態にしておくメソッド
base.mainloop()
