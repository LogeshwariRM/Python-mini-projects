import random
import string
import tkinter as tk
from tkinter import simpledialog, messagebox

def generate_password(length):
    # Define the character set: uppercase, lowercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password

def generate_passwords():
    try:
        # Get user input for the length of the password
        password_length = int(simpledialog.askstring("Input", "Enter the length of each password:"))
        if password_length <= 0:
            raise ValueError("Password length should be a positive integer.")
        
        # Get user input for the number of passwords to generate
        number_of_passwords = int(simpledialog.askstring("Input", "Enter the number of passwords to generate:"))
        if number_of_passwords <= 0:
            raise ValueError("Number of passwords should be a positive integer.")
        
        # Generate and collect the passwords
        passwords = [generate_password(password_length) for _ in range(number_of_passwords)]
        
        # Display the passwords in a message box
        messagebox.showinfo("Generated Passwords", "\n".join(passwords))
    
    except ValueError as e:
        messagebox.showerror("Invalid input", str(e))

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")
root.configure(bg="white")

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Passwords", command=generate_passwords, bg="lightblue", font=("Helvetica", 14))
generate_button.pack(pady=20)

# Start the main event loop
root.mainloop()
