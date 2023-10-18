alist = []
blist = []

while(1):
    a, b = input().split()
    a, b = int(a), int(b)
    if a == 0 and b == 0:
        break
    # alist.append(a)
    # blist.append(b)
    print(min(a, b), max(a, b))

# for i in range(0, len(alist)):
#     print(blist[i], alist[i])