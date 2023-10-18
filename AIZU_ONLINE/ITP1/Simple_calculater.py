while(1):
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    if op == "+":
        print(a + b)
    if op == "-":
        print(a - b)
    if op == "*":
        print(a * b)
    if op == "/":
        print(int(a / b))
    if op == "?":
        break
