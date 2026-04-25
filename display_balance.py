import utils
from utils import transactions
def give_balance():
    if(utils.balance==0):
        print(" No balance")
    else:
        print("Current  balance is :",utils.balance)
    transactions.append("Current balance="+str(utils.balance))
