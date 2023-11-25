# http:docs.python.jp/3.5/library.tkinter.html
# Tool Kit Interface の略
# pythonでGUIアプリケーションを作る為の標準ライブラリ
import tkinter as tk

# ベースとなる画面
base = tk.Tk()

def supermode():
    print('super mode!');

# ベース画面にメニューを設置する。
# また、menubarはメニューの項目を置く場所で、メニュー部分に置かれる部品にとってはbaseに相当する。
menubar = tk.Menu(base);
# menubarを元に、filemenuオブジェクトを生成する。
filemenu = tk.Menu(menubar);
# メニューをクリックしたときに表示される項目を追加する。
# ラベルは表記上の文字列
# クリックされた時の処理はcommandで指定された関数(supermode)が呼ばれる
filemenu.add_command(label='supermode', command=supermode);
# filemenuをメニューバーに関連づける。
menubar.add_cascade(label='Operation', menu=filemenu);
# base画面のmenuとしてmenubarを設置
base.config(menu=menubar)



# ベースとなる画面の表示を維持する。
# また、ベースとなる画面に置いた部品に対する操作、プログラムで書いた処理の画面への反映を受け付けている状態にしておくメソッド
base.mainloop()
