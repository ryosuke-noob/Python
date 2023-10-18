n = int(input())
coordinates = []
for i in range(n):
    coordinate = tuple(map(int,input().split()))
    coordinates.append(coordinate)
coordinates.sort()
for xy in coordinates:
    print(xy[0], xy[1])
# for xy in coordinates:
#     print(*xy)
