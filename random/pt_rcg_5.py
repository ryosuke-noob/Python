import numpy as np
from scipy import stats

ball_list = np.array([8,6,8,4,6,6,8,4,6,8,8,6])
ball_num = len(ball_list)

a = np.zeros(ball_num)
b = np.zeros(ball_num)
c = np.zeros(ball_num)

# params init
p_a = 0.333
p_b = 0.333
p_c = 0.333

p_8_a = 0.2
p_8_b = 0.4
p_8_c = 0.5
p_6_a = 0.3
p_6_b = 0.4
p_6_c = 0.2
p_4_a = 0.5
p_4_b = 0.2
p_4_c = 0.3

for rec in range(1):
    print(f'---{rec+1}---')
    p_8 = p_8_a * p_a + p_8_b * p_b + p_8_c * p_c
    p_6 = p_6_a * p_a + p_6_b * p_b + p_6_c * p_c
    p_4 = p_4_a * p_a + p_4_b * p_b + p_4_c * p_c

    for i, x in enumerate(ball_list):
        if x == 8:
            a[i] = p_8_a * p_a / p_8 # p_a_8
            b[i] = p_8_b * p_b / p_8 # p_b_8
            c[i] = p_8_c * p_c / p_8 # p_c_8
        if x == 6:
            a[i] = p_6_a * p_a / p_6 # p_a_6
            b[i] = p_6_b * p_b / p_6 # p_b_6
            c[i] = p_6_c * p_c / p_6 # p_c_6
        if x == 4:
            a[i] = p_4_a * p_a / p_4 # p_a_4
            b[i] = p_4_b * p_b / p_4 # p_b_4
            c[i] = p_4_c * p_c / p_4 # p_c_4
    # a
    a_sum = a.sum()
    p_a = a.sum() / ball_num
    a_ave = np.matmul(a,ball_list.T) / a_sum
    a_res = (ball_list - a_ave)**2
    a_v = np.matmul(a_res, a.T) / a_sum
    p_8_a = (a_v + (4 - a_ave) * (6 - a_ave)) / 8
    p_6_a = - (a_v + (4 - a_ave) * (8 - a_ave)) / 4
    p_4_a = (a_v + (6 - a_ave) * (8 - a_ave)) / 8
    print(f'p(A): {round(p_a,2)}')
    print(f'p(8|k): {round(p_8_a,2)}')
    print(f'p(6|k): {round(p_6_a,2)}')
    print(f'p(4|k): {round(p_4_a,2)}')
    # print(f'a_ave: {a_ave}, a_v: {a_v}, p_8_a: {p_8_a}')
    # b
    b_sum = b.sum()
    p_b = b.sum() / ball_num
    b_ave = np.matmul(b,ball_list.T) / b_sum
    b_res = (ball_list - b_ave)**2
    b_v = np.matmul(b_res, b.T) / b_sum
    p_8_b = (b_v + (4 - b_ave) * (6 - b_ave)) / 8
    p_6_b = - (b_v + (4 - b_ave) * (8 - b_ave)) / 4
    p_4_b = (b_v + (6 - b_ave) * (8 - b_ave)) / 8
    print(f'p(B): {round(p_b,2)}')
    print(f'p(8|k): {round(p_8_b,2)}')
    print(f'p(6|k): {round(p_6_b,2)}')
    print(f'p(4|k): {round(p_4_b,2)}')
    # print(f'b_ave: {b_ave}, b_v: {b_v}, p_8_b: {p_8_b}')
    # c
    c_sum = c.sum()
    p_c = c.sum() / ball_num
    c_ave = np.matmul(c,ball_list.T) / c_sum
    c_res = (ball_list - c_ave)**2
    c_v = np.matmul(c_res, c.T) / c_sum
    p_8_c = (c_v + (4 - c_ave) * (6 - c_ave)) / 8
    p_6_c = - (c_v + (4 - c_ave) * (8 - c_ave)) / 4
    p_4_c = (c_v + (6 - c_ave) * (8 - c_ave)) / 8
    print(f'p(C): {round(p_c,2)}')
    print(f'p(8|k): {round(p_8_c,2)}')
    print(f'p(6|k): {round(p_6_c,2)}')
    print(f'p(4|k): {round(p_4_c,2)}')
    # print(f'c_ave: {c_ave}, c_v: {c_v}, p_8_c: {p_8_c}')
