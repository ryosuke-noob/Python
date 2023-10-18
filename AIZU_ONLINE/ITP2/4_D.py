n = int(input())
a_list = list(map(int, input().split()))

# ret_list = set(a_list)
# print(*ret_list)
# setは常に順番を維持するわけでもない．完全にランダム．
# したがってret_listをソートしてprintしなければならない

a_len = len(a_list)
for i in range(0,a_len):
    if i == 0:
        print(a_list[i],end='')
        continue
    if a_list[i-1] < a_list[i]:
        print('',a_list[i],end='')
print('')

# print(' '.join(map(str,a)))
# print(*sorted(list(set(a))))