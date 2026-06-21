import json

try:
    with open("Expensetracker.json", "r") as file:
        expensetracker = json.load(file)
except:
    expensetracker = {}

def save_data():
    with open("Expensetracker.json", "w") as file:
        json.dump(expensetracker, file, indent=4)

def add_expense():
    expense = input("Enter name of the expense: ")

    if expense == "":
        print("Expense can't be empty")
        return

    amount = input("Enter the amount: ")

    expensetracker[expense] = {
        "amount": amount
    }

    save_data()
    print("Expense added successfully")

def view_all_expense():
    for expense in expensetracker:
        print("Expense =", expense)
        print("Amount =", expensetracker[expense]["amount"])

def total_expenses():
    total = 0

    for expense in expensetracker:
        total += int(expensetracker[expense]["amount"])

    print("Total Expense =", total)

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_all_expense()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Thank You!")
        save_data()
        break

    else:
        print("Invalid Choice!")