from bisect import insort_left
from itertools import combinations

n = int(input())
T = list(map(int, input().split()))
k = T[0]
T = T[1:]

num_sets = []
for i in range(1, k+1):
    for comb in combinations(T,i):
        b = 0
        for shift in comb:
            b |= (1<<shift)
        insort_left(num_sets, (b, sorted(comb)))

print('0:')    
for b, num_set in num_sets:
    print(b, ': ', sep='', end='')
    print(*num_set)

# MOHEJIJN
# bit全探索

# n=int(input())
# l=list(map(int,input().split()))
# k=l[0]
# b=[0]*k
# for j in range(k):
#     b[j]=l[j+1]
# for i in range(1<<k):
#     sum=0
#     for j in range(k):
#         if (i>>j)&1:sum|=(1<<b[j])
#     print(sum,end='')
#     print(":",end='')
#     for j in range(n):
#         if (i>>j)&1:print(" ",b[j],sep='',end='')
#     print()
