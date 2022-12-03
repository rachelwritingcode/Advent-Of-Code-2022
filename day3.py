import math

def get_priority(item): #16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.
    priority = 0
    for i in item:
        if i.islower():
            priority = ord(i)-96
        else:
            priority = ord(i)-65+27
    return priority

def get_duplicate(rucksack): # vJrwpWtwJgWr hcsFMMfFFhFp
    middle = math.floor(len(rucksack) / 2)
    first_comp = rucksack[0:middle]
    second_comp = rucksack[middle:]
    duplicate_item = set(first_comp) & set(second_comp)
    return duplicate_item

def main():
    f = open("./input/day3_input.txt", "r")
    total = 0
    rucksacks = f.readlines()
    for i in range(len(rucksacks)):
        rucksack = rucksacks[i]
        duplicate_item = get_duplicate(rucksack)
        total += get_priority(duplicate_item)
    print(total)

if __name__ == '__main__':
    main()
