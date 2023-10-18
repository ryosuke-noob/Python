A = set()
B = set()
n = int(input())
a_array = list(map(int, input().split()))
for i in range(n):
    A.add(a_array[i])
m = int(input())
b_array = list(map(int, input().split()))
for i in range(m):
    B.add(b_array[i])
AB = list(A ^ B)
union = sorted(AB)
for elem in union:
    print(elem)

# mohejin

# n = int(input())
# A = set((map(int, input().split())))
# m = int(input())
# B = set((map(int, input().split())))

# print(A)
# print(B)