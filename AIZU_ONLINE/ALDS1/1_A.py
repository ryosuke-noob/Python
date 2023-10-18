def my_insertionSort(A, N):
    print(*A)
    for i in range(1,N):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v: #挿入したい要素より大きい要素は配列の後ろに送る
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
        print(*A)


n = int(input())
a = list(map(int, input().split()))
my_insertionSort(a, n)

# insetionSort
# O(n^2)
# O(n) if list sorted