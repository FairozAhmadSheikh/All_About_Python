import random

outcomes=("rock","paper","scissor")
print("Welcome to Rock Paper Scissors game ")
while True:
    player=input("Enter Your Choice  (Q to quit)? :").lower()
    computer=random.choice(outcomes)
    if player==computer:
        print("That was a Tie")
        print(f"Computer Choose {computer} , You Choose {player}")
    elif player=="rock" and computer=="scissor":
        print("You Win")
        print(f"Computer Choose {computer} , You Choose {player}")
    elif player=="scissor" and computer=="paper":
        print("You Win")
        print(f"Computer Choose {computer} , You Choose {player}")
    elif player=="paper" and computer=="rock":
        print("You Win")
        print(f"Computer Choose {computer} , You Choose {player}")
    elif player=="q":
        print("Thnks for Playing ")
        break
    else:
        print("Computer Wins")
        print(f"Computer Choose {computer} , You Choose {player}")