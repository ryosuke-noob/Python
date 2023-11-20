# 91
# f = open('test.txt', 'a')
# # f.write('Test\n')
# print('I am print', file=f)
# f.close()

# 92
# with open('test.txt', 'a') as f:
#     # # f.write('Test\n')
#     print('I am print', file=f)

# # 93
# s = """\
# AAA
# BBB
# CCC
# DDD
# """
# # with open('test.txt', 'w') as f:
# #     f.write(s)
# #     # print('I am print', file=f)

# with open('test.txt', 'r') as f:
#     # print(f.read())
#     while True:
#         chunk = 2
#         # line = f.readline()
#         line = f.read(chunk)
#         print(line, end='')
#         # print(line)
#         if not line:
#             break

# 94
with open('test.txt', 'r') as f:
    # fileのポインタが現在どこをさしているか
    print(f.tell())
    print(f.read(1))
    print(f.tell())
    # ファイルポインタの設定
    f.seek(5)
    print(f.tell())
    print(f.read(1))
    f.seek(14)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))
    f.seek(5)
    print(f.read(1))