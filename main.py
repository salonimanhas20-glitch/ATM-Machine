from display_balance import give_balance
from deposit_money import deposit
from withdraw_money import withdraw
from statement import show_statement

def atm():
    while True:
        print("\n1- Deposit money")
        print("2-Display Balance")
        print("3- Withdraw money")
        print("4- Statement")
        print("5- Exit")
        choice = int(input("Enter your choice: "))
        
        if (choice==1):
            deposit()
        elif (choice==2):
            give_balance()
        elif (choice==3):
            withdraw()
        elif (choice==4):
           show_statement()
        elif (choice==5): 
            print("Thank you for using the ATM Machine..")
            break
        else:
            print("Invalid choice")
            
atm()