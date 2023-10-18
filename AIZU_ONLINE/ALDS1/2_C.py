def bubbleSort(C, N) -> None:
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j][1] < C[j-1][1]:
                C[j], C[j-1] = C[j-1], C[j]

def selectionSort(C, N) -> None:
    for i in range(N):
        min_j = i
        for j in range(i, N):
            if C[j][1] < C[min_j][1]:
                min_j = j
        if i != min_j:
            C[i], C[min_j] = C[min_j], C[i]

n = int(input())
args = input().split()
bubble_array = args[:]
selection_array = args[:]
bubbleSort(bubble_array, n)
print(*bubble_array)
print("Stable")
selectionSort(selection_array, n)
print(*selection_array)
if selection_array == bubble_array:
    print("Stable")
else:
    print("Not stable")