n = int(input())
a_list = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    b, e = map(int, input().split())
    a_len = len(a_list)
    tmp_swap = a_list[b:e]
    a_list[b:e] = tmp_swap[::-1]
a_len = len(a_list)
for i, ai in enumerate(a_list):
    print(ai, end='')
    if i != a_len-1:
        print(' ', end='')
print('')