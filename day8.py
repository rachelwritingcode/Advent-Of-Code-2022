def main():
    
    tree_counter = 0
    scenic_score = 0
    trees = []
    with open("./input/day8-input.txt") as f:
        for line in f:
            tree_positions = [int(t) for t in line.strip()]
            trees.append(tree_positions)

    for i, row in enumerate(trees):
        for j, height in enumerate(row):
            score = 1
            isVisible = False
            treelines = [
                row[:j][::-1],
                row[j + 1 :],
                [r[j] for r in trees[:i]][::-1],
                [r[j] for r in trees[i + 1 :]],
            ]

            for treeline in treelines:
                for dist, h in enumerate(treeline, 1):
                    if h >= height:
                        score *= dist
                        break
                else:
                    isVisible = True
                    score *= max(1, len(treeline))

            tree_counter += int(isVisible)
            scenic_score = max(score, scenic_score)

    print(tree_counter) # Part 1
    print(scenic_score) # Part 2


if __name__ == '__main__':
    main()