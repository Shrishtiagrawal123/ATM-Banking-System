#ATMOperations.py
from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500.00
def deposit():
    damt=float(input("Enter How Much Amount u want to Deposit:")) #ValueError
    if(damt<=0):
        raise DepositError
    else:
        global bal
        bal=bal+damt
        print("Ur Account xxxxx123 Credited with INR:{}".format(damt))
        print("Now Ur Account xxxxx123 Balance:{}".format(bal))
def withdraw():
    global bal
    wamt = float(input("Enter How Much Amount u want to Withdraw:"))  # ValueError
    if(wamt<=0):
        raise WithdrawError
    elif(wamt>bal):
        raise InSuffFundError
    else:
        bal=bal-wamt
        print("Ur Account xxxxx123 debitted  with INR:{}".format(wamt))
        print("Now Ur Account xxxxx123 Balance:{}".format(bal))

def balenq():
    print("Ur Account xxxxx123 Balance:{}".format(bal))
