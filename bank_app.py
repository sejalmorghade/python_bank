import sqlite3
import tkinter as tk
from tkinter import messagebox

# Create a connection to the SQLite database
conn = sqlite3.connect('banking.db')
c = conn.cursor()

# Create a table to store account information
c.execute('''CREATE TABLE IF NOT EXISTS accounts
(id INTEGER PRIMARY KEY, name TEXT, balance REAL)''')
conn.commit()

# Function to create a new account
def create_account(name, initial_balance):
    c.execute('''INSERT INTO accounts (name, balance) VALUES (?, ?)''', (name, initial_balance))
    conn.commit()

# Function to deposit money into an account
def deposit_money(account_id, amount):
    c.execute('''UPDATE accounts SET balance = balance + ? WHERE id = ?''', (amount, account_id))
    conn.commit()

# Function to withdraw money from an account
def withdraw_money(account_id, amount):
    c.execute('''UPDATE accounts SET balance = balance - ? WHERE id = ?''', (amount, account_id))
    conn.commit()

# Function to check balance
def check_balance(account_id):
    c.execute('''SELECT balance FROM accounts WHERE id = ?''', (account_id,))
    balance = c.fetchone()
    if balance:
        return balance[0]
    else:
        return None

# GUI function for creating an account
def create_account_gui():
    def submit():
        name = name_entry.get()
        try:
            initial_balance = float(balance_entry.get())
            create_account(name, initial_balance)
            messagebox.showinfo("Success", "Account created successfully!")
            create_window.destroy()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    create_window = tk.Toplevel(root)
    create_window.title("Create Account")
    tk.Label(create_window, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(create_window)
    name_entry.grid(row=0, column=1)
    tk.Label(create_window, text="Initial Balance:").grid(row=1, column=0)
    balance_entry = tk.Entry(create_window)
    balance_entry.grid(row=1, column=1)
    submit_button = tk.Button(create_window, text="Submit", command=submit)
    submit_button.grid(row=2, columnspan=2)

# Placeholder GUI functions
def deposit_gui():
    pass

def withdraw_gui():
    pass

def check_balance_gui():
    pass

# Main GUI function
def main_menu():
    global root
    root = tk.Tk()
    root.title("Banking System")
    tk.Label(root, text="Welcome to the Banking System").pack()
    tk.Button(root, text="Create Account", command=create_account_gui).pack()
    tk.Button(root, text="Deposit Money", command=deposit_gui).pack()
    tk.Button(root, text="Withdraw Money", command=withdraw_gui).pack()
    tk.Button(root, text="Check Balance", command=check_balance_gui).pack()
    root.mainloop()

# Run the main menu
if __name__ == "__main__":
    main_menu()
