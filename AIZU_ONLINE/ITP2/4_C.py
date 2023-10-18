# from collections import deque

n = int(input())
a_list = list(map(int, input().split()))
q = int(input())
a_len = len(a_list)
for _ in range(q):
    b, e, t = map(int, input().split())
    tmp_swap = a_list[:]
    after_b = (b + (t - b)) % a_len
    after_e = (e + (t - b)) % a_len
    if after_b < after_e:
        a_list[after_b:after_e] = tmp_swap[b:e]
        a_list[b:e] = tmp_swap[after_b:after_e]
    else:
        a_list[after_b:a_len] = tmp_swap[b:b + a_len - after_b]
        a_list[0:after_e] = tmp_swap[b + a_len - after_b:e]
        a_list[b:b + a_len - after_b] = tmp_swap[after_b:a_len]
        a_list[b + a_len - after_b:e] = tmp_swap[0:after_e]
    # print(a_list)

for i, ai in enumerate(a_list):
    print(ai, end='')
    if i != a_len-1:
        print(' ', end='')
print('')