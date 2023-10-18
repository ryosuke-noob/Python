n = int(input())
arg = map(int, input().split())
ilist = []
for i in arg:
    ilist.append(i)
print(ilist[n - 1], end='')
for i in range(n - 2, -1, -1):
    print('', ilist[i], end='')
print('')