def get_range_list(section)->list:
    section = section.split("-")
    range_list = []
    first_index = int(section[0])
    second_index = int(section[1])+1
    range_list = [*range(first_index, second_index)]
    return range_list

def check_contains(section):
    elf_one = set(get_range_list(section[0]))
    elf_two = set(get_range_list(section[1]))
    if (elf_one.issubset(elf_two) or elf_two.issubset(elf_one)):
        return True 
    else:
        return False

def main():
    f = open("./input/day4-input.txt", "r")
    contains = 0
    sections = f.readlines()
    for section in sections:
        section = section.replace("\n","").split(",")
        if check_contains(section):
            contains += 1
    print(f"There are {contains} assignment pairs that contain each other")

if __name__ == '__main__':
    main()
