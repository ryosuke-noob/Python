import math
a, b, c = map(float, input().split())
c = math.pi / 180 * c
S = 1/2 * math.sin(c) * a * b
L = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(c)) + a + b
h = S / a * 2
print(S, L, h)
# print(math.sin(c))