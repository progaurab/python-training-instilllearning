class BankAccount: 
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficent balance")
        else:
            self.balance -= amount
        return self.balance
    
# create two objects for the BankAccount Class
    account1 = BankAccount('Gaurab Kumar', 5000)
    account2 = BankAccount('Vince Tiwari', 6000)

    print(account1.deposit(2000))
    print(account2.deposit(3000))

    print(account1.withdraw(4000))
    print(account2.withdraw(4000))


    100?? 
    small ?