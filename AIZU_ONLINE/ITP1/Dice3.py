def check_arg(a_arg, b_arg, up, front):
    a1, a2, a3, a4, a5, a6 = a_arg
    b1, b2, b3, b4, b5, b6 = b_arg
    a_case1 = a4+a2+a3+a5+a4
    a_case2 = a1+a4+a6+a3+a1
    a_case3 = a1+a2+a6+a5+a1
    a_case4 = a1+a5+a6+a2+a1
    a_case5 = a1+a3+a6+a4+a1
    a_case6 = a2+a4+a5+a3+a2
    str = up + front
    if str in a_case1:
        return a1
    if str in a_case2:
        return a2
    if str in a_case3:
        return a3
    if str in a_case4:
        return a4
    if str in a_case5:
        return a5
    if str in a_case6:
        return a6

a_arg = input().split()
b_arg = input().split()
b1, b2, b3, b4, b5, b6 = b_arg

if check_arg(a_arg, b_arg, b1, b2) != b3:
    print("No")
elif check_arg(a_arg, b_arg, b2, b6) != b3:
    print("No")
elif check_arg(a_arg, b_arg, b6, b5) != b3:
    print("No")
elif check_arg(a_arg, b_arg, b5, b1) != b3:
    print("No")
else:
    print("Yes")