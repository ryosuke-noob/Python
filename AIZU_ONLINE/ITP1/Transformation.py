str = input()
q = int(input())
for _ in range(0,q):
    arg = input()
    if "print" in arg:
        command, a, b = arg.split()
        a = int(a)
        b = int(b)
        print(str[a:b+1])
    elif "reverse" in arg:
        command, a, b = arg.split()
        a = int(a)
        b = int(b)
        p = str[b:a:-1]
        tmp = str[:a] + p + str[a] + str[b+1:]
        str = "" + tmp
    else:
        command, a, b, p = arg.split()
        a = int(a)
        b = int(b)
        tmp = str[:a] + p + str[b+1:]
        str = "" + tmp
    # print(str)