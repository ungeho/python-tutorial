# ファイルを直接実行する時、__name__には'__main__'が入っている。
# それを利用して、importした時には読み込まれないようにする
if __name__ == '__main__':
    print('happy new year3 !!')