from random import randint
# rock paper scissors game

print("Welcome to rock-paper-scissors-gamble!")
score = 0 # score is counted throughout
i = 1 # count round number
play_again = True # play-again value

while play_again == True:
    comp_hand = int(randint(1,4))
    if comp_hand == 1: # if statement converts random number to string
        comp_hand = str("rock")
    elif comp_hand == 2:
        comp_hand = str("paper")
    elif comp_hand == 3:
        comp_hand = str("scissors")
    elif comp_hand == 4:
        comp_hand = str("gamble")
    player_hand = str(input("\nRound " + str(i) + ") Enter your hand now (r,p,s), or (g) to \"gamble\": ")).lower()
    if comp_hand == str("rock"): # checks player hand values
        if player_hand == str("r"):
            print("Its a tie!")
        elif player_hand == str("p"):
            print("You win!")
            score = score + 1
        elif player_hand == str("s"):
            print("Sorry, you lose.")
            score = score - 1
        elif player_hand == str("g"):
            print("Not successful:(")
            score = score - 7
    elif str(comp_hand) == str("paper"):
        if str(player_hand) == str("r"):
            print("Sorry, you lose.")
            score = score - 1
        elif str(player_hand) == str("p"):
            print("Its a tie!")
        elif str(player_hand) == str("s"):
            print("You win!")
            score = score + 1
        elif player_hand == str("g"):
            print("Not successful:(")
            score = score - 7
    elif str(comp_hand) == str("scissors"):
        if str(player_hand) == str("r"):
            print("You win!")
            score = score + 1
        elif str(player_hand) == str("p"):
            print("Sorry, you lose.")
            score = score - 1
        elif str(player_hand) == str("s"):
            print("Its a tie!")
        elif player_hand == str("g"):
            print("Not successful:(")
            score = score - 7
    elif str(comp_hand) == str("gamble"): # gamble condition
        if str(player_hand) == str("r"):
            print("You win!")
            score = score + 1
        elif str(player_hand) == str("p"):
            print("You win!")
            score = score + 1
        elif str(player_hand) == str("s"):
            print("You win!")
            score = score + 1
        elif player_hand == str("g"):
            print("Jackpot!")
            score = score + 20
    i = i + 1
    play_again = str(input("Your score is currently " + str(score) + ". Would you like to play again? (y/n): ")).lower() # play again redefine
    if play_again == str("y"):
       play_again = True
    else:
       play_again = False
    
print("\nYour ending score is " + str(score) + ". Thank you for playing!") # final score printout