import random
n=random.random()
RN=round(n*100)
GN=int(input("Guess any number from 1 to 100 : "))
game_over=False
G=1
while not game_over:
    if RN==GN:
        print(f"You won,in {G} attempt.")
        game_over=True
    else:
        if GN>RN:
            print("Too high")
            G+=1
            GN=int(input("Guess again : "))
        else:
            print("Too low")
            G+=1
            GN=int(input("Guess again : "))