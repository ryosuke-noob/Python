# import numpy as np
import math
# from scipy.spatial.distance import chebyshev

n = int(input())
# for _ in range(0,n):
a = map(int, input().split())
b = map(int, input().split())
a = ([ai for ai in a])
b = ([bi for bi in b])

sum_1 = 0
sum_2 = 0
sum_3 = 0
sum__ = 0
# for ai, bi in a, b:
for i in range(0,n):
    sum_1 += abs((a[i] - b[i]))
    sum_2 += abs((a[i] - b[i])**2)
    sum_3 += abs((a[i] - b[i])**3)
    sum__ = max(abs(a[i] - b[i]), sum__)

print(sum_1)
print(math.pow(sum_2, 1/2))
print(math.pow(sum_3, 1/3))
print(sum__)