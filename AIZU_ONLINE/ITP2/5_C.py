import itertools

n = int(input())
args = list(map(int, input().split()))

perm = list(itertools.permutations(args, len(args)))
perm = sorted(perm)
i = perm.index(tuple(args))
if i > 0:
    print(*perm[i-1])
print(*perm[i])
if i < len(perm)-1:
    print(*perm[i+1])