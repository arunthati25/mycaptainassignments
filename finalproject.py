import tkinter as tk
from tkinter import ttk
import sqlite3
import pandas as pd
from datetime import datetime
from openpyxl import Workbook

class ExpenseTracker:
    def _init_(self, master):
        self.master = master
        self.master.title("Expense Tracker")

        # Create UI components
        # ...

        # Initialize expense data structure
        self.expense_data = []

        # Connect to SQLite database
        self.db_connection = sqlite3.connect("expense_data.db")
        self.create_table()

    def create_table(self):
        # Create SQLite table if not exists
        # ...

    def add_expense(self, amount, category, description):
        # Add expense to the data structure and update SQLite database
        # …
    def edit_expense(self, expense_id, amount, category, description):
        # Edit expense in the data structure and update SQLite database
        # ...

    def delete_expense(self, expense_id):
        # Delete expense from the data structure and SQLite database
        # ...

    def export_data(self, file_path, export_format):
        # Export data in the specified format (Excel, text, SQLite)
        # ...

    def update_summary(self):
        # Update and display expense summary
        # ...

    def create_gui(self):
        # Create the graphical user interface
        # ...

def main():
    root = tk.Tk()
    expense_tracker_app = ExpenseTracker(root)
    expense_tracker_app.create_gui()
    root.mainloop()

if __name__ == "_main_":
    main()