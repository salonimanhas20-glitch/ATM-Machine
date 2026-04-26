import utils
from utils import transactions
def deposit():
     money = float(input("enter money to be deposited"))
     if(money>0):
          utils.balance=utils.balance+money
          transactions.append("deposited  money="+str(utils.balance))

          print("Money deposited and Balance updated")
     else:
          print("Invalid amount!!!") 