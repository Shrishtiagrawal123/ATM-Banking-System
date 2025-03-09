#ATMMainProg.py
from ATMOperations import deposit,withdraw,balenq
from ATMExcept import DepositError, InSuffFundError, WithdrawError
from ATMMenu import menu
while(True):
    try:
        menu()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                    deposit()
                except ValueError:
                    print("\tDon't Enter alnums,strs and symbols for Deposit")
                except DepositError:
                    print("\tDon't Enter -Ve OR Zero for Depositing Amount")
            case 2:
                try:
                    withdraw()
                except ValueError:
                    print("\tDon't Enter alnums,strs and symbols for Withdraw")
                except WithdrawError:
                    print("\tDon't Enter -Ve OR Zero for Withdrawing Amount")
                except InSuffFundError:
                    print("\tUr Account Does not have Suff Funds")
            case 3:
                balenq()
            case 4:
                print("Thx for this Program")
                break
            case _:
                print("Ur Selection of Operation is Wrong-Try again")
    except ValueError:
        print("Ur Choice Should not be alnums,strs and symbols-try again")