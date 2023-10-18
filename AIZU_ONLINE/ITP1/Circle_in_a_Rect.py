str = input()
w, h, x, y, r = str.split()

w = int(w)
h = int(h)
x = int(x)
y = int(y)
r = int(r)

if (x - r < 0 or x + r > w):
    print("No")
elif (y - r < 0 or y + r > h):
    print("No")
else:
    print("Yes")
