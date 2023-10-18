n = int(input())
coordinates = []
for i in range(n):
    coordinate = list(input().split())
    coordinate[0] = int(coordinate[0])
    coordinate[1] = int(coordinate[1])
    coordinate[3] = int(coordinate[3])
    coordinate = tuple(coordinate)
    coordinates.append(coordinate)
coordinates = sorted(coordinates)
# for xy in coordinates:
#     print(xy[0], xy[1])
for xy in coordinates:
    print(*xy)

# tbl = []
# n = int(input())
# for i in range(n):
# 	a = input().split()
# 	tbl.append((int(a[0]), int(a[1]), a[2], int(a[3]), a[4]))
# tbl.sort()
# for i in tbl: print(*i)
