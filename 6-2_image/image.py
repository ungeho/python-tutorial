# pip install Pillow
from PIL import Image

# 画像の読み込み
image = Image.open('image/flower.jpg');
# 画像の表示
# image.show();


# 色の変換
# 画像のrgb値を分けて格納する。
# 光の三原色（rgbが全て重なるのは白）
# split...分裂させる
r, g, b = image.split();
# merge...複数のものを混合させる
# 読み込んだRGB値のredとblueを入れ替えた画像を変数に格納
convert_image = Image.merge("RGB", (b, g, r));
# redとblueを入れ替えた画像を保存
convert_image.save('image/rgb_to_bgr.jpg');
# redとblueを入れ替えた画像を表示する
# convert_image.show();


# モノクローム画像（2値画像）
# 白 or 黒　の2値の画像に変換する
black_and_white = image.convert('1');
# black_and_white.show()
black_and_white.save('image/b_and_w.jpg')


# グレースケール画像
# 黒～白の濃淡のみに変換（輝度のみ）
# RGBのそれぞれの強さ（0~255）を元に、以下の計算式を使って変換される。
# L（輝度） = R（赤） * 0.299 + G（緑）* 0.587 + B（青） * 0.114
gray_image = image.convert('L');
# gray_image.show();
gray_image.save('image/gray_image.jpg');


# 画像の回転
image.transpose(Image.ROTATE_90).show();
image.transpose(Image.ROTATE_90).save('image/rotate_90.jpg');
# 変換の種類
# Image.FLIP_LEFT_RIGHT 画像の左右を反転 （flip...はじく、ひっくり返す）
# Image.FLIP_TOP_BOTTOM 画像の上下を反転
# Image.ROTATE_90       画像を90度回転
# Image.ROTATE_180      画像を180度回転
# Image.ROTATE_270      画像を270度回転
# 反時計回り