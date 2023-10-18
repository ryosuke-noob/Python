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

def is_same(a_arg, b_arg):
    b1, b2, b3, b4, b5, b6 = b_arg

    if check_arg(a_arg, b_arg, b1, b2) != b3:
        return False
    elif check_arg(a_arg, b_arg, b2, b6) != b3:
        return False
    elif check_arg(a_arg, b_arg, b6, b5) != b3:
        return False
    elif check_arg(a_arg, b_arg, b5, b1) != b3:
        return False
    elif check_arg(a_arg, b_arg, b4, b2) != b1:
        return False
    elif check_arg(a_arg, b_arg, b2, b3) != b1:
        return False
    elif check_arg(a_arg, b_arg, b3, b5) != b1:
        return False
    elif check_arg(a_arg, b_arg, b5, b4) != b1:
        return False
    elif check_arg(a_arg, b_arg, b3, b2) != b6:
        return False
    elif check_arg(a_arg, b_arg, b2, b4) != b6:
        return False
    elif check_arg(a_arg, b_arg, b4, b5) != b6:
        return False
    elif check_arg(a_arg, b_arg, b5, b3) != b6:
        return False
    elif check_arg(a_arg, b_arg, b6, b2) != b4:
        return False
    elif check_arg(a_arg, b_arg, b2, b1) != b4:
        return False
    elif check_arg(a_arg, b_arg, b1, b5) != b4:
        return False
    elif check_arg(a_arg, b_arg, b5, b6) != b4:
        return False
    elif check_arg(a_arg, b_arg, b1, b4) != b2:
        return False
    elif check_arg(a_arg, b_arg, b4, b6) != b2:
        return False
    elif check_arg(a_arg, b_arg, b6, b3) != b2:
        return False
    elif check_arg(a_arg, b_arg, b3, b1) != b2:
        return False
    elif check_arg(a_arg, b_arg, b1, b3) != b5:
        return False
    elif check_arg(a_arg, b_arg, b3, b6) != b5:
        return False
    elif check_arg(a_arg, b_arg, b6, b4) != b5:
        return False
    elif check_arg(a_arg, b_arg, b4, b1) != b5:
        return False
    else:
        return True

n = int(input())
args = []
for _ in range(0,n):
    arg = input().split()
    args.append(arg)
have_same = False
for i in range(0,n-1):
    for j in range(i+1,n):
        if is_same(args[i], args[j]) == True:
            have_same = True
if have_same == True:
    print("No")
else:
    print("Yes")