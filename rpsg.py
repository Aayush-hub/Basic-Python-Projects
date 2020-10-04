# Rock,paper and scissor
while(True):
    print("Welcome to Rock,paper and scissor Game")
    name=input("Enter your name:\n")
    print(f"Hi {name},\n We will play Rock,paper and scissor Game for 10 times &\n then, I will tell your score \n So Let the game begin.")

    import random
    i = 0
    z = 0
    d=0
    l=0
    while (i < 10):
        o = random.randint(0, 2)
        # o=0 is rock, o=1 is paper, o=2 is scissor
        x = input("Enter your choice(rock,paper and scissor):\n")
        oh = x.lower()
        if o == 0 and oh == "rock":
            d=d+1
            print("It's a draw")
        elif o == 1 and oh == "paper":
            d = d + 1
            print("It's a draw")
        elif o == 2 and oh == "scissor":
            d = d + 1
            print("It's a draw")
        elif o == 0 and oh == "paper":
            z = z + 1
            print("You won this time")
        elif o == 0 and oh == "scissor":
            l=l+1
            print("You lose this time")
        elif o == 1 and oh == "rock":
            l=l+1
            print("You lose this time")
        elif o == 1 and oh == "scissor":
            z = z + 1
            print("You won this time")
        elif o == 2 and oh == "rock":
            z = z + 1
            print("You won this time")
        elif o == 2 and oh == "paper":
            l=l+1
            print("You lose this time")
        else:
            print("enter a valid choice")
        i = i + 1
    print(f"you won {z} times,lose {l} time and it was a draw {d} times.")
    import time
    time=time.asctime(time.localtime(time.time()))
    yn=input("Would you like to see scoreboard?\n")
    y=yn.lower()
    f=open("rockpaperandscissorgame.txt","a")
    f.write(f"At {time}, {name} won {z} times,lose {l} time and it was a draw {d} times.\n")
    f.close()
    if y=="yes":
        f=open("rockpaperandscissorgame.txt")
        print(f.read())
        print("Thank You")
        f.close()
    else:
        print("Thank You \n Hope You will play again")
    play1=input("Would you like to play again?:\n")
    if play1.lower()=="yes":
        pass
    else:
        break
