# Banking Program

balance=0
is_running=True

def check_balance():
    return f"Your Balance is ${balance:.2f}"

def deposit():
    amount=float(input("Enter Amount To Deposit : "))
    if amount>0:
        print(f"Sucessfully Deposited Amount ${amount}")
        return amount
    else:
        print(f"You cant deposit {amount} try valid amount")
        return 0

def withdrawl():
    amount=float(input("Enter Amount To Withdraw : "))
    if amount>balance:
        print("Insufficent Funds ")
        return 0
    elif amount<=0:
        print(f"You cant withdraw {amount} try valid amount")
        return 0
    else:
        print(f"Withdrawal Sucess for Amount ${amount}")
        return amount
        
while is_running:
    print("Welcome to Banking Program ".center(40,"*"))
    print("1. Balance Enquiry ")
    print("2. Deposit  ")
    print("3. Withdrawl ")
    print("4. Exit ")
    user_input=int(input("Enter Your choice (1-4)"))
    
    match user_input:
        case 1:
            print(check_balance())
        case 2:
           balance+= deposit()
        case 3:
            balance-=withdrawl()
        case 4:
            is_running=False
        case _:
            print("Invalid Choice Seleceted ")
            
print("Thanks Have a Nice Day ! ")