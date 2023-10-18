import sys

alph_dict = {}
a = ord('a')
z = ord('z')
arg = ''
for i in range(a, z+1):
    alph_dict[chr(i)] = arg.count(chr(i))

# arg = input()
arg = sys.stdin.read()
arg = arg.lower()
tmp = ''.join(set(arg))
for c in tmp:
    if a > ord(c) or ord(c) > z:
        continue
    alph_dict[c] += arg.count(c)

for i, j in alph_dict.items():
    print(i, ':', j)