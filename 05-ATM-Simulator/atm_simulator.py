# ATM Simulator

customers = {}

def create_account():
    # New customer ka account create karna
    name = input("Enter your name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    account_number = str(1001 + len(customers))

    while True:
        pin = input("Set your 4-digit PIN: ")

        if len(pin) == 4 and pin.isdigit():
            break

        print("PIN must be exactly 4 digits.")

    while True:
        try:
            initial_deposit = float(input("Enter initial deposit: "))

            if initial_deposit < 0:
                print("Deposit cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid amount.")

    customers[account_number] = {
        "name": name,
        "pin": pin,
        "balance": initial_deposit,
        "transactions": []
    }

    customers[account_number]["transactions"].append(
        f"Account created - Deposit: ₹{initial_deposit:.2f}"
    )

    print("\nAccount created successfully!")
    print("Your Account Number:", account_number)


def login_customer():
    # Existing customer ka login
    account_number = input("Enter account number: ").strip()

    if account_number not in customers:
        print("Account not found.")
        return

    customer = customers[account_number]
    attempts = 3

    while attempts > 0:
        pin = input("Enter your PIN: ")

        if pin == customer["pin"]:
            print(f"\nWelcome, {customer['name']}!")
            atm_menu(customer)
            return

        attempts -= 1
        print(f"Incorrect PIN. Attempts left: {attempts}")

    print("Login failed.")


def check_balance(customer):
    # Customer ka current balance dikhana
    print(f"Available Balance: ₹{customer['balance']:.2f}")


def withdraw_money(customer):
    # Account se money withdraw karna
    try:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")

        elif amount > customer["balance"]:
            print("Insufficient balance.")

        else:
            customer["balance"] -= amount

            customer["transactions"].append(
                f"Withdrawal: ₹{amount:.2f}"
            )

            print(f"Please collect your cash: ₹{amount:.2f}")
            print(f"Remaining Balance: ₹{customer['balance']:.2f}")

    except ValueError:
        print("Please enter a valid amount.")


def deposit_money(customer):
    # Account mein money deposit karna
    try:
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")

        else:
            customer["balance"] += amount

            customer["transactions"].append(
                f"Deposit: ₹{amount:.2f}"
            )

            print(f"₹{amount:.2f} deposited successfully.")
            print(f"Updated Balance: ₹{customer['balance']:.2f}")

    except ValueError:
        print("Please enter a valid amount.")


def show_mini_statement(customer):
    # Last transactions dikhana
    print("\nMini Statement")

    if not customer["transactions"]:
        print("No transactions found.")
        return

    for transaction in customer["transactions"][-5:]:
        print(transaction)


def atm_menu(customer):
    # Customer ke liye ATM menu
    while True:
        print("\nATM Menu")
        print("1. Balance Enquiry")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Mini Statement")
        print("5. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance(customer)

        elif choice == "2":
            withdraw_money(customer)

        elif choice == "3":
            deposit_money(customer)

        elif choice == "4":
            show_mini_statement(customer)

        elif choice == "5":
            print("You have been logged out.")
            break

        else:
            print("Invalid choice. Please try again.")


# Main ATM program
while True:
    print("\nATM Simulator")
    print("1. New Customer")
    print("2. Existing Customer Login")
    print("3. Exit")

    main_choice = input("Enter your choice: ")

    if main_choice == "1":
        create_account()

    elif main_choice == "2":
        login_customer()

    elif main_choice == "3":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")