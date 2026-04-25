import utils
from utils import transactions
def withdraw():
    money=float(input("enter money to  be withdrawn"))
    if(money<=0):
        print("Invalid amount")
    elif(money>utils.balance):
        print("Insufficient balance")
    else:
        utils.balance=utils.balance-money
        print("Money withdrawn successfully")
        print("Remaining balance:",utils.balance)
    transactions.append("Withdrawal money="+str(utils.balance))


