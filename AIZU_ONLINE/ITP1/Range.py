str = input()
a, b, c = str.split()

a = int(a)
b = int(b)
c = int(c)

if a < b < c:
    print("Yes")
else:
	print("No")