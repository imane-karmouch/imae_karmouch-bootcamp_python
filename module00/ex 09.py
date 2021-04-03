import random 
n=random.randint(1,99)
print("This is an interactive guessing game!You have to enter a number between 1 and 99 to find out the secret number.Type 'exit' to end the game.Good luck!")
m=int(input("What's your guess between 1 and 99?"))
coup=0
while (m != n):
    if (n> m):
        print("Too low!");
    else:
        if (n < m):
            print("Too high!");
    m=int(input("What's your guess between 1 and 99?"))
    coup+=1
print ("Congratulations, you've got it in :",coup,"tries");
