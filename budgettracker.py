def show_menu():
    print("\n===== Budget Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Balance")
    print("4. Exit")


# initialize variables
budget = float(input("Enter your total budget: "))
expenses = []

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        expenses.append((name, amount))
        print(f"Added expense: {name} - ${amount:.2f}")

    elif choice == "2":
        print("\nYour expenses:")
        total = 0
        for name, amount in expenses:
            print(f"- {name}: ${amount:.2f}")
            total += amount
        print(f"Total spent: ${total:.2f}")

    elif choice == "3":
        total = sum(amount for _, amount in expenses)
        balance = budget - total
        print(f"\nRemaining balance: ${balance:.2f}")

    elif choice == "4":
        print("Exiting Budget Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
