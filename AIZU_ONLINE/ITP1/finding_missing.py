# init
slist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
hlist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
clist = [1,2,3,4,5,6,7,8,9,10,11,12,13]
dlist = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# action
n = int(input())
for i in range(0,n):
    suit, rank = input().split()
    rank = int(rank)
    if suit == 'S':
        slist.remove(rank)
    if suit == 'H':
        hlist.remove(rank)
    if suit == 'C':
        clist.remove(rank)
    if suit == 'D':
        dlist.remove(rank)
for i in range(0, len(slist)):
    print('S',slist[i])
for i in range(0, len(hlist)):
    print('H',hlist[i])
for i in range(0, len(clist)):
    print('C',clist[i])
for i in range(0, len(dlist)):
    print('D',dlist[i])

