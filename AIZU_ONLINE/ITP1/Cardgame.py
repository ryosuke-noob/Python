n = int(input())
a_count = 0
b_count = 0
for _ in range(0,n):
    a, b = input().split()
    if a < b:
        b_count += 3
    elif a > b:
        a_count += 3
    else:
        a_count += 1
        b_count += 1
print(a_count, b_count)