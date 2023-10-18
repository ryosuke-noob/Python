from bisect import insort_left
from itertools import combinations

n, k = map(int,input().split())
T = [i for i in range(n)]

num_sets = []
for comb in combinations(T,k):
    b = 0
    for shift in comb:
        b |= (1<<shift)
    insort_left(num_sets, (b, sorted(comb)))

for b, num_set in num_sets:
    print(b, ': ', sep='', end='')
    print(*num_set)

