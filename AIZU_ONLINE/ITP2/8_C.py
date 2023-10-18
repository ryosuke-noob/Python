from bisect import bisect_left, bisect_right, insort_left

q = int(input())
m = {}
keytbl = []
for _ in range(q):
    args = list(input().split())
    key = args[1]
    if args[0] == '0':
        if not key in keytbl:
            insort_left(keytbl, key)
        m[key] = int(args[2])
    if args[0] == '1':
        print(m[key] if key in m else 0)
        # if key in m:
        #     print(m[key])
        # else:
        #     print(0)
    if args[0] == '2':
        if key in m:
            m[key] = 0
    if args[0] == '3':
        start = bisect_left(keytbl, args[1])
        end = bisect_right(keytbl, args[2], start)
        for i in range(start, end):
            if m[keytbl[i]] > 0:
                print(keytbl[i], m[keytbl[i]])

# 10行目の
# if key not in keytbl(list型)
# を
# if key not in m(dict型)
# とすることで探索が早くなる