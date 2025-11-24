import datetime

# --------- FILE SETUP ----------
FILE = "expenses.txt"

# Make sure file exists
open(FILE, "a").close()


# --------- FUNCTIONS ------------

def add_expense():
    amount = float(input("Enter amount spent: ₹"))
    category = input("Category (food/travel/study/other): ").lower()
    note = input("Short note: ")

    time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

    with open(FILE, "a") as f:
        f.write(f"{amount},{category},{note},{time}\n")

    print("Expense added successfully!\n")


def read_expenses():
    expenses = []
    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if len(data) == 4:
                amount, category, note, time = data
                expenses.append([float(amount), category, note, time])
    return expenses


def show_summary(budget):
    expenses = read_expenses()

    if not expenses:
        print("No expenses found.\n")
        return

    total = sum(x[0] for x in expenses)
    remaining = budget - total

    print("\n----- EXPENSE SUMMARY -----")
    print(f"Total Spent: ₹{total}")
    print(f"Remaining Balance: ₹{remaining}")

    # Category-wise spending
    categories = {"food": 0, "travel": 0, "study": 0, "other": 0}
    for amt, cat, _, _ in expenses:
        if cat in categories:
            categories[cat] += amt

    print("\nCategory-wise spending:")
    for cat, amt in categories.items():
        bar = "█" * int(amt / 50) # bar chart
        print(f"{cat.capitalize():7} : ₹{amt:5} {bar}")

    # Suggestions
    print("\n--- Suggestions ---")
    if total > budget:
        print("⚠ You have crossed your budget. Reduce spending immediately!")
    else:
        if categories["food"] > budget * 0.4:
            print("Try cooking at home sometimes to reduce food expenses.")
        if categories["travel"] > budget * 0.3:
            print("Use public transport or share rides to save money.")
        if categories["study"] < 200:
            print("Invest more in study materials if needed.")
        if remaining < budget * 0.2:
            print("You are close to your limit. Spend carefully.")

    print()


# --------- MAIN PROGRAM ------------

print("========== SMART EXPENSE TRACKER ==========")
budget = float(input("Enter your monthly budget: ₹"))

while True:
    print("\n1. Add Expense")
    print("2. View Summary")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_summary(budget)
    elif choice == "3":
        print("Thank you for using the tracker!")
        break
    else:
        print("Invalid choice. Try again.\n")