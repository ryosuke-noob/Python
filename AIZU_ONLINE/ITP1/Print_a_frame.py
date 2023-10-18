while(1):
    h, w = map(int, input().split())
    if h == 0 and w == 0:
        break
    for j in range(0, w-1):
        print('#', end="")
    print('#')
    for i in range(1, h-1):    
        print('#', end="")
        for j in range(1, w-1):
            print('.', end="")
        print('#')
    for j in range(0, w-1):
        print('#', end="")
    print('#')
    print('')