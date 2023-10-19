def my_find(lst : list, key) -> int:
    if key in lst:
        return lst.index(key)
    else:
        return -1

field = input()
flen = len(field)
sum_area = 0
i_filed = [0]
for i in range(flen):
    if field[i] == '\\':
        i_filed.append(i_filed[i] - 1)
    elif field[i] == '/':
        i_filed.append(i_filed[i] + 1)
    else: # field[i] == '-'
        i_filed.append(i_filed[i])

# print(*i_filed)

lst_area = []
# for i in range(flen):
i = 0
while i < flen:
    now_h = i_filed[i]
    next_same_h_index = my_find(i_filed[i+1:], now_h)
    if next_same_h_index == -1:
        i += 1
        continue
    else:
        next_same_h_index += i + 1 # relative index -> def index
    if i_filed[i+1] >= now_h:
        i+= 1
        continue
    # print("next_height", next_same_h_index)
    area = 0.0
    j = i + 1
    # for j in range(1, next_same_h_index - i - 1):
    while j <= next_same_h_index:
        area += now_h - i_filed[j] - 1
        if field[j - 1] == '_':
            area += 1
        elif field[j - 1] == '\\':
            area += 0.5
        else:
            area += 1.5
        # print(area)
        j += 1
    i = next_same_h_index
    sum_area += int(area)
    lst_area.append(int(area))

print(sum_area)
print(len(lst_area), *lst_area)


for i in range(flen - 1):
    if field[i] == '\\' and field[i + 1] =='\\': #\\
        pass
    if field[i] == '\\' and field[i + 1] =='/': #\/
        pass
    if field[i] == '/' and field[i + 1] =='\\': #/\
        pass
    if field[i] == '/' and field[i + 1] =='//': #//
        pass
    