
from banking_pkg import account

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
name = input("Enter name to register:")
if len(name) > 10:
    print("The maximum name length is 10 characters")
    name = input("Enter name to register:\nYou must enter a name. ")


pin = input("Enter PIN:")
if len(pin) > 4:
    print("The maximum pin length is 4 characters")
    pin = input("Enter a pin to register:\nYou must create a pin. ")


balance = 0
print(name, "has been registered with a starting balance of $" + str(balance))

while True:

    print("LOGIN")
    name_login = input("Enter name:")
    pin_login = input("Enter PIN:")

    if name_login != name or pin_login != pin:
        print("Invalid credentials!")

    elif name_login == name and pin_login == pin:
        print("Login successful!")
        break

while True:

    atm_menu(name)
    option = input("Choose an option:")

    if option == "1":
        account.show_balance(balance)

    elif option == "2":
        balance = account.deposit(balance)

        account.show_balance(balance)

    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)

    elif option == "4":
        account.logout(name)
        break
    else:
        print("Choose a valid option")
