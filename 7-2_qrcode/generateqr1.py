# QRコードを生成する外部ライブラリ
# https://pypi.python.org/pypi/qrcode

import qrcode

encode_text = 'http://google.com';

img = qrcode.make(encode_text);

print(type(img));

img.show();