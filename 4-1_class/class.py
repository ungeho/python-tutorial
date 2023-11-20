# class クラス名
#   変数の定義（メンバ変数）
#   関数の定義（メソッド）

# クラス（設計図）の定義
class fruit:
    color = 'red';
    # pythonではメソッドの第一引数に必ずselfが必要
    def taste(self):
        return 'delicious';

# __init__メソッド
# 使う数値などを初期設定のように最初に定義したり
# インスタンス化するときに引数を渡して定義することを必須にする。
# class クラス名:
#   def __init__(self, 引数, ....):
#       self.初期設定したい変数 = 引数
#       最初に行いたい処理
#   def メソッド名
#       メソッドの処理

# 従業員クラス
class staff:
    # 引数bonusを必須にする。
    def __init__(self, bonus):
        self.bonus = bonus;
    # クラスの中で定義された変数は、selfの中にある。
    def salary(self):
        # self.bonusとすることで参照できる。
        salary = 10000 + self.bonus;
        return salary;




# fruitクラスのインスタンス化（組み立て）
apple = fruit();
print(apple.color);
print(apple.taste());
print();

# オブジェクト
# pythonの場合はオブジェクトはデータ型を言い換える事も出来る
# 文字列型のデータと
color = "green";
# 文字列型のメソッドを備えた文字列型オブジェクト
print(color.count('e'));
print(color.upper());
print();

# stuffクラスのインスタンス化
yamamoto = staff(50000)
print(yamamoto.salary());
