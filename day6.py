
def main():
    f = open("./input/day6-input.txt", "r")
    message = f.read()

    # part 1
    for i in range(0,len(message)):
        if len(set(message[i:i+4])) == 4:
            break
    marker = i + 4
    print(f"Characters that need to be processed {marker}")

    # part 2
    for i in range(0,len(message)):
        if len(set(message[i:i+14])) == 14:
            break
    marker = i + 14
    print(f"Characters that need to be processed {marker}")

if __name__ == '__main__':
    main()