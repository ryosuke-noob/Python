n, q = map(int,input().split())
A = [[] for _ in range(n)]
args = [[] for i in range(0,q)]
for i in range(0,q):
    args[i] = list(map(int, input().split()))
for i in range(0,q):
    if args[i][0] == 0:
            A[args[i][1]].append(args[i][2])
    elif args[i][0] == 1:
         length = len(A[args[i][1]])
         if length == 0:
            print('')
            continue
         for i, c in enumerate(A[args[i][1]]):
            if i != length - 1:
                print(c, end=' ')
            else:
                print(c)
    else:
        A[args[i][1]].clear()

# map型オブジェクトはキャストによって簡単に自分の使いたい型に変換できるデータ型
# A.insert, A.popの計算量はどちらもO(n)であり，全体としてはO(n^2)となるため
# nが大きくなるとタイムアウトしてしまう．