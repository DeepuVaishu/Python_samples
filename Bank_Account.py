
class Bank_Account:
    def __init__(self,user_id,password,balance = 0):
        self.user_id = user_id
        self.password = password
        self.balance = balance

    def login(self,password):
        if self.password == password:
            print("Login successful")
            return True
        else:
            print("Invalid password")
            return False

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited amount: {amount} , Current balance: {self.balance}")
        else:
            print("Invalid deposit")

    def withdraw(self,amount):
        if amount>0 and amount <= self.balance:
            self.balance -= amount
            print(f"Amount Withdrawn: {amount}, Current Balance: {self.balance}")
        else:
            print("You have no sufficient balance")

    
accounts = {} 

def create_new_account():
    user_id = input("Create your user_id: ")
    if user_id in accounts:
        print("User_id already exists! Try a different name for your account.")
        return None
    
    password = input("Create a password: ")
    balance = float(input("Enter initial deposit (optional, default is 0): ") or 0)
    new_user = Bank_Account(user_id, password, balance)
    accounts[user_id] = new_user
    print(f"Account created successfully for {user_id}!")
    
def login():
    user_id = input("Enter your user_id: ")
    if user_id in accounts:
        user = accounts[user_id]
        password = input("Enter your password:")
        if user.login(password):
            return user
    else:
        print("This account does not exist!")
    return None 
    
def main():
    while True:
        print("Welcome to Oops Banking system")
        print("1. Create an account")
        print("2. Login to existing accont")
        print("3. Exit")
        num = int(input("Enter your choice: "))
        if num == 1:
            create_new_account()
        elif num == 2:
            user = login()
            if user:
                while True:
                    print("1. Deposit")
                    print("2. Withdrawal")
                    print("3. Log out")
                    num1 = int(input("Choose your action: "))
                    if num1 == 1:
                        amount = float(input("Enter amount to deposit: "))
                        user.deposit(amount)
                    elif num1 == 2:
                        amount = float(input("Enter amount to withdraw: "))
                        user.withdraw(amount)
                    elif num1 == 3:
                        print("Logged out!")
                        break
            else:
                print("Invalid choice! Please try again.")
        elif num == 3:
            print("Thank you for using the banking system. Goodbye!")
            break
        else:
            print("Invalid choice")

main()
