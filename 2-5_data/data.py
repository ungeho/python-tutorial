# 整数
print(34 + 56);
print();

# 浮動小数点数
print(5 + 3.4);
print(5 / 2);
print();


# 複素数
print((5 + 5j) + (3 + 1j));
print();


# 文字列型
print('Sunday\nMonday\nTuesday');
# 文字列の連結
print('thunder' + 'bolt');
# 同じ文字列を繰り返す
print('hunter' * 2);
# 文字列を全て大文字に変換
text = 'hello';
print(text.upper());
# 指定した文字の数を数える
word = 'maintenance';
print(word.count('n'));
print();


# 論理（bool）型
print(46 < 49);
print(46 > 49);
print();


# リスト型...[データ1, データ2, データ3]
# 数値型と文字列型をまとめられる。
apple = ['りんご', 57];
print(apple[0] + 'は' + str(apple[1] + 3) + '個');
Agroup = ['kazu', 'gorou'];
print(Agroup);
# append（追加）によってリストの後ろに要素を追加出来る。
Agroup.append('dai');
print(Agroup);
# removeによって指定した要素を削除
Agroup.remove('kazu');
print(Agroup);
# appendで再度'kazu'を後ろに追加し、sortで整列（アルファベット順）
Agroup.append('kazu');
print(Agroup);
Agroup.sort();
print(Agroup);
# 数字も整列可能
test_result = [87, 55, 99, 50, 66, 78];
test_result.sort();
print(test_result);
print();

# 辞書型...{見出し1:内容のデータ1, 見出し2:内容のデータ2, ....}
activities = {'Monday':'バスケ', 'Tuesday':'自転車', 'Wednesday':'軽音', 'Friday':'水泳'};
# 欲しいデータを見出しで指定出来る。
print(activities['Tuesday']);
print(activities['Friday']);
# keysメソッドを使うと、見出しとなるキーを全て表示出来る。
print(activities.keys());
# valuesメソッドを使うと、内容のデータを全て表示出来る。
print(activities.values());
print();

# タプル型（複数の要素からなる一組...2重（ダブル）,3重（トリプル）,4重（4タプル）,5重（5タプル）） .... (データ1, データ2, データ3, .....)
# 数値型と文字列型をまとめられる。
tuple_sample = ('apple', 3, 90, 90.4)
print(tuple_sample);
# リスト型との比較
# リストは要素を変更出来るが、タプルは出来ない。
flavor_list = ['ミント', 'チョコ', 'ストロベリー', 'バニラ'];
flavor_list[0] = 'ラムレーズン';
print(flavor_list);
flavor_tapple = ('ミント', 'チョコ', 'ストロベリー', 'バニラ');
# 下記の1行は、エラーが発生する。
# flavor_tapple[0] = 'ラムレーズン';
# 要素を変更出来ない性質により辞書型のkeyの設定にタプルを用いる事が出来る。
# 辞書のキーがころころ変わってしまうのは良くない為、変更できないデータ型のみをキーとして受け入れるようになっている。
# 辞書型の空データを定義
diary = {};
# タプルで見出し（key）を設定
key = ('kamata', '08-01');
# 同じ事をリスト型で行おうとするとエラーになる。
# key = ['nakata', '08-01'];
diary[key] = '70kg';
print(diary);
print();

# 集合（セット）型....{データ1, データ2, データ3, .....} あるいは　set(データ)
# 数値型と文字列型をまとめられる。
candy = {'delicious', 'fantastic'};
print(candy);
# set関数に文字列を渡すと、１文字ずつのバラバラになって要素が保存されている。
# 集合型は順番を保存しない為、完全にバラバラに保存される。
# また、集合型は同じデータ（重複するデータ）を持たない為、iが二つあるが保存されるiは一つのみになる。
candy = set('delicious');
print(candy);
print();

# set関数を使ってもバラバラにならないように定義
# リスト型で渡すとバラバラにならない。
flavor = ['apple', 'peach', 'soda'];
candy = set(flavor);
print(candy);
# 追加する時もupdateでリストで渡す事でバラバラにならない
candy.update(['grape']);
print(candy);
print()

# 集合型の便利な使い方：重複を削除
# 以下のリストはいくつか重複する要素が存在する。
flavor = ['apple', 'soda', 'chocolate', 'apple', 'grape', 'grape', 'soda'];
# set関数を通して集合型に変換する事で、重複する要素を削除する。
flavor_set = set(flavor);
print(flavor_set);
# 集合型をlist型に変換し、重複する要素を削除したリストを戻す
flavor = list(flavor_set);
# 重複する要素を削除したリストが得られる。
print(flavor);
print();

# 集合型を使った複数のデータ同士の計算
flavor_set_A = {'apple', 'peach', 'soda'};
flavor_set_B = {'apple', 'soda', 'chocolate'};
# flavor_set_Aの要素からflavor_set_Bの要素を除いたものを表示
print(flavor_set_A - flavor_set_B);
# flavor_set_A と flavor_set_B の共通する要素のみを表示
print(flavor_set_A & flavor_set_B);
# 集合型で使える機能
# A <= B BにAの全ての要素が含まれるか調べる（包含）
# B <= A AにBの全ての要素が含まれるか調べる
# A | B AとBに含まれる全ての要素を持った新しい集合型変数を生成　OR
# A & B AとB共通に含まれる要素を持った新しい集合型変数を生成 AND
# A - B Aには含まれるが、Bには含まれない要素を持った新しい集合型変数を生成
# A ^ B AとBのうち、どちらかにしか含まれない要素を持った新しい集合型変数を生成 XOR
