# 継承(inheritance)
# 親クラスから子クラスへデータやメソッドを受け継がせる

# 継承の書き方（子クラス）
# 親クラスは通常通りのクラスの書き方
# class クラス名(親クラス名):
#   変数
#   def メソッド名:
#       メソッドの処理

# 親クラス 動物の基本形
class animalBaseClass:
    # 脚の本数の指定を必須にする。
    def __init__(self, num):
        self.animallegs = num;
    # 歩く機能を持つ
    def walk(self):
        print('あるく');
    # 鳴く機能を持つ
    def cry(self):
        print('なく');
    # 脚の本数を取得するメソッド
    def getLegsNum(self):
        print(self.animallegs);

# 子クラス 犬のクラス
class dogClass(animalBaseClass):
    # 脚の本数の指定を必須にする。
    def __init__(self, num):
        # super(子クラス名, インスタンス)
        # 親クラスのオブジェクトを変数に格納
        parent_class = super(dogClass, self)
        # 犬親クラスの初期化メソッドにnumを渡す。
        parent_class.__init__(num)
        print('いぬです。');

# 子クラス 犬のクラス
# 親クラスから継承し、脚の本数と鳴き方を上書き
class birdClass(animalBaseClass):
    def __init__(self, num):
        parent_class = super(birdClass, self)
        parent_class.__init__(num)
        print('とりです。');
    # メソッドのオーバーライド（上書き）
    def cry(self):
        print('ぴよぴよ');

# 初期化メソッドの値（脚の数）が基本的に変わらないなら以下のように書く事も出来る
# 蛇のクラス
class snakeClass(animalBaseClass):
    def __init__(self):
        # 蛇の足の数は基本的に0本で変わらないため、引数を取らずに設定。
        snake_legs = 0;
        parent_class = super(snakeClass, self);
        parent_class.__init__(snake_legs);
        print('へびです。');



# 子クラスには記載してないメソッドも利用出来る
# 犬のインスタンス化
wanko = dogClass(4);
wanko.walk();
wanko.cry();
wanko.getLegsNum();

piyo_suke = birdClass(2);
piyo_suke.walk();
piyo_suke.cry();
piyo_suke.getLegsNum();


nyoro = snakeClass();
nyoro.getLegsNum();