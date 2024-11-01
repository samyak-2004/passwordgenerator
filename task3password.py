import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        include_chars = include_entry.get()
        exclude_chars = exclude_entry.get()
        
        # Ensure length is at least 4 for the mandatory character types
        if length < 4:
            raise ValueError("Length must be at least 4 to include all character types.")
        
        # Default characters
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits

        # Define the character set based on exclusions

        special_chars = ""
        if include_chars:
            for c in include_chars:
                if c not in exclude_chars:
                    special_chars += c
        else:
            special_chars = string.punctuation

        # Define available characters by filtering out excluded characters
        available_chars = ""
        for c in uppercase + lowercase + digits + special_chars:
            if c not in exclude_chars:
                available_chars += c
        
        # Check if there are enough characters to create the password
        if length > len(available_chars):
            raise ValueError("Not enough unique characters to generate a password of this length.")
        
        # Guarantee at least one character from each required type
        password = [
            random.choice(uppercase),
            random.choice(lowercase),
            random.choice(digits),
            random.choice(special_chars)
        ]
        
        # Fill the rest of the password length with random choices from available characters
        # Append random choices to fill the remaining length
        for nn in range(length - 4):
            password.append(random.choice(available_chars))

        random.shuffle(password)  # Shuffle to mix mandatory characters
        
        # Display the password
        password_entry.delete(0, tk.END)
        password_entry.insert(0, ''.join(password))
        
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

def clear_fields():
    length_entry.delete(0, tk.END)
    include_entry.delete(0, tk.END)
    exclude_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Set up the main window
window = tk.Tk()
window.title("Password Generator")
window.configure(bg="powder blue")
window.geometry("600x400")


font = ("Helvetica", 30)

# Labels and Entries
tk.Label(window, text="Length of Password:", bg="powder blue", font=font).grid(row=0, column=0, padx=10, pady=5, sticky="w")
length_entry = tk.Entry(window, font=font)
length_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Include Special Characters:", bg="powder blue", font=font).grid(row=1, column=0, padx=10, pady=5, sticky="w")
include_entry = tk.Entry(window, font=font)
include_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Exclude Characters:", bg="powder blue", font=font).grid(row=2, column=0, padx=10, pady=5, sticky="w")
exclude_entry = tk.Entry(window, font=font)
exclude_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Generated Password:", bg="powder blue", font=font).grid(row=3, column=0, padx=10, pady=5, sticky="w")
password_entry = tk.Entry(window, font=font)
password_entry.grid(row=3, column=1, padx=10, pady=5)

# Buttons
generate_button = tk.Button(window, text="Generate Password", command=generate_password, bg="light blue", font=font)
generate_button.grid(row=4, column=0, columnspan=2, pady=10)

clear_button = tk.Button(window, text="Clear", command=clear_fields, bg="light blue", font=font)
clear_button.grid(row=5, column=0, columnspan=2, pady=10)

window.mainloop()
