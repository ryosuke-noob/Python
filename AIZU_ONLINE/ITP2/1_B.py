q = int(input())
A = [0] * (2 * q + 1)
args = [[] for i in range(0,q)]
for i in range(0,q):
    args[i] = list(map(int, input().split()))
start = q + 1
end = q
for i in range(0,q):
    if args[i][0] == 0:
        if args[i][1] == 0:
            start -= 1
            A[start] = args[i][2]
        else:
            end += 1
            A[end] = args[i][2]
    elif args[i][0] == 1:
        p = args[i][1] + start
        print(A[p])
    else:
        if args[i][1] == 0:
            start += 1
        else:
            end -= 1

# map型オブジェクトはキャストによって簡単に自分の使いたい型に変換できるデータ型
# A.insert, A.popの計算量はどちらもO(n)であり，全体としてはO(n^2)となるため
# nが大きくなるとタイムアウトしてしまう．