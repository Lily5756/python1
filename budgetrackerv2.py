def show_menu():
    """Display the main menu options"""
    print("\n" + "=" * 30)
    print("     BUDGET TRACKER")
    print("=" * 30)
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Balance")
    print("4. Delete Expense")
    print("5. View Statistics")
    print("6. Set Budget Category Limits")
    print("7. Exit")
    print("=" * 30)


def add_expense(expenses, categories):
    """Add a new expense with category"""
    name = input("Enter expense name: ")

    while True:
        try:
            amount = float(input("Enter expense amount: ฿"))
            if amount <= 0:
                print("Amount must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")

    print("\nCategories: Food, Transport, Entertainment, Bills, Other")
    category = input("Enter category: ").title()

    if category not in categories:
        categories[category] = []

    expenses.append({"name": name, "amount": amount, "category": category})
    categories[category].append(amount)

    print(f"✓ Added expense: {name} - ฿{amount:.2f} ({category})")


def view_expenses(expenses):
    """Display all expenses organized by category"""
    if not expenses:
        print("\nNo expenses recorded yet!")
        return

    print("\n" + "=" * 50)
    print("YOUR EXPENSES".center(50))
    print("=" * 50)

    total = 0
    current_category = None

    # Sort by category for better organization
    sorted_expenses = sorted(expenses, key=lambda x: x["category"])

    for expense in sorted_expenses:
        if current_category != expense["category"]:
            if current_category is not None:
                print()
            current_category = expense["category"]
            print(f"\n[{current_category}]")

        print(f"  • {expense['name']}: ${expense['amount']:.2f}")
        total += expense["amount"]

    print("\n" + "-" * 50)
    print(f"Total Spent: ${total:.2f}")
    print("=" * 50)


def show_balance(budget, expenses):
    """Display remaining balance with visual indicator"""
    total_spent = sum(exp["amount"] for exp in expenses)
    balance = budget - total_spent
    percentage_used = (total_spent / budget * 100) if budget > 0 else 0

    print("\n" + "=" * 50)
    print("BALANCE SUMMARY".center(50))
    print("=" * 50)
    print(f"Total Budget:    ${budget:.2f}")
    print(f"Total Spent:     ${total_spent:.2f}")
    print(f"Remaining:       ${balance:.2f}")
    print(f"Used:            {percentage_used:.1f}%")

    # Visual progress bar
    bar_length = 30
    filled = int(bar_length * percentage_used / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"\n[{bar}]")

    # Warning messages
    if percentage_used >= 90:
        print("\n⚠️  WARNING: You've used 90% or more of your budget!")
    elif percentage_used >= 75:
        print("\n⚠️  CAUTION: You've used 75% of your budget!")

    print("=" * 50)


def delete_expense(expenses, categories):
    """Delete an expense from the list"""
    if not expenses:
        print("\nNo expenses to delete!")
        return

    print("\nYour Expenses:")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['name']} - ${exp['amount']:.2f} ({exp['category']})")

    try:
        choice = int(input("\nEnter the number of expense to delete (0 to cancel): "))
        if choice == 0:
            return
        if 1 <= choice <= len(expenses):
            deleted = expenses.pop(choice - 1)
            print(f"✓ Deleted: {deleted['name']} - ${deleted['amount']:.2f}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number!")


def show_statistics(expenses, categories):
    """Display spending statistics by category"""
    if not expenses:
        print("\nNo expenses recorded yet!")
        return

    print("\n" + "=" * 50)
    print("SPENDING STATISTICS".center(50))
    print("=" * 50)

    total_spent = sum(exp["amount"] for exp in expenses)

    # Calculate spending by category
    category_totals = {}
    for exp in expenses:
        cat = exp["category"]
        category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

    # Sort categories by spending
    sorted_categories = sorted(
        category_totals.items(), key=lambda x: x[1], reverse=True
    )

    print("\nSpending by Category:")
    for category, amount in sorted_categories:
        percentage = (amount / total_spent * 100) if total_spent > 0 else 0
        bar_length = 20
        filled = int(bar_length * percentage / 100)
        bar = "█" * filled + "░" * (bar_length - filled)
        print(f"\n{category:15} ${amount:8.2f} ({percentage:5.1f}%)")
        print(f"                [{bar}]")

    print("\n" + "=" * 50)
    print(f"Average Expense: ${total_spent / len(expenses):.2f}")
    print(f"Total Expenses:  {len(expenses)}")
    print("=" * 50)


def main():
    """Main program loop"""
    print("\n💰 Welcome to Budget Tracker! 💰")

    # Initialize budget
    while True:
        try:
            budget = float(input("\nEnter your total budget: $"))
            if budget <= 0:
                print("Budget must be positive!")
                continue
            break
        except ValueError:
            print("Please enter a valid number!")

    expenses = []
    categories = {}

    # Main loop
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_expense(expenses, categories)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            show_balance(budget, expenses)

        elif choice == "4":
            delete_expense(expenses, categories)

        elif choice == "5":
            show_statistics(expenses, categories)

        elif choice == "6":
            new_budget = float(input("Enter new budget amount: $"))
            budget = new_budget
            print(f"✓ Budget updated to ${budget:.2f}")

        elif choice == "7":
            print("\n" + "=" * 50)
            print("Thanks for using Budget Tracker! 💰")
            print("=" * 50)
            break

        else:
            print("❌ Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    main()
