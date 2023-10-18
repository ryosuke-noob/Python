def have_key(array : list, key : int) -> bool:
    a_len = len(array)
    start = 0
    end = a_len - 1
    while start <= end:
        a_len = end - start + 1
        mid = int(a_len / 2) + start
        if array[mid] < key:
            start = mid + 1
        elif array[mid] > key:
            end = mid - 1
        else: # array[mid] == key
            return True
    return False


n = int(input())
array = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    key = int(input())
    if have_key(array, key):
        print(1)
    else:
        print(0)
