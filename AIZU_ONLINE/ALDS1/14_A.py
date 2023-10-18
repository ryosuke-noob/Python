t = input()
p = input()
t_len = len(t)
p_len = len(p)
if (p_len > t_len):
    exit()
for i in range(t_len - p_len + 1):
    if t[i] == p[0]:
        flag = 1
        for j in range(p_len):
            if t[i+j] != p[j]:
                flag = 0
        if flag == 1:
            print(i)
