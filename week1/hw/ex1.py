import sys

digit_string = sys.argv[1]
s = 0
for i in digit_string:
    s += int(i)
print(s)
