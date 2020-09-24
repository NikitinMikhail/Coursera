import sys

ladder_height = int(sys.argv[1])
levels = list()

for level_number in range(1, ladder_height + 1):
    print(' ' * (ladder_height - level_number) + '#'*level_number)
