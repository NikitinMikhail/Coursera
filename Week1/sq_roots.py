import sys

a, b, c = [int(sys.argv[i]) for i in range(1, 4)]

print(int((-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 / a))
print(int((-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 / a))
