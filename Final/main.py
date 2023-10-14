from user import User ,Bank,Admin

bank = Bank()
admin = Admin(bank)

user1 = admin.create_account("Nabel", "nabel@example.com", "Mirpur,Dhaka", "Savings")
user2 = admin.create_account("morshed", "morshed2@example.com", "Dhanmondi,Dhaka", "Current")


while(True):
    print()
    print("-------------------------")
    print(f" Welcome to Phitron_Bank ")
    print("-------------------------")
    print()
    print("1. Admin")
    print("2. User")
    print("3. EXIT!!!")
    print("select an option: ",end=' ')
    x=int(input( ))

    if (x==1):  #ADMIN
        while(True):
            print()
            print("1. Create an Account")
            print("2. Delete User Account")
            print("3. User Account List")
            print("4. Check Total available Balance")
            print("5. Check Total Loan Amount")
            print("6. Enable/Disable Loan Feature!!!")
            print("7. EXIT")
            print("select an option: ",end=' ')
            z=int(input( ))

            if z==1:
                print()
                print('User Name: ',end="")
                name=input()
                print('email ',end="")
                email=input()
                print('Address: ',end="")
                address=input()
                print('Account Type: Savings/Current ',end="")
                type=input()
                admin.create_account(name,email,address,type)
            elif z==2:
                print()
                print("User Account Number: ",end=" ")
                id=int(input())
                admin.delete_account(id)
                print(f'Account Number {id} deleted!!!')
            elif z==3:
                print()
                admin.see_all_accounts()
            elif z==4:
                print()
                admin.check_total_balance()
            elif z==5:
                print()
                admin.check_total_loan()
            elif z==6:
                print()
                print("If want to disable --> False ")
                print("If want to enable --> True ",end=' ')
                x=input()
                admin.toggle_loan_feature(x)
            elif z==7:
                break
            else:
                print("You select wrong option!!!")
                break

    elif x==2:  #USER
        print("Give your id: ",end=' ')
        id=int(input( ))
        if id in bank.users:
            user= bank.users[id]
        else:
            print("No user Found!!!")
            continue
        print()
        print("USER INFO!!!")
        print(user)
        print()
        while (True):
            print()
            print("1. Deposit")
            print("2. withdraw")
            print("3. Transfer Amount") #******
            print("4. Take Loan")
            print("5. Check Balance")
            print("6. Transaction history")
            print("7. EXIT")
            print("select an option: ",end=' ')
            y=int(input( ))

            if y==1:
                print("Amount= ",end=" ")
                a=int(input( ))
                user.deposit(a)
                print(f"Deposited ${a}")
                print()
            elif y==2:
                print("Amount= ",end=" ")
                a=int(input( ))
                user.withdraw(a)
                print()
            elif y==3:
                print()
                print("Whom you want to transfer? Give the ID:- ",end=' ')
                id=int(input( ))
                if id in bank.users:
                    user2= bank.users[id]
                else:
                    print("Account Doesn't Exist!!!")
                    break
                print("Transferal Amount: ",end=" ")
                amount=int(input())
                user.transfer(user2,amount)
            elif y==4:
                print("Loan Amount= ",end=" ")
                a=int(input( ))
                user.take_loan(a)
                print()
            elif y==5:
                user.check_balance()
                print()
            elif y==6:
                user.check_transactions()
                print()
            elif y==7:
                break
            else:
                print("You select wrong option!!!")
                break

    elif x==3:  #EXIT
        break 
    else:
        print("You select wrong option!!!")