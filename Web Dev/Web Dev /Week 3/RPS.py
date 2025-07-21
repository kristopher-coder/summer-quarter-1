# build a RPS game 
# 2-players 
# each player picks bewtween rock paper or scissors
# each players choice is compared:
# Rock < Scissors 

def RPS():
    player1 = input("player 1, please enter your name: ")
    player2 = input("player 1, please enter your name: ")

    p1_choice = input(f"{player1}, choose bewtween Rock, Paper, Scissors ").lower().strip()

    while not IsValidmove(p1_choice):
        print("InvalidMove please try again")
        p1_choice = input(f"{player1}, choose bewtween Rock, Paper, Scissors ").lower().strip()


    p2_choice = input(f"{player2}, choose bewtween Rock, Paper").lower().strip()

    while not IsValidmove(p2_choice):
        print("InvalidMove please try again")
        p2_choice = input(f"{player2}, choose bewtween Rock, Paper, Scissors ").lower().strip()


    if p1_choice == "rock" and p2_choice =="paper":
        print(f"Rock beats Sciossrs, {player1} wins")
    elif p1_choice == "scissors" and p2_choice == "paper":
        print(f"paper beats rock ,  {player1} wins!")
    elif p1_choice == "paper" and p2_choice == "rock":
        print(f"paper beats rock ,  {player1} wins!")
     
    elif p2_choice == "rock" and p1_choice == "paper":
        print(f"paper beats rock ,  {player1} wins!")

    elif p2_choice == "scissors" and p1_choice == "paper":
        print(f"paper beats rock ,  {player1} wins!")

    elif p2_choice == "paper" and p1_choice == "rock":
        print(f"paper beats rock ,  {player2} wins!")





def IsValidmove(playermove):
    validmoves = ["rock", "paper", "scissors"]

    if playermove in validmoves: 
        return True
    else:
        return False 

RPS() 

