class Bank:
    Account_type = "Savings"
    location = "Guntur"

    def __init__(self, name, Account_Number, balance):
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_type = Bank.Account_type
        self.location = Bank.location

    def __repr__(self):
        print("Welcome to the SBI ATM Machine")
        print("------------------------------------")

        account_pin = int(input("Please enter your pin number: "))

        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()

        return ' '.join([self.name, self.Account_Number])

    def Error(self):
        account_pin = int(input("Please enter your pin number: "))
        if account_pin == 123:
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            self.Error()

    def Account(self):
        print("Your Card Number is: XXXX XXXX XXXX 1337")
        print("Would you like to deposit / withdraw / check balance?")
        print("""
1) Balance
2) Withdraw
3) Deposit
4) Quit
""")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Your balance is:", self.balance)
            self.Account()

        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Withdraw successful! New balance:", self.balance)
            else:
                print("Insufficient funds!")
            self.Account()

        elif choice == 3:
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            print("Deposit successful! New balance:", self.balance)
            self.Account()

        elif choice == 4:
            print("Thank you for using SBI ATM!")
        else:
            print("Invalid choice. Try again.")
            self.Account()


# Chạy thử
user = Bank("An User", "1234-5678-9999", 5000)
print(user)
