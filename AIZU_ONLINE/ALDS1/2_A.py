def bubbleSort(array , n) -> int:
    swap_count = 0
    flag = 1
    while flag:
        flag = 0
        for j in range(n-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] #swap
                flag = 1
                swap_count += 1
    return swap_count

n = int(input())
array = list(map(int, input().split()))

swap_count = bubbleSort(array,n)
print(*array)
print(swap_count)