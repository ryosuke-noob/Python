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

def includes(a : list, b : list) -> bool:
    for key in b:
        if have_key(a, key):
            pass
        else:
            return False
    return True

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
if includes(a, b):
    print(1)
else:
    print(0)