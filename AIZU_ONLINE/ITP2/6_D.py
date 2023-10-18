import bisect

n = int(input())
array = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    key = int(input())
    l_index =bisect.bisect_left(array, key)
    r_index =bisect.bisect_left(array, key + 1)
    print(l_index, r_index)
