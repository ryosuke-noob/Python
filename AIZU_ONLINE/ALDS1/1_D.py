def culc_max_profit(R) -> int:
    R_len = len(R)
    min_point = R[0]
    max_profit = R[1] - R[0]
    for i in range(1, R_len):
        max_profit = max(max_profit, R[i] - min_point)
        min_point = min(min_point, R[i])
    return (max_profit)

n = int(input())
R = []
for _ in range(n):
    R.append(int(input()))
print(culc_max_profit(R))
