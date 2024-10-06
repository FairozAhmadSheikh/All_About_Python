# Python Slot Machine

import random


def spin_row():
    symbols=['🍒','🍉','🍋','🔔','⭐']
    result=[ random.choice(symbols) for _ in range(3)]
    return result

def print_row(row):
    print("***************")
    print(" | ".join(row))
    print("***************")


def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet*6
        elif row[0]=="🍉":
            return bet*12
        elif row[0]=="🍋":
            return bet*18
        elif row[0]=="🔔":
            return bet*36
        elif row[0]=="⭐":
            return bet*72
    return 0


def main():
    balance=100
    print("*************************")
    print(" Welcome to Python Slots ")
    print(" Symbols:  🍒🍉🍋🔔⭐  ")
    print("*************************")
    
    while balance>0:
        # Your Initial Balance 
        print(f"Your Current balance is {balance}")
        
        # Place Bet Amount 
        bet_amount=input("Place Your Bet Amount : ")
        
        # Check whether bet is a digit or not
        if not bet_amount.isdigit():
            print("Please Enter a Valid Amount ")
            continue
        
        # Convert bet amount into integer
        bet_amount=int(bet_amount)
        
        # Check if bet amount should not be greater than balance  
        if bet_amount>balance:
            print("Insufficent Balance ")
            continue
        
        # Condition to Check Whether the bet amount should not be  0 or negative 
        if bet_amount<=0:
            print("Bet Must be greater than 0")
            continue
        
        # Deduct Bet Amount 
        balance-=bet_amount
        
        # Spin Wheel Now
        row=spin_row()
        print("Spinning.......\n")
        # Display row using print_row function
        print_row(row)
        
        # Winning Case 
        payout=get_payout(row,bet_amount)
        if payout>0:
            print(f"You won ${payout}")
        else:
            print(f"You Lost This Round ")       
        
        #Balance Update
        balance+=payout 
        
        # Stop Condition
        play_again=input("Do You want to play again (Y/N)?").upper()
        if play_again !="Y":
            break
    print("***************************")
    print(f"Your Final Balance is ${balance}")
    print("***************************")
# Dunder method main executes        
if __name__=='__main__':
    main()