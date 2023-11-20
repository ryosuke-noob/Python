# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    max_len = max(len(A), 200000)
    count = 1
    index = 0
    while A[index] != -1:
        index = A[index]
        count += 1
        if count > max_len:
            break
    return count

solution([1, 4, -1, 3, 2])