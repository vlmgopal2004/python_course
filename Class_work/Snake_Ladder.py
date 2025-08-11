import random

player1_score = 0
player2_score = 0
snakes = {3:0,99:54,77:49,21:12,96:5,50:20,19:9,80:40}
ladders = {2:17,13:63,10:98,24:76,33:56,79:84,88:92}
while player1_score < 100 and player2_score < 100:
    player1 = input("[s]top and [c]ontinue: ")
    if player1 == 'c':
        player1_turn = random.randint(1,6)
        player1_score += player1_turn
        if player1_score in snakes:
            player1_score = snakes[player1_score]
            print(f"Player-1 ---- Snake Bit ---- score: {player1_score} - Dice:{player1_turn}")
        elif player1_score in ladders:
            player1_score = ladders[player1_score]
            print(f"Player-1 **** Ladder **** score: {player1_score} - Dice:{player1_turn}")
        print(f"Player-1 Score: {player1_score} - Dice:{player1_turn}")
    else:
        print("Player-2 Win")
        break
    player2 = input("[s]top and [c]ontinue: ")
    if player2 == 'c':
        player2_turn = random.randint(1,6)
        player2_score += player2_turn
        if player2_score in snakes:
            player2_score = snakes[player2_score]
            if player2_score in snakes:
                player2_score = snakes[player2_score]
                print(f"Player-2 ---- Snake Bit ---- score: {player2_score} - Dice:{player2_turn}")
            elif player2_score in ladders:
                player2_score = ladders[player2_score]
                print(f"Player-2 **** Ladder **** score: {player2_score} - Dice:{player2_turn}")
        print(f"Player-2 Score: {player2_score} - Dice:{player2_turn}")
    else:
        print("Player-1 Win")

if player1_score > player2_score:
    print("\nPlayer-1 win")
elif player2_score > player1_score:
    print("\nPlayer-2 win")
else:
    print("Tie")