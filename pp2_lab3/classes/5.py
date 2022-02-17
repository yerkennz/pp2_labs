class Account():
    owner = " "
    balance = 0
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: {self.balance}'
    
    def deposit(self, money):
        self.balance += money
        return "Deposit Accepted"

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            return "Withdrawl Accepted:"
        return "Unavailable!"

person = Account("Nursultan", 50000)
print(person.deposit(5000))
print(person)
print(person.deposit(5000))
print(person.withdraw(48000))
print(person)