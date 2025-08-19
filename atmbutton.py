import tkinter as tk
from tkinter import simpledialog, messagebox

class ATM:
    def __init__(self):
        self.balance = 0
        self.pin = "1234"  # Default PIN
        self.transactions = []

    def verify_pin(self):
        entered_pin = simpledialog.askstring("PIN Verification", "Enter your ATM PIN:", show='*')
        return entered_pin == self.pin

    def check_balance(self):
        if self.verify_pin():
            messagebox.showinfo("Balance", f"Your current balance is: ${self.balance}")
            self.transactions.append(f"Checked balance: ${self.balance}")
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def deposit(self, amount):
        if self.verify_pin():
            if amount > 0:
                self.balance += amount
                messagebox.showinfo("Deposit", f"${amount} has been deposited. Your new balance is: ${self.balance}")
                self.transactions.append(f"Deposited: ${amount}")
            else:
                messagebox.showerror("Error", "Deposit amount must be positive.")
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def withdraw(self, amount):
        if self.verify_pin():
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    messagebox.showinfo("Withdraw", f"${amount} has been withdrawn. Your new balance is: ${self.balance}")
                    self.transactions.append(f"Withdrew: ${amount}")
                else:
                    messagebox.showerror("Error", "Insufficient balance.")
            else:
                messagebox.showerror("Error", "Withdrawal amount must be positive.")
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def transfer_money(self, amount):
        if self.verify_pin():
            if amount > 0:
                if self.balance >= amount:
                    self.balance -= amount
                    messagebox.showinfo("Transfer", f"${amount} has been transferred. Your new balance is: ${self.balance}")
                    self.transactions.append(f"Transferred: ${amount}")
                else:
                    messagebox.showerror("Error", "Insufficient balance.")
            else:
                messagebox.showerror("Error", "Transfer amount must be positive.")
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def change_pin(self, new_pin):
        if self.verify_pin():
            if new_pin:
                self.pin = new_pin
                messagebox.showinfo("Change PIN", "Your PIN has been changed successfully.")
            else:
                messagebox.showerror("Error", "PIN cannot be empty.")
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def mini_statement(self):
        if self.verify_pin():
            statement = "\n".join(self.transactions[-5:]) if self.transactions else "No transactions yet."
            messagebox.showinfo("Mini Statement", statement)
        else:
            messagebox.showerror("Error", "Invalid PIN")

def main():
    atm = ATM()

    def check_balance():
        atm.check_balance()

    def deposit_money():
        amount = simpledialog.askfloat("Deposit", "Enter the amount to deposit:")
        if amount is not None:
            atm.deposit(amount)

    def withdraw_money():
        amount = simpledialog.askfloat("Withdraw", "Enter the amount to withdraw:")
        if amount is not None:
            atm.withdraw(amount)

    def transfer_money():
        amount = simpledialog.askfloat("Transfer", "Enter the amount to transfer:")
        if amount is not None:
            atm.transfer_money(amount)

    def change_pin():
        new_pin = simpledialog.askstring("Change PIN", "Enter the new PIN:")
        if new_pin is not None:
            atm.change_pin(new_pin)

    def mini_statement():
        atm.mini_statement()

    def exit_atm():
        root.destroy()

    root = tk.Tk()
    root.title("ATM")
    root.configure(bg="white")  # Set background color to white
    root.geometry("400x600")  # Set the size of the window

    button_bg = "lightblue"  # Button background color
    button_font = ("Helvetica", 14)  # Button font

    tk.Label(root, text="Welcome to the ATM", bg="white", font=("Helvetica", 16)).pack(pady=10)
    tk.Button(root, text="Check Balance", command=check_balance, bg=button_bg, font=button_font, height=2, width=30).pack(pady=10)
    tk.Button(root, text="Deposit Money", command=deposit_money, bg=button_bg, font=button_font, height=2, width=30).pack(pady=10)
    tk.Button(root, text="Withdraw Money", command=withdraw_money, bg=button_bg, font=button_font, height=2, width=30).pack(pady=10)
    tk.Button(root, text="Transfer Money", command=transfer_money, bg=button_bg, font=button_font, height=2, width=30).pack(pady=10)
    tk.Button(root, text="Change PIN", command=change_pin, bg=button_bg, font=button_font, height=2, width=30).pack(pady=10)
    tk.Button(root, text="Mini Statement", command=mini_statement, bg=button_bg, font=button_font, height=2, width=30).pack(pady=10)
    tk.Button(root, text="Exit", command=exit_atm, bg=button_bg, font=button_font, height=2, width=30).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
