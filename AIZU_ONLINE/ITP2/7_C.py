import bisect

def is_contained(key : int, S : list, s_len : int) -> int:
    start = 0
    end = s_len - 1
    while start <= end:
        s_len = end - start + 1
        mid = int(s_len / 2) + start
        if S[mid] < key:
            start = mid + 1
        elif S[mid] > key:
            end = mid - 1
        else: # array[mid] == key
            return 1
    return 0

S = []
s_len = 0
q = int(input())
for _ in range(q):
    cmd = list(map(int, input().split()))
    be_found = is_contained(cmd[1], S, s_len)
    if cmd[0] == 0:
        if be_found == 0:
            S.insert(bisect.bisect_left(S, cmd[1]), cmd[1])
            s_len += 1
        print(s_len)
    if cmd[0] == 1:
        print(be_found)
    if cmd[0] == 2:
        if be_found:
            S.pop(bisect.bisect_left(S, cmd[1]))
            s_len -= 1
    if cmd[0] == 3:
        start = bisect.bisect_left(S, cmd[1])
        end = bisect.bisect_right(S, cmd[2])
        for i in range(start, end):
            print(S[i])
