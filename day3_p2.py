# remove \n character
def clean_list(group_list): 
    clean_list = []
    for group in group_list:
        group = group.replace("\n","")
        clean_list.append(group)
    return clean_list

def get_duplicate(group_list): 
    group_list = clean_list(group_list)
    item = None
    duplicate_item = set(group_list[0]) & set(group_list[1]) & set(group_list[2])
    for i in duplicate_item:
        if i != '\n':
            item = i
    print(f"Duplicate item: {duplicate_item}")
    return item

def get_priority(item): 
    priority = 0
    if item.islower():
        priority = ord(item)-96
    else:
        priority = ord(item)-65+27
    print(f"Priority value: {priority}")
    return priority

def group_elves(elves):
    group_list = [elves[n:n+3] for n in range(0, len(elves), 3)]
    return group_list

def main():
    # f = open("./input/d3_test.txt", "r")
    f = open("./input/day3_input.txt", "r")
    elves = f.readlines()
    group_list = group_elves(elves)
    total = 0
    for group in group_list:
        item = get_duplicate(group)
        total += get_priority(item)  
    print(f"Total sum : {total}")

if __name__ == '__main__':
    main()
