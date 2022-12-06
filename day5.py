from collections import deque

def move_crate(crates, quantity, from_location, to_location) -> list:
    new_crates = []
    # print(f"Move {quantity} {crates[from_location]} to {crates[to_location]}")
    while quantity != 0:
        crates[to_location].append((crates[from_location].pop()))
        quantity -= 1
    new_crates = crates 
    return new_crates 

def translate_instructions(crates, instructions) -> list:
    new_crates = []
    for instr in instructions:
        quantity = int(instr.split("move")[1].split("from")[0])
        from_location = int(instr.split("from")[1].split("to")[0]) - 1
        to_location = int(instr.split("to")[1]) - 1
        new_crates = move_crate(crates, quantity, from_location, to_location )
    return new_crates

def main():

    # f = open("./input/day5-test.txt", "r")
    f = open("./input/day5-input.txt", "r")
    crates = []
    new_crates = []
    crate_lines = []
    lines = f.readlines()

    for line in lines:
        crate_lines.append(line.strip('\n'))

    # TODO change for real input
    # c1 = deque(['Z', 'N'])
    # c2 = deque(['M', 'C', 'D'])      
    # c3 = deque(['P']) 
    # crates = [c1, c2, c3]

    c1 = deque(['F','T','C','L','R','P','G','Q'])
    c2 = deque(['N','Q','H','W','R','F','S','J'])
    c3 = deque(['F','B','H','W','P','M','Q'])
    c4 = deque(['V','S','T','D','F'])
    c5 = deque(['Q','L','D','W','V','F','Z'])
    c6 = deque(['Z','C','L','S'])
    c7 = deque(['Z','B','M','V','D','F'])
    c8 = deque(['T','J','B'])
    c9 = deque(['Q','N','B','G','L','S','P','H'])
    crates = [c1,c2,c3,c4,c5,c6,c7,c8,c9]

    instructions = crate_lines[10:] # TODO change index for real input
    new_crates = translate_instructions(crates, instructions)
    for crate in new_crates:
        print(crate.pop())
       
if __name__ == '__main__':
    main()