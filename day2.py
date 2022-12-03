X = 1 # rock
Y = 2 # paper
Z = 3 # scissors

def get_outcome_score(player_one, player_two):

    score = 0
    if player_two == 'X':
        if player_one == 'A':
            score += 3
        elif player_one == 'B':
            score += 1
        elif player_one == 'C':
            score += 2
    elif player_two == 'Y':
        score += 3
        if player_one == 'A':
            score += 1
        elif player_one == 'B':
            score += 2
        elif player_one == 'C':
            score += 3
    elif player_two == 'Z':
        score += 6
        if player_one == 'A':
            score += 2
        elif player_one == 'B':
            score += 3
        elif player_one == 'C':
            score += 1
    return score


def get_total_score(player_one, player_two):

    total = 0
    # Shape + Outcome
    # Tied use cases
    if player_one == 'A' and player_two == 'X':#rock and rock
        total = X + 3
    elif player_one == 'B' and player_two == 'Y':#paper and paper
        total = Y + 3
    elif player_one == 'C' and player_two == 'Z':# scissors and scissors
        total = Z + 3

    # Lose use cases 
    elif player_one == 'A' and player_two == 'Z': #rock and scissors
        total = Z + 0
    elif player_one == 'C' and player_two == 'Y': #scissors and paper
        total = Y + 0
    elif player_one == 'B' and player_two == 'X': #paper and rock
        total = X + 0

    # Winning use cases
    elif player_one == 'B' and player_two == 'Z': #paper and scissors
        total = Z + 6
    elif player_one == 'A' and player_two == 'Y': #rock and paper
        total = Y + 6
    elif player_one == 'C' and player_two == 'X': #scissors and rock 
        total = X + 6

    return total


def main():
    f = open("strategy_guide.txt", "r")
    rounds = f.readlines()
    total_score = 0
    outcome_score = 0

    for i in range(len(rounds)):
        p1 = rounds[i][0]
        p2 = rounds[i][2]
        total_score += get_total_score(p1, p2) # Part 1 Solution
        outcome_score += get_outcome_score(p1, p2) # Part 2 Solution

    print(total_score) 
    print(outcome_score)



if __name__ == '__main__':
    main()

