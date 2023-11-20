counter = 0;
while(counter < 5):
    print(counter)
    counter += 1;
print();

# 無限ループとbreak
power = 2;
while(True):
    print('パンチ');
    print('キック');
    print('必殺奥義');
    power -= power;
    # 条件を満たしたらbreakで無限ループから抜ける
    if(power == 0):
        break
print();

# continue 処理をスキップ
family = ['ryu-ko', 'mako', 'satsuki']
for kid in family:
    print('おはよう！' + kid);
    print('起床');
    print('朝ごはん');
    # 条件を満たした場合、スキップして次のループへ
    if(kid == 'mako'):
        continue
    print('学校に出発');