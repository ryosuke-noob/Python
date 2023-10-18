import itertools

n = int(input())
nums = [i for i in range(1,n+1)]

perm = list(itertools.permutations(nums, n))
perm = sorted(perm)
for elem in perm:
    print(*elem)