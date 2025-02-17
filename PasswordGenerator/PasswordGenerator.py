import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        length = int(length_var.get())
        if length < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number for password length.")
        return

    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_special_chars = special_chars_var.get()

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "At least one character type must be selected.")
        return

    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(random.choice(string.digits))
    if use_special_chars:
        password.append(random.choice(string.punctuation))

    password += random.choices(characters, k=length - len(password))

    random.shuffle(password)

    password_var.set("".join(password))


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    copied_label.config(text="Password copied!", fg="green")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(expand=True)

length_var = tk.StringVar(value="12")
uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_chars_var = tk.BooleanVar(value=True)
password_var = tk.StringVar()

tk.Label(frame, text="Password Length:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
length_entry = tk.Entry(frame, textvariable=length_var, width=10, font=("Arial", 12))
length_entry.grid(row=0, column=1, padx=10, pady=5, sticky="we")

tk.Checkbutton(frame, text="Include Uppercase Letters", variable=uppercase_var, font=("Arial", 11)).grid(row=1, column=0, columnspan=2, pady=2)
tk.Checkbutton(frame, text="Include Numbers", variable=numbers_var, font=("Arial", 11)).grid(row=2, column=0, columnspan=2, pady=2)
tk.Checkbutton(frame, text="Include Special Characters", variable=special_chars_var, font=("Arial", 11)).grid(row=3, column=0, columnspan=2, pady=2)

generate_btn = tk.Button(frame, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#4CAF50", fg="white")
generate_btn.grid(row=4, column=0, columnspan=2, pady=10, sticky="we")

password_entry = tk.Entry(frame, textvariable=password_var, state="readonly", width=30, font=("Arial", 12), justify="center")
password_entry.grid(row=5, column=0, columnspan=2, pady=5, sticky="we")

copy_btn = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#008CBA", fg="white")
copy_btn.grid(row=6, column=0, columnspan=2, pady=5, sticky="we")

copied_label = tk.Label(frame, text="", font=("Arial", 10))
copied_label.grid(row=7, column=0, columnspan=2, pady=5)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

root.mainloop()
