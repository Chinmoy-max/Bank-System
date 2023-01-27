"""Banking System using OOPs

Parent class: User
⦁	Holds details about an user
⦁	Has a function to show user details

Child Class: Bank
⦁	Stores details about account balance
⦁	Stores details about the amount
⦁	Allows for deposits,withdraw,view_balance"""


# Parent class
class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal Details")
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender", self.gender)


# Child class

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.amount = None
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance += amount
        print("Account balance has been updated : $", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Balance | Balance Available : $", self.balance)
        else:
            self.balance -= amount
            print("Account balance has been updated : $", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account Balance is : $", self.balance)


Sumit = Bank('Sumit', 26, "Male")
Sumit.show_details()
Sumit.deposit(500)
Sumit.withdraw(600)
Sumit.withdraw(200)
Sumit.view_balance()
