q = int(input())
fr = []
sc = []
for i in range(q):
    args = list(map(int,input().split()))
    if args[0] == 0:
        sc.append(args[1])
    elif args[0] == 1:
        d = args[1]
        if d > 0:
            for j in range(d):
                fr.append(sc[-1])
                sc.pop()
        else:
            for j in range(-d):
                sc.append(fr[-1])
                fr.pop()
    else:
        sc.pop()

for x in fr:
    print(x)
for x in reversed(sc):
    print(x)
# map型オブジェクトはキャストによって簡単に自分の使いたい型に変換できるデータ型
# A.insert, A.popの計算量はどちらもO(n)であり，全体としてはO(n^2)となるため
# nが大きくなるとタイムアウトしてしまう．