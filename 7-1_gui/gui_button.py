# http:docs.python.jp/3.5/library.tkinter.html
# Tool Kit Interface の略
# pythonでGUIアプリケーションを作る為の標準ライブラリ
import tkinter as tk

# ベースとなる画面
base = tk.Tk();

# ボタンを作成
# tk.部品のクラス（親となるインスタンス, 設定項目1=XXXX, 設定項目2=XXXX, .....）
# button1 = tk.Button(base, text='Push!');
# button2 = tk.Button(base, text='Push!');
# button3 = tk.Button(base, text='Push!');

# 部品を設置するメソッド
# 設置する位置や並べ方を指定する事も出来る。
# button1.pack();
# button2.pack();
# button3.pack();

# ボタンの幅や並びを指定する事も出来る。また、ボタンのインスタンス化と設置をまとめる事も出来る。
# 幅を指定した広いボタン1が最上位に設置され
# 左から設置したボタン2は左下に
# 右から設置したボタン3は右下に設置される。
# button1 = tk.Button(base, text='Push1', width=20).pack();
# button2 = tk.Button(base, text='Push2').pack(side=tk.LEFT);
# button3 = tk.Button(base, text='Push3').pack(side=tk.RIGHT);
# sideオプションで設定可能な並べ方
# tk.TOP 上から並べる（デフォルト）
# tk.LEFT 左から並べる
# tk.RIGHT 右から並べる
# tk.BOTTOM 下から並べる

# ボタン123の作成
# button1 = tk.Button(base, text='Push1');
# button2 = tk.Button(base, text='Push2');
# button3 = tk.Button(base, text='Push3');

# grid（格子）メソッドを使うと、部品を行（row）と列（column）で指定して設置できる。
# button1.grid(row=0, column=0);
# button2.grid(row=0, column=1);
# button3.grid(row=1, column=1);

# 設置位置を座標で指定したい場合は、placeメソッド
# xは左から何ピクセル離れているか
# yは上から何ピクセル離れているかを指定する。
# button1.place(x=0, y=0);
# button2.place(x=50, y=30);
# button3.place(x=100, y=60);

# 基本的にはpackとgridを使い、仕方ない時にplaceを使う


# ボタンを押した時の反応を作る。
def melon():
    # コンソール上で "MELON !" と表示
    print('MELON !');


# ボタンが押された時、commandに入れた関数名（push）の関数が呼ばれる。
button = tk.Button(base, text="WATAR", command=melon).pack()



# ベースとなる画面の表示を維持する。
# また、ベースとなる画面に置いた部品に対する操作、プログラムで書いた処理の画面への反映を受け付けている状態にしておくメソッド
base.mainloop();



