n = int(input())
# str = "1 2 3 4 5"
# print(str.split())
num = map(int, input().split())
sum = 0
mi = 1000000
ma = -1000000
for i in num:
    mi = min(mi, i)
    ma = max(ma, i)
    sum += i
print(mi, ma, sum)