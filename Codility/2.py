# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def size_of_triangle(a, b, c):
    if a + b <= c:
        return -1
    if b + c <= a:
        return -1
    if c + a <= b:
        return -1
    return a + b + c

def solution(A):
    a_len = len(A)
    if a_len > 100000:
        return -1
    max_size = -1
    for i in range(0,a_len-2):
        for j in range(i+1, a_len-1):
            for k in range(j+1,a_len):
                max_size = max(max_size, size_of_triangle(A[i],A[j],A[k]))
    return max_size