n = int(input())
masks = []
for i in range(n):
    masks[i] = list(map(int, input().split()))

q = int(input())
flag = 0
for _ in range(q):
    type, m = (map(int, input().split()))
    if type == 0: #test
        print((flag >> i) & 1)
    elif type == 1: #set
        for i in masks[m]:
            if not ((flag >> i) & 1):
                flag += (1 << i)
    elif type == 2: # clear
        for i in masks[m]:
            if ((flag >> i) & 1):
                flag -= (1 << i)
    elif type == 3: # flip
        for i in masks[m]:
            if not ((flag >> i) & 1):
                flag += (1 << i)
            else: 
                flag -= (1 << i)        
    elif type == 4: # all
        tmp_flag = 1
        for i in masks[m]:
            if not ((flag >> i) & 1):
                tmp_flag *= 0
        print(tmp_flag)
    elif type == 5: # any
        tmp_flag = 0
        for i in masks[m]:
            if ((flag >> i) & 1):
                tmp_flag = 1
        print(tmp_flag)
    elif type == 6: # none
        tmp_flag = 1
        for i in masks[m]:
            if ((flag >> i) & 1):
                tmp_flag = 0
        print(tmp_flag)
    elif type == 7: # count
        count = 0
        for i in masks[m]:
            if (flag >> i & 1):
                count += 1
        print(count)
    elif type == 8: # val
        sum = 0
        for i in masks[m]:
            bit_on = (flag >> i) & 1
            sum += bit_on * (1 << i)
        print(sum)
