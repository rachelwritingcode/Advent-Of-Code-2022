from collections import defaultdict

MAX_SIZE = 100000
total = 0

def main():

    f = open("./input/day7-input.txt", "r")
    dir_sizes = defaultdict(int)
    total = 0
    commands = []
    inputs = f.readlines()
    file_path = []

    for command in inputs:
        commands.append(command.strip("\n"))

    for c in commands:
        if c.find('$ cd') != -1:
            directory = c.split()[-1]
            if directory == '..':
                file_path.pop()
            else:
                file_path.append(directory)

        elif c.find('$ ls') != -1:
            continue
        else:
            size = c.split(" ")[0]
            if(size.isdigit()):
                for i in range(len(file_path)):
                    dir_sizes['/'.join(file_path[:i+1])] += int(size)
        
    for _, v in dir_sizes.items():
        if v <= 100_000:
            total += v

    print(total)

if __name__ == '__main__':
    main()
