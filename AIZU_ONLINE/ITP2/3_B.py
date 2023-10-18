n = int(input())
nums = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    com, b, e = map(int,input().split())
    if com == 0: #min(b,e)
        print(min(nums[b:e]))
    else:        #max(b,e)
        print(max(nums[b:e]))
