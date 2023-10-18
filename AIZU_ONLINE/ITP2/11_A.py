n = int(input())

print("0:")
for i in range(1, (1 << n)):
    elems = []
    x = i
    now_bit = 0
    while x > 0:
        if x % 2 == 1:
            elems.append(now_bit)
        now_bit += 1
        x = int(x / 2)
    print(f'{i}:', *elems)

# MOHEJIN
# n=int(input())
# for i in range(1<<n):
#     print(i,end='')
#     print(":",end='')
#     for j in range(n):
#         if (i>>j)&1:print(" ",j,sep='',end='')
#     print()
