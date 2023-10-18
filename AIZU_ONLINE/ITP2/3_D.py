n = int(input())
n_nums = list(map(int, input().split()))
m = int(input())
m_nums = list(map(int, input().split()))
n_len = len(n_nums)
m_len = len(m_nums)
for i in range(min(n_len, m_len)):
    if n_nums[i] == m_nums[i]:
        continue
    if n_nums[i] < m_nums[i]:
        print(1)
        exit()
    else:
        print(0)
        exit()
if n_len < m_len:
    print(1)
else:
    print(0)