def selectionSort(A, N) -> int:
    swap_count = 0
    for i in range(N):
        min_j = i
        for j in range(i, N):
            if A[j] < A[min_j]:
                min_j = j
        if i != min_j:
            A[i], A[min_j] = A[min_j], A[i]
            swap_count += 1
    return swap_count

n = int(input())
array = list(map(int, input().split()))

swap_count = selectionSort(array,n)
print(*array)
print(swap_count)