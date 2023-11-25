# http:docs.python.jp/3.5/library.tkinter.html
# Tool Kit Interface の略
# pythonでGUIアプリケーションを作る為の標準ライブラリ
import tkinter as tk

# ベースとなる画面
base = tk.Tk()

# ラジオボタンは複数ある項目のうち、一つだけを選択させるボタン
# 整数のみの値を取るクラスを格納
radio_value = tk.IntVar();
# 初期値を1（Bランチ）とする。
radio_value.set(1);
# ランチメニュー
lunch = {0:'Aランチ', 1:'Bランチ', 2:'Cランチ'};

# ランチメニューの数だけラジオボタンを設置



for i in range(len(lunch)):
    # variableに初期値
    # また、選択されている時にvalueの値がradio_valueに入る。
    tk.Radiobutton(base, text = lunch[i], variable = radio_value, value = i).pack();

def buy():
    print(lunch[radio_value.get()]);

# ボタンが押されたらbuy関数を実行
tk.Button(base, text='注文', command=buy).pack();


# ベースとなる画面の表示を維持する。
# また、ベースとなる画面に置いた部品に対する操作、プログラムで書いた処理の画面への反映を受け付けている状態にしておくメソッド
base.mainloop()
