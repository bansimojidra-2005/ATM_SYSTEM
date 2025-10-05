# ATM System using Dictionary, Functions, Loops, and Conditional Statements

# Dictionary to store user data in the format: name: {"pin": xxxx, "balance": xxxx}

accounts = {
    "urmi": {
        "pin": 1234,
        "name": "Urmi Mojidra",
        "Contact No": 8989899044,
        "balance": 5000
    },
    "rahul": {
        "pin": 1111,
        "name": "Rahul Agrawal",
        "Contact No": 8785343402,
        "balance": 3000
    },
    "neha": {
        "pin": 2222,
        "name": "Neha Jadav",
        "Contact No": 9904894544,
        "balance": 8000
    },
    "binal": {
        "pin": 1244,
        "name": "Binal Patel",
        "Contact No": 8990667780,
        "balance": 5000
    },
    "ram": {
        "pin": 3456,
        "name": "Ram Patel",
        "Contact No": 4589805531,
        "balance": 9000
    },
    "het": {
        "pin": 5678,
        "name": "Het Moradiya",
        "Contact No": 4556789920,
        "balance": 10000
    },
    "umang": {
        "pin": 4569,
        "name": "Umang Mojidra",
        "Contact No": 9989070760,
        "balance": 15000
    }
}


# ADMIN function to show all accounts (Name, PIN, Balance)

def show_all_data():
    print("-------------------------------------------------------------------")
    print("\n--- 📝 All Account Data (Admin View) ---")
    print("-------------------------------------------------------------------")
    print("\nUserName      \tPin     \tBalance")
    print("-------------------------------------------------------------------")
    if len(accounts) == 0:
        print("No accounts available.")
    else:
        for name, data in accounts.items():
            print(f"{name.capitalize()}\t\t{data['pin']}\t\t₹{data['balance']}")

# Function for user login using name + pin

def user_login():
    name = input("Enter your name: ").lower()
    pin = int(input("Enter your PIN: "))
    if name in accounts and accounts[name]["pin"] == pin:
        print(f"\n✅ Welcome {name.capitalize()}!")
        user_menu(name)
    else:
        print("❌ Incorrect name or PIN!")

# After login: user menu to deposit, withdraw, check balance

def user_menu(name):
    while True:
        print(f"\n=== {name.capitalize()} ATM Menu ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Your Balance: ₹{accounts[name]['balance']}")
        elif choice == '2':
            amount = int(input("Enter amount to deposit: ₹"))
            accounts[name]['balance'] += amount
            print(f"₹{amount} deposited successfully! New Balance: ₹{accounts[name]['balance']}")
        elif choice == '3':
            amount = int(input("Enter amount to withdraw: ₹"))
            if amount <= accounts[name]['balance']:
                accounts[name]['balance'] -= amount
                print(f"₹{amount} withdrawn successfully! New Balance: ₹{accounts[name]['balance']}")
            else:
                print("❌ Insufficient balance!")
        elif choice == '4':
            print(f"👋 {name.capitalize()} logged out successfully.")
            break
        else:
            print("Invalid choice!")

# Function to add new account

def add_account():
    name = input("Enter new account holder name: ").lower()
    if name in accounts:
        print("Account already exists!")
    else:
        pin = int(input("Set a 4-digit PIN: "))
        balance = int(input("Enter initial balance: ₹"))
        accounts[name] = {"pin": pin, "balance": balance}
        print(f"✅ Account for {name.capitalize()} added successfully!")

# Function to remove account

def remove_account():
    name = input("Enter account holder name to remove: ").lower()
    if name in accounts:
        del accounts[name]
        print(f"🗑 Account for {name.capitalize()} removed successfully!")
    else:
        print("Account not found!")

# Main Program Loop

while True:
    print("\n===== 🏦 ATM SYSTEM MENU =====")
    print("1. Show All Data (Admin)")
    print("2. User Login (Name + PIN)")
    print("3. Add Account")
    print("4. Remove Account")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        show_all_data()
    elif choice == '2':
        user_login()
    elif choice == '3':
        add_account()
    elif choice == '4':
        remove_account()
    elif choice == '5':
        print("Thank you for using ATM System 😊")
        break
    else:
        print("Invalid choice! Please try again.")
