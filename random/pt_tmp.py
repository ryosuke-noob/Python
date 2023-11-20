import numpy as np
from scipy import stats

ball_list = np.array([8,6,8,4,6,6,8,4,6,8,8,6])
ball_num = len(ball_list)

a = np.zeros(ball_num)
b = np.zeros(ball_num)
c = np.zeros(ball_num)

# params init

p_8_a = 0.054
p_8_b = 0.054
p_8_c = 0.399

p_a = 0.44
p_b = 0.25
p_c = 0.31

p5a = stats.norm.pdf(x=5, loc=7.23, scale=1.27**0.5)
p5b = stats.norm.pdf(x=5, loc=3.10, scale=0.89**0.5)
p5c = stats.norm.pdf(x=5, loc=5.20, scale=1.13**0.5)
# p5a = round(p5a, 3)
# p5b = round(p5b, 3)
# p5c = round(p5c, 3)
p5 = p5a * p_a + p5b * p_b + p5c * p_c
# p5 = round(p5, 3)

print('p5:', p5)
print('p5a:', p5a)
print('p5b:', p5b)
print('p5c:', p5c)

print('-------')

print('pa5:', round(p5a * p_a / p5, 3))
print('pb5:', round(p5b * p_b / p5, 3))
print('pc5:', round(p5c * p_c / p5, 3))

print('-------')
p_a = 1 / 3
p_b = 1 / 3
p_c = 1 / 3

# p6a = round(stats.norm.pdf(x=6, loc=7, scale=1.0**0.5), 3)
# p6b = round(stats.norm.pdf(x=6, loc=3, scale=1.0**0.5), 3)
# p6c = round(stats.norm.pdf(x=6, loc=5, scale=1.0**0.5), 3)
p6a = (stats.norm.pdf(x=6, loc=7, scale=1.0**0.5))
p6b = (stats.norm.pdf(x=6, loc=3, scale=1.0**0.5))
p6c = (stats.norm.pdf(x=6, loc=5, scale=1.0**0.5))

print(f'stats p6a: {p6a}')
print(f'stats p6b: {p6b}')
print(f'stats p6c: {p6c}')
print('-------')
p6 = (p_a * p6a + p_b * p6b + p_c * p6c)
pa6 = round(p6a * p_a / p6, 3)
pb6 = round(p6b * p_b / p6, 3)
pc6 = round(p6c * p_c / p6, 3)
# p6 = round(p_a * p6a + p_b * p6b + p_c * p6c, 3)
# pa6 = round(p6a * p_a / p6, 3)
# # pb6 = round(p6b * p_b / p6, 3)
# pc6 = round(p6c * p_c / p6, 3)
print(f'pa6: {pa6}')
print(f'pb6: {pb6}')
print(f'pc6: {pc6}')




# for rec in range(0,10):
#     print(f'---{rec}---')
#     p_8 = p_8_a * p_a + p_8_b * p_b + p_8_c * p_c
#     # p_6 = p_6_a * p_a + p_6_b * p_b + p_6_c * p_c
#     # p_4 = p_4_a * p_a + p_4_b * p_b + p_4_c * p_c

#     for i, x in enumerate(ball_list):
#         if x == 8:
#             a[i] = p_8_a * p_a / p_8 # p_a_8
#             b[i] = p_8_b * p_b / p_8 # p_b_8
#             c[i] = p_8_c * p_c / p_8 # p_c_8
#         if x == 6:
#             a[i] = p_6_a * p_a / p_6 # p_a_6
#             b[i] = p_6_b * p_b / p_6 # p_b_6
#             c[i] = p_6_c * p_c / p_6 # p_c_6
#         if x == 4:
#             a[i] = p_4_a * p_a / p_4 # p_a_4
#             b[i] = p_4_b * p_b / p_4 # p_b_4
#             c[i] = p_4_c * p_c / p_4 # p_c_4
#     # a
#     a_sum = a.sum()
#     p_a = a.sum() / ball_num
#     a_ave = np.matmul(a,ball_list.T) / a_sum
#     a_res = (ball_list - a_ave)**2
#     a_v = np.matmul(a_res, a.T) / a_sum
#     p_8_a = stats.norm.pdf(x=8, loc=a_ave, scale=a_v)
#     p_6_a = stats.norm.pdf(x=6, loc=a_ave, scale=a_v)
#     p_4_a = stats.norm.pdf(x=4, loc=a_ave, scale=a_v)
#     print(f'a_ave: {a_ave}, a_v: {a_v}, p_8_a: {p_8_a}')
#     # b
#     b_sum = b.sum()
#     p_b = b.sum() / ball_num
#     b_ave = np.matmul(b,ball_list.T) / b_sum
#     b_res = (ball_list - b_ave)**2
#     b_v = np.matmul(b_res, b.T) / b_sum
#     p_8_b = stats.norm.pdf(x=8, loc=b_ave, scale=b_v)
#     p_6_b = stats.norm.pdf(x=6, loc=b_ave, scale=b_v)
#     p_4_b = stats.norm.pdf(x=4, loc=b_ave, scale=b_v)
#     print(f'b_ave: {b_ave}, b_v: {b_v}, p_8_b: {p_8_b}')
#     # c
#     c_sum = c.sum()
#     p_c = c.sum() / ball_num
#     c_ave = np.matmul(c,ball_list.T) / c_sum
#     c_res = (ball_list - c_ave)**2
#     c_v = np.matmul(c_res, c.T) / c_sum
#     p_8_c = stats.norm.pdf(x=8, loc=c_ave, scale=c_v)
#     p_6_c = stats.norm.pdf(x=6, loc=c_ave, scale=c_v)
#     p_4_c = stats.norm.pdf(x=4, loc=c_ave, scale=c_v)
#     print(f'c_ave: {c_ave}, c_v: {c_v}, p_8_c: {p_8_c}')


# print(b)
# print(c)


