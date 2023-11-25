# QRコードを生成する外部ライブラリ
# https://pypi.python.org/pypi/qrcode

import qrcode as qr
import tkinter as tk
import tkinter.filedialog as fd
# 画像をtkinterで使える形に変換する為に使う
from PIL import ImageTk

# ベースとなるウィンドウ
base = tk.Tk();
# ウィンドウのタイトル
base.title('QRcode Generator');

# url入力用のフレーム（部品）を生成
# 他の部品をひとまとめに置いておくことが出来る
# reliefはフレームの枠の種類（直線で囲む、盛り上がっている、凹んでいるなど）
# bdはborderwidthの略、フレームの幅
input_area = tk.Frame(base, relief=tk.RAISED, bd=2);
# qr画像出力用のフレーム（部品）を生成
image_area = tk.Frame(base, relief=tk.SUNKEN, bd=2);

# qrコードにするurl(文字列)を保持する変数
encode_text = tk.StringVar();

# 文字の入力エリアを左から生成
# 設置場所はurl入力用のフレームの為、この時点ではベースウィンドウには表示されない。
entry = tk.Entry(input_area, textvariable=encode_text).pack(side = tk.LEFT);

# QRコードを表示する為のラベル
# 設置場所はqr画像出力用のフレーム
qr_label = tk.Label(image_area);

# QRコードを生成する為の関数
def generate():
    # 入力された文字列をQRコードに変換し、変数に保存する。
    qr_label.qr_img = qr.make(encode_text.get());
    # QRコードのイメージサイズを変数に格納。
    img_width, img_height = qr_label.qr_img.size;
    # qrコードへの変換によって得られた画像を、tkで扱える形に変換する。
    qr_label.tk_img = ImageTk.PhotoImage(qr_label.qr_img);
    qr_label.config(image=qr_label.tk_img,width=img_width,height=img_height);
    # 生成されたQR画像がqrコード出力用のフレームに設置される。
    qr_label.pack();

# ボタンをurl入力用のフレームに設置
# 押されるとgenerate関数を呼び出す。
encode_button = tk.Button(input_area, text='QRcode!',command=generate).pack(side=tk.LEFT);
# フレームを描画（設置）する。
input_area.pack(pady=5);
image_area.pack(padx=3, pady=1);

# メニューのsaveが押されたら呼ばれる関数
def save():
    # ファイルを保存する為の画像が開き、名前を付けて保存する。
    # initialfileは初期値の保存ファイル名
    filename = fd.asksaveasfilename(title='名前を付けて保存する', initialfile='qrcode.png');
    # filenameが入力されている時（保存するファイル名が何も入力されてない場合はFalse）　かつ
    # hasattr関数は第一引数に第二引数のattributeが存在する場合はTrue、存在しない場合はFalse
    # qr_labelに文字列、'qr_img'が存在するかどうかの確認。
    # qr_imgはgenerate関数を通して初めて生成される。
    # qr画像を生成していないのにsaveをしようとするとエラーになる為、それを回避する（何も行わない）のための条件
    if filename and hasattr(qr_label, 'qr_img'):
        qr_label.qr_img.save(filename);

# メニューのexitが押されたら終了する
def exit():
    base.destroy();

menubar = tk.Menu(base);
filemenu = tk.Menu(menubar);
menubar.add_cascade(label='File', menu=filemenu);
filemenu.add_command(label='save', command=save);
filemenu.add_separator()
filemenu.add_command(label='exit', command=exit);
base.config(menu=menubar);

# ウィンドウを表示させ続ける。
base.mainloop();
