from math import ceil

def insertionSort(A, n, g) -> int:
    cnt = 0
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v
    return cnt

def shellSort(A, n):
    cnt = 0
    m = 1
    G = [1]
    for i in range(2, n):
        g = int(((3**i)-1)/2) #shellSortではgの取り方がある程度決まっている．
        if g > ceil(n / 3):
            m = i - 1
            break
        G.append(g)
    G.reverse()
    for i in range(m):
        cnt += insertionSort(A, n, G[i])
    
    print(m)
    print(*G)
    print(cnt)

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))

shellSort(A, n)

for i in range(n):
    print(A[i])
