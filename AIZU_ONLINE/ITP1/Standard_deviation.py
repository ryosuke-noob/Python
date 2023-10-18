import statistics

while True:
    n = int(input())
    if n == 0:
        break
    arg = map(int, input().split())
    print(statistics.pstdev(arg))