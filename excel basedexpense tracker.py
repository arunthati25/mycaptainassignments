import openpyxl
from datetime import datetime

# Global data structure to store expenses
expenses = []

# Predefined expense categories
expense_categories = ["Groceries", "Transportation", "Entertainment"]

def add_expense(amount, description, date, category):
    """
    Add a new expense to the expenses list.
    """
    expense = {"amount": amount, "description": description, "date": date, "category": category}
    expenses.append(expense)
    print("Expense added successfully.")

def edit_expense(index, amount, description, date, category):
    """
    Edit an existing expense in the expenses list.
    """
    if 0 <= index < len(expenses):
        expenses[index] = {"amount": amount, "description": description, "date": date, "category": category}
        print("Expense edited successfully.")
    else:
        print("Invalid expense index.")

def delete_expense(index):
    """
    Delete an expense from the expenses list.
    """
    if 0 <= index < len(expenses):
        del expenses[index]
        print("Expense deleted successfully.")
    else:
        print("Invalid expense index.")

def export_to_excel():
    """
    Export expenses to an Excel spreadsheet.
    """
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Date", "Description", "Amount", "Category"])

    for expense in expenses:
        ws.append([expense["date"], expense["description"], expense["amount"], expense["category"]])

    wb.save("expenses.xlsx")
    print("Expenses exported to expenses.xlsx.")

def display_summary():
    """
    Display a summary of expenses.
    """
    total_spending = sum(expense["amount"] for expense in expenses)
    print(f"Total spending: ${total_spending}")

    # Display spending by category
    print("Spending by category:")
    for category in expense_categories:
        category_spending = sum(expense["amount"] for expense in expenses if expense["category"] == category)
        print(f"{category}: ${category_spending}")

    # Additional analysis features can be added here

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. Export to Excel")
        print("5. Display Summary")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            amount = float(input("Enter the amount spent: "))
            description = input("Enter a description: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            category = input("Enter the category: ")
            add_expense(amount, description, date, category)

        elif choice == "2":
            index = int(input("Enter the index of the expense to edit: "))
            amount = float(input("Enter the new amount spent: "))
            description = input("Enter the new description: ")
            date = input("Enter the new date (YYYY-MM-DD): ")
            category = input("Enter the new category: ")
            edit_expense(index, amount, description, date, category)

        elif choice == "3":
            index = int(input("Enter the index of the expense to delete: "))
            delete_expense(index)

        elif choice == "4":
            export_to_excel()

        elif choice == "5":
            display_summary()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "_main_":
    main()