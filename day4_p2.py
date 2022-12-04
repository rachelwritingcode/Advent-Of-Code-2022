def get_range_list(section)->list:
    section = section.split("-")
    range_list = []
    first_index = int(section[0])
    second_index = int(section[1])+1
    range_list = [*range(first_index, second_index)]
    return range_list

def check_overlap(section):
    elf_one = set(get_range_list(section[0]))
    elf_two = set(get_range_list(section[1]))
    if elf_one.intersection(elf_two):
        return True 
    elif elf_two.intersection(elf_one):
        return True
    else:
        return False

def main():
    f = open("./input/day4-input.txt", "r")
    overlap = 0
    sections = f.readlines()
    for section in sections:
        section = section.replace("\n","").split(",")
        if check_overlap(section):
            overlap += 1
    print(f"There are {overlap} pairs that overlap.")

if __name__ == '__main__':
    main()
