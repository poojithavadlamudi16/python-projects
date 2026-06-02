expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.View Total Expense")
    print("4.Exit")

    choice=input("Enter your choice: ")

    if choice=="1":
        item=input("Enter expense name: ")
        amount=float(input("Enter amount: "))

        expenses.append([item,amount])

        print("Expense added successfully!")

    elif choice=="2":
        if len(expenses)==0:
            print("No expenses recorded.")

        else:
            print("\nExpenses:")
            for expense in expenses:
                print(expense[0],"-",expense[1])

    elif choice=="3":
        total=0

        for expense in expenses:
            total+=expense[1]

        print("Total Expense =",total)

    elif choice=="4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")