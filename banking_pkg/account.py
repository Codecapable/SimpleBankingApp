from os import name


def show_balance(balance):
    print("Current Balance: $", (float(balance)))


def deposit(balance):
    amount = float(input("Enter amount to deposit:"))
    return balance + amount


def withdraw(balance):
    amount = float(input("Enter amount to withdraw:"))
    if float(amount) > balance:
        print("Where are you going to get that kind of money?")
        return balance
    else:
        return balance - amount


def logout(name):
    print("Goodbye", name + "!")
