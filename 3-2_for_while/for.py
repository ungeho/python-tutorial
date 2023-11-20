# 0~2までの繰り返し、繰り返しの番号はcountに入る。
for count in range(3):
    print('繰り返します');
    print(count);
print();

# forを使った文字列の繰り返し
# for 変数 in データ
# foreachのような挙動。先頭から1文字ずつ変数に格納して最後の文字まで繰り返す
word = 'ninja';
for chara in word:
    print(chara);
print();

# forを使ったリスト型の繰り返し
# for 変数 in データ
# 先頭の要素から順に変数に格納される。
music_list = ['DEATH METAL', 'ROCK', 'ANIME', 'POP'];
for music in music_list:
    print('now playing... ' + music);
print();

# forを使った辞書型の繰り返し
# for 変数 in データ
# 先頭の見出し（key）から順に変数に格納される。
menu = {'ラーメン':500, 'チャーハン':430, '餃子':210}
for order in menu:
    print(order);
    print(menu[order] * 1.08);