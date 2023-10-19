def is_op(arg : str) -> bool:
    length = len(arg)
    if length > 1:
        return False
    if arg[0] == '+' or arg[0] == '-' or arg[0] == '*':
        return True
    else:
        return False

def do_op(arg : str, a : int, b : int) -> int:
    if arg[0] == '+':
        return a + b
    if arg[0] == '-':
        return a - b
    if arg[0] == '*':
        return a * b
    return -1

args = input().split()
stack = []
for arg in args:
    # print(type(arg))
    if is_op(arg):
        b = stack.pop(-1)
        a = stack.pop(-1)
        res = do_op(arg, a, b)
        stack.append(res)
    else:
        stack.append(int(arg))
    # print(*stack)
print(stack[0])