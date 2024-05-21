class ATM:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"${amount} deposited successfully."
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"${amount} withdrawn successfully."

def main():
    atm = ATM(100)  # Initial balance set to $100 for demonstration purposes

    while True:
        print("\nATM Main Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            balance = atm.check_balance()
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            message = atm.deposit(amount)
            print(message)
        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            message = atm.withdraw(amount)
            print(message)
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
