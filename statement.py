from utils import transactions
def show_statement():
    if(transactions==[]):
        print(" No transactions performed")
    else:
        print(transactions)
        