# http:docs.python.jp/3.5/library.tkinter.html
# Tool Kit Interface の略
# pythonでGUIアプリケーションを作る為の標準ライブラリ
import tkinter as tk

# ベースとなる画面
base = tk.Tk();

topping = {0:'ノリ', 1:'煮玉子', 2:'もやし', 3:'チャーシュー'};
check_value = {};

# トッピングの数だけ繰り返す
for i in range(len(topping)):
    # True か False のみの値を取るクラスを格納する。
    # set や get メソッドで操作する事が出来る。
    check_value[i] = tk.BooleanVar();
    # トッピングの数だけチェックボタンを生成し、対応したトッピング名を表示する。
    # チェックボタンの状態を格納する変数はcheck_value[i]
    # anchorはbaseとなる画面（window）のどちら寄りに配置するかで、指定は左に寄せる（WはWestの略）
    tk.Checkbutton(base, variable = check_value[i], text = topping[i]).pack(anchor=tk.W);

# check_valueの値を取ってきて、Trueの場合、その順に対応したトッピングを表示する。
def buy():
    for i in check_value:
        if check_value[i].get() == True:
            print(topping[i]);

# ボタンが押されると関数buyが呼ばれる
tk.Button(base, text='注文', command=(buy)).pack();

# ベースとなる画面の表示を維持する。
# また、ベースとなる画面に置いた部品に対する操作、プログラムで書いた処理の画面への反映を受け付けている状態にしておくメソッド
base.mainloop();
