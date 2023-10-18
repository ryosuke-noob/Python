import math

def is_prime(n : int) -> bool:
    n_sqrt = math.sqrt(n)
    ceil = min(n - 1, math.ceil(n_sqrt))
    for i in range(2, ceil + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
p_cnt = 0
for _ in range(n):
    num = int(input())
    if is_prime(num):
        p_cnt += 1
print(p_cnt)
