# 関数の定義
def washingMachine(mode):
    print('給水します。');
    if(mode == 'soft'):
        print('やさしく洗う');
    elif(mode == 'hard'):
        print('激しく洗う');
    else:
        print('普通に洗う');

# 円の面積を計算する関数
def area(radius):
    result = radius * radius * 3.14;
    return result;

# 関数の呼び出し
washingMachine('soft');
print();
print(area(5));
print();

# 既に組み込まれている関数
# 文字数を数える len()
print(len('thunderbolt'));
# 要素の数を数える len()
animal = ['cat','dog','duck'];
print(len(animal));
print();
# 最大値、最小値 max(),min()
print(max(100,10,50));
print(min(300,30,3000));
# 文字列にも対応
# maxの場合、最もzに近い文字を返す。（minであれば最もaに近い文字）
# 優先順位は： min <- 数字 , 大文字英字(A-Z) , 小文字英字(a-z) -> max
print(max('thunderbolt'));
print();
# 整列: sorted()
# 渡したデータを並べ替えてリストで返してくれる。
# 優先順位はmin,maxと同様に：  数字  大文字英字(A-Z)  小文字英字(a-z) の順に並び替える
print(sorted('1Aa'));
print(sorted([100, 95, 55, 98, 78, 80, 78]));
print();
# 表示する print()
print('Hello World!');
print()
# データの型を調べる type()
# 使いたい変数の型がわからない時に便利。
hatena_1 = 9800;
print(type(hatena_1));
hatena_2 = 'marshmallow'
print(type(hatena_2))
hatena_3 = ['osomatsu', 'karamatsu']
print(type(hatena_3))
print();

# メソッドの表示 dir()
string = 'nikuman';
# データ型の種類に応じた便利なメソッドをリファレンスを参照しなくとも思い出すきっかけを作る。
# 文字列型を渡すと、文字列型のメソッドが確認出来る。使えそうなメソッドを探すきっかけになる。
print(dir(string));
# dir関数に何も渡さずに表示すると、dir()が実行された場所で有効なデータのリストを表示出来る。
# 迷子になった時に便利
print(dir());