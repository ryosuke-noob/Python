n = int(input())
T = list(map(int, input().split()))
if T[0] == 0:
    print("0:")
T = set(T[1:])

for i in range(1, (1 << n)):
    elems = []
    x = i
    now_bit = 0
    while x > 0:
        if x % 2 == 1:
            elems.append(now_bit)
        now_bit += 1
        x = int(x / 2)
    flag = 1
    for elemT in T:
        if elemT not in elems:
            flag = 0
    if flag == 1:
        print(f'{i}:', *elems)

# MOHEJIN
# n=int(input())
# l=list(map(int,input().split()))
# k=l[0]
# b=0
# for j in range(k):
#     b|=(1<<l[j+1])
# for i in range(1<<n):
#     if i&b!=b:continue
#     print(i,end='')
#     print(":",end='')
#     for j in range(n):
#         if (i>>j)&1:print(" ",j,sep='',end='')
#     print()
