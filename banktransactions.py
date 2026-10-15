class Bank:
    def __init__(self, owner, balance, history):
        self.owner = owner
        self.balance = balance
        self.history = history
    def deposit(self, money):
        self.balance += money
        print(f"Your balance is now {self.balance}")
    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
            print(f"Your balance is now {self.balance}")
        else:
            print(f"You do not have enough in your account! Your balance is {self.balance}")



historylist = []
firstuser = Bank("Colm", 0, historylist)
while True:
    print("Welcome to Bank of Colm")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. View transaction history")
    print("5. Exit")

    string = False

    try:
        action = int(input("Please enter action from 1-5: "))
    except ValueError:
        print("Please enter an integer from 1-5.")

    if action == 1:
        print(f"Balance: {firstuser.balance}")

    elif action == 2:
        print(f"Current Balance: {firstuser.balance}")
        amount = input("Please enter amount of money you would like to deposit: £")
        firstuser.deposit(int(amount))
        historylist.append(f"Deposited {amount}")

    elif action == 3:
        initialbalance = firstuser.balance
        print(f"Current Balance: {firstuser.balance}")
        amount = input("Please enter amount of money you would like to withdraw: £")
        firstuser.withdraw(int(amount))
        if initialbalance != firstuser.balance:
            historylist.append(f"Withdrew {amount}")

    elif action == 4:
        index = 1
        for transaction in historylist:
            print(f"{index}. {transaction}")
            index += 1

    elif action == 5:
        print("Goodbye!")
        break

    elif action > 5 or action < 1:
        print("Please enter a number from 1-5!")
