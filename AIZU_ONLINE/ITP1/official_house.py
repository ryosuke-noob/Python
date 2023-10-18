# 失敗
# この作り方だと同じIDをもつ[int(0)] * 10が12個つくられてしまう．
# # init
# tenant = [[[int(0)] * 10] * 3] * 4　
# print(tenant)
# # input
# n = int(input())
# for i in range(0, n):
#     b, f, r, v = map(int, input().split())
#     tenant[b - 1][f - 1][r - 1] = v

# # print
# for i in range(0,4):
#     print(id(tenant[i]))
#     for j in range(0, 3):
#         for k in range(0, 10):
#             print(tenant[i][j][k], end=' ')
#         print('')
#     if i != 3:
#         print('####################')

# init
tenant = [[[int(0)] * 10 for i in range(0,3)] for j in range(0,4)]
# print(tenant)
# input
n = int(input())
for i in range(0, n):
    b, f, r, v = map(int, input().split())
    tenant[b - 1][f - 1][r - 1] += v

# print
for i in range(0,4):
    # print(id(tenant[i]))
    for j in range(0, 3):
        for k in range(0, 10):
            print('', tenant[i][j][k], end='')
            # if k != 9:
            #     print(' ', end='')
        print('')
    if i != 3:
        print('####################')
    