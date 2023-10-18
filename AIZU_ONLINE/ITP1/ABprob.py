a, b = (int(x) for x in input().split())
d = int(a/b)
r = a%b
f = float(d) + float(r/b)
print(d, r, round(f, 10))

# round is needed

# #someone's
# a,b = map(int,input().split())

# print("%d %d %.10f"%(a/b,a%b,a/b))