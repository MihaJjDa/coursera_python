import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = (b**2 - 4*a*c) ** 0.5

print(int(((-1)*b + d)/(2*a)))
print(int(((-1)*b - d)/(2*a)))

