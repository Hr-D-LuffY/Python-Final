class Bank:
    def __init__(self):
        self.users = {}
        self.users_info={}

class User:
    user_count = 1
    loan_amount=0
    loan_enable=True

    def __init__(self, name, email, address, account_type):
        self.account_number = User.user_count
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan_limit = 2
        self.transactions = []
        self.active = True
        User.user_count += 1

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")
        

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
            return
        self.balance -= amount
        self.transactions.append(f"Withdrew ${amount}")
        print(f"Withdrew ${amount}")

    def check_balance(self):
        print(f"Available balance: ${self.balance}")

    def check_transactions(self):
        print(self.transactions)

    def take_loan(self, amount):
        if User.loan_enable==True:
            if self.loan_limit > 0:
                self.balance += amount
                self.loan_limit -= 1
                User.loan_amount+=amount
                self.transactions.append(f"Took a loan of ${amount}")
            else:
                print("You have already taken the maximum allowed loans.")
        else:
            print("Bank Disable the Loan Feature")

    def transfer(self, recipient, amount):
        if recipient.active:
            if amount > self.balance:
                print ("Transferal amount exceeded")
                return
            self.balance -= amount
            recipient.deposit(amount)
            self.transactions.append(f"Transferred ${amount} to account {recipient.account_number}")
        else:
            print("Account does not exist.")

    def is_bankrupt(self):
        return "The bank is bankrupt" if self.balance < 0 else ""

    def __str__(self):
        return f"Account Number: {self.account_number}\nName: {self.name}\nEmail: {self.email}\nAddress: {self.address}\nAccount Type: {self.account_type}\nBalance: ${self.balance}\n"


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        self.bank.users[user.account_number] = user  
        user_info = f"Account Number: {user.account_number}\nName: {user.name}\nEmail: {user.email}\nAddress: {user.address}\nAccount Type: {user.account_type}\nBalance: ${user.balance}\n"
        self.bank.users_info[user.account_number] = user_info  
        return user

    def delete_account(self, user_id):
        if user_id in self.bank.users:
            del self.bank.users[user_id] 
        if user_id in self.bank.users_info:
            del self.bank.users_info[user_id]  

    def see_all_accounts(self):
        for user_info in self.bank.users_info.values():
            print(user_info)

    def check_total_balance(self):
        total_balance = sum(user.balance for user in self.bank.users.values() if user.active)
        print(f"Total available balance in the bank: ${total_balance}")
        return total_balance

    def check_total_loan(self):
        total_loan=User.loan_amount
        print(f"Total loan amount in the bank: ${-total_loan}")

    def toggle_loan_feature(self, enable):
        User.loan_enable = False 


