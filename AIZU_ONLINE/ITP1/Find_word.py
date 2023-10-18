w = input()
w = w.lower()
count = 0
end = "END_OF_TEXT"
while True:
    t = input()
    if end == t:
        break
    t = t.lower()
    arg = t.split()
    for t in arg:
        if t == w:
            count += 1

print(count)