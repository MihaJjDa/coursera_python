import sys

num_steps = int(sys.argv[1])

for i in range(num_steps):
    print(" " * (num_steps-1-i), "#" * (i+1), sep="")

