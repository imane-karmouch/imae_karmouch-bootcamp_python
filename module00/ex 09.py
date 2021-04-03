import random 
n=random.randint(1,99)
m=int(input("donner un nombre"))
coup=0
while (m != n):
    if (n> m):
        print("Too low!");
    else:
        if (n < m):
            print("Too high!");
    m=int(input("donner un nombre"))
    coup+=1
print ("Congratulations, you've got it in :",coup,"tries");
