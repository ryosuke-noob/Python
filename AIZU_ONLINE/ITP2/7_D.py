from bisect import bisect_left, bisect_right, insort_left
dict = {}
keytbl = []
cnt = 0
q = int(input())
for i in range(q):
	a = list(input().split())
	ki = int(a[1])
	if a[0] == '0':
		if ki not in dict:
			dict[ki] = 1
			insort_left(keytbl, ki)
		else: dict[ki] += 1
		cnt += 1
		print(cnt)
	elif a[0] == '1': print(dict[ki] if ki in dict else 0)
	elif a[0] == '2':
		if ki in dict:
			cnt -= dict[ki]
			dict[ki] = 0
	else:
		L = bisect_left (keytbl, int(a[1]))
		R = bisect_right(keytbl, int(a[2]), L)
		r = []
		for j in range(L, R): r += [keytbl[j]]*dict[keytbl[j]]
		if r != []: print(*r, sep='\n')
