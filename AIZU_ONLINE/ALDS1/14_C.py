h, w = map(int, input().split())
field = [[] for i in range(h)] 
for i in range(h):
    field[i] = input()
# print(field)

r, c = map(int, input().split())
pattern = [[] for i in range(r)] 
for i in range(r):
    pattern[i] = input()

for i in range(h - r + 1):
    for j in range(w - c + 1):
        flag = 1
        for k in range(r):
            if not field[i+k].startswith(pattern[k], j):
                flag = 0
                break
        if flag == 1:
            print(i, j)
