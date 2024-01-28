# For random number btw 1 to 6 (L3 TO L13)

import random

def rool():
    min_value = 1
    max_value = 6
    rool = random.randint(min_value, max_value)

    return rool

value = rool()
print(value)

# For players (L17 TO L26)

while True:
    players = input("Enter the number of the players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
                print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

# For score dashboard like [0, 0]

max_score = 50
player_score = [0 for _ in range(players)]
# Here "_" is coz i don't care what the varriable is

while max(player_score) < max_score:

    for player_index in range(players):
        print("\nYour total score is:", player_score[player_index])
        print("Player number", player_index + 1, "turn has just started!\n")
        current_score = 0

        while True:
            should_rool = input("Would you like to roll (y/n)? ")
            if should_rool.lower() != "y":
                break
            
            value = rool()

            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            
            print("Your score is:", current_score)
    player_score[player_index] += current_score
    print("Your total score is:", player_score[player_index])

max_score = max(player_score)    
winning_index = player_score.index(max_score)
print("Player number", winning_index + 1, "is the winner with a score of:", max_score)
