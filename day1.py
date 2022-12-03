f = open("./input/day1-input.txt", "r")
calorie_list = f.readlines()

elf_totals = []
elf_calorie_total = 0

for line in calorie_list:
    if line == '\n':
        elf_totals.append(elf_calorie_total)
        elf_calorie_total = 0
    else:
        elf_calorie_total += int(line)

elf_one = sorted(elf_totals)[-1] # Part 1 Solution
elf_two = sorted(elf_totals)[-2] # Part 2 Solution
elf_three = sorted(elf_totals)[-3] # Part 2 Solution

max_three_elves = elf_one + elf_two + elf_three
