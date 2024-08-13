import time

print("Please insert your CARD")
time.sleep(2)  # Card reading time

# Initial details
password = 1234 # Default PIN, can be changed
balance = 5000
transaction_history = []  # To store transaction details

# Function to display menu options
def display_menu():
    print("""
    ==========================================================
    1 == Balance Inquiry
    2 == Withdraw Balance
    3 == Deposit Balance
    4 == Change PIN
    5 == Transaction History
    6 == Exit
    ==========================================================""")

# Function to add transactions to history
def add_transaction(transaction):
    transaction_history.append(transaction)

# Takes pin input
pin = int(input("Enter your ATM PIN: "))

if pin == password:
    while True:
        display_menu()
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option.")
            continue
        
        if option == 1:
            print(f"Your current balance is {balance}")
        
        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            if withdraw_amount > balance:
                print("Insufficient balance.")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account.")
                print(f"Your updated balance is {balance}")
                add_transaction(f"Withdraw: -{withdraw_amount}")

        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account.")
            print(f"Your updated balance is {balance}")
            add_transaction(f"Deposit: +{deposit_amount}")

        elif option == 4:
            new_pin = int(input("Enter your new PIN: "))
            password = new_pin
            print("Your PIN has been successfully changed.")

        elif option == 5:
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions yet.")

        elif option == 6:
             # Exit the program
            print("Thank you for using the ATM. Have a great day!")
            break

        else:
            print("Invalid option. Please try again.")
else:
    print("Wrong PIN, Please try again.")