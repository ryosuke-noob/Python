# from collections import deque

n = int(input())
a_list = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    b, m, e = map(int, input().split())
    tmp_swap = a_list[:]
    after_b = b + (e - m) % (e - b)
    a_list[b:after_b] = tmp_swap[m:e]
    a_list[after_b:e] = tmp_swap[b:m]
a_len = len(a_list)
for i, ai in enumerate(a_list):
    print(ai, end='')
    if i != a_len-1:
        print(' ', end='')
print('')