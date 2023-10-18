def culc_gcd(x : int, y : int) -> int:
    if x < y:
        tmp = x
        x = y
        y = tmp
    if x % y == 0:
        return y
    ret = culc_gcd(y, x % y)
    return ret

x, y = map(int, input().split())
print(culc_gcd(x, y))