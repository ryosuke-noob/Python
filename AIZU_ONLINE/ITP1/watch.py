n = int(input())

print(int(n/3600), ":", int((n%3600) /60), ":", n %60, sep="")