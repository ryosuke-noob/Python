int_list = []
while(1):
    x = int(input())
    if x == 0:
        break
    int_list.append(x)

i = 1
for x in int_list:
    print("Case ", i, ": ", x, sep="")
    i += 1