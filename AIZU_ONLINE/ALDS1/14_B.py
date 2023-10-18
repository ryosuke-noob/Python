t = input()
p = input()
t_len = len(t)
p_len = len(p)
if (p_len > t_len):
    exit()
# for i in range(t_len - p_len + 1):
#     if t[i] == p[0]:
#         flag = 1
#         for j in range(int(p_len/2)+1):
#             if t[i+j] != p[j] or t[i+p_len-j-1] != p[p_len-j-1]:
#                 flag = 0
#         if flag == 1:
#             print(i)
for i in range(t_len):
    if t.startswith(p, i): # なんかわからんけど推奨されている方法らしい
        print(i)