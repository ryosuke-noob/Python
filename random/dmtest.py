import math

# param
w1 = 1.0
w2 = -1.0
b = 0.0

# input
x1 = 0.50
x2 = 0.50
t = 1
n = 1.0

# forward propagation
a = b + w1*x1 + w2*x2
y = 1 / (1 + math.exp(-a))
z = 1/2 * (y - t)**2

print("1st out :", y)
print("1st loss:", z, "\n")

# back propagation
w1 = w1 + x1 * y*((1-y)**2)
w2 = w2 + x2 * y*((1-y)**2)
b = b + y*((1-y)**2)

print("w1:", w1)
print("w2:", w2)
print("b :", b, "\n")

# forward propagation
a = b + w1*x1 + w2*x2
y = 1 / (1 + math.exp(-a))
z = 1/2 * (y - 1)**2

print("2nd out :", y)
print("2nd loss:", z)
