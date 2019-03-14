class BankAccount():
    def __init__(self, account_number, account_name, balance=0.00):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance
    def open(self):
        self.account_name = input("Enter account name: ")
        self.account_number = input("enter account number: ")
        self.balance = 0
        print("Hello!" + self.account_name + " " + "Green Bank welcomes you!")
        # print("here is your account number")
    def deposit(self, amount):
        self.balance += amount
        print(input("enter acccount name: "))
        print(input("enter account number: "))
        print(input("enter amount to deposit: "))
        print("you have deposited" + " " + str(deposit) + " " + "thank you for depositing with Green bank")
    def withdrawal(self,amount):
        self.balance >= amount
        self.balance -= amount
        print(input("enter account name: "))
        print(input("enter account number: "))
        print(input("enter amount to withdraw: "))
        print("You have withdrawed" + " " + str(withdraw))
        
    def get_balance(self, amount):
        self.account_name = input("enter account name: ")
        self.account_number =  input("enter account number: ")
        print("your account balance is:\t" + str(self.balance))
    def delete_account(self, close):
        self.account_name == close
        self.account_number == close
        print("Your account is successfully deleted")
            
        
            
 #class instantiation
account = BankAccount("ac23663455", "dodo" )
account.deposit(200000)
account.withdraw(100000)
print("Welcome to Green bank!\nPlease select on one of the options below:")
print("1. open an account")
print("2.Deposit money")
print("3. Withdraw money")
print("4. Check account balance")
print("5. close account")
select = input("Please select an option: ")
selection = int(select)
if selection == 1:
    account.open
elif selection == 2:
    account.deposit
elif selection == 3:
    account.withdrawal
elif selection == 4:
    account.get_balance
elif selection == 5:
    account.delete_account

 

    
    




