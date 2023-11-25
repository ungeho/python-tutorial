# http:docs.python.jp/3.5/library.tkinter.html
# Tool Kit Interface の略
# pythonでGUIアプリケーションを作る為の標準ライブラリ
import tkinter as tk
import tkinter.filedialog as fd

# ベースとなる画面
base = tk.Tk()

def open():
    # 選択したファイル名と場所を表示
    filename = fd.askopenfilename()
    print('open file => ' + filename);

def exit():
    # ウィンドウを閉じる
    base.destroy();


def find():
    print('find !');



menubar = tk.Menu(base);
filemenu = tk.Menu(menubar);
menubar.add_cascade(label='File' ,menu=filemenu);
filemenu.add_command(label='open',command=open);
# ファイルの項目に罫線を入れる。
filemenu.add_separator();
filemenu.add_command(label='exit', command=exit);
editmenu= tk.Menu(menubar);
menubar.add_cascade(label='Edit', menu=editmenu);
editmenu.add_command(label='find', command=find);
base.config(menu=menubar);




# ベースとなる画面の表示を維持する。
# また、ベースとなる画面に置いた部品に対する操作、プログラムで書いた処理の画面への反映を受け付けている状態にしておくメソッド
base.mainloop()
