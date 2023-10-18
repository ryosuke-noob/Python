str = input()
a, b, c = str.split()

a = int(a)
b = int(b)
c = int(c)

sum = a + b + c
min = min(a, b, c)
max = max(a, b, c)
print(min, sum - min - max, max)