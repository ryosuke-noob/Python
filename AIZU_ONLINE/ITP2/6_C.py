def get_index(array : list, key : int) -> int:
    a_len = len(array)
    if array[a_len-1] < key:
        return a_len
    start = 0
    end = a_len - 1
    while a_len > 10:
        a_len = end - start + 1
        mid = int(a_len / 2) + start
        if array[mid] < key:
            start = mid
        elif array[mid] >= key:
            end = mid
    for index in range(start, end + 1):
        if array[index] >= key:
            return index
    return -1


# n = int(input())
# array = list(map(int, input().split()))
# q = int(input())
# for _ in range(q):
#     key = int(input())
#     print(get_index(array, key))

# solution
import bisect
n = int(input())
array = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    key = int(input())
    print(bisect.bisect_left(array, key))
