from bisect import bisect_left, bisect_right, insort_left

q = int(input())
m = {}
keytbl = []
for _ in range(q):
    args = list(input().split())
    key = args[1]
    if args[0] == '0':
        if not key in m:
            insort_left(keytbl, key)
            m[key] = [int(args[2])]
        else:
            m[key].append(int(args[2]))
    if args[0] == '1':
        if key in m:
            for value in m[key]:
                print(value)
    if args[0] == '2':
        if key in m:
            m[key] = []
    if args[0] == '3':
        start = bisect_left(keytbl, args[1])
        end = bisect_right(keytbl, args[2], start)
        for i in range(start, end):
            if m[keytbl[i]] != []:
                for value in m[keytbl[i]]:
                    print(keytbl[i], value)
