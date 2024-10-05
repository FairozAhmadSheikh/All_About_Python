import random
# Number Guessing Game
start_num=10  # Starting range 
end_num=20      # Ending range
answer=random.randint(start_num,end_num)
is_Running=True
chances=0
print(answer)
while is_Running:
    guess=input("Enter Your Guess (10-20) : ") 
    if guess.isdigit():
        guess=int(guess)
        if guess>end_num or guess<start_num:
            print(f"Please Start from {start_num} to {end_num}")
        elif guess==answer:
            print(f"Correct Guess , Number was {answer}")
            chances+=1
            print(f"It took you {chances} chances ")
            is_Running=False
        elif guess>answer:
            print("Too high Entered Try Lower Value")
            chances+=1
        elif guess<answer:
            print("Too low Entered Try Higher value")  
            chances+=1
    else:
        print("Not A Valid Guess")
        print(f"Please enter a valid guess starting from {start_num} till {end_num}")
    
        