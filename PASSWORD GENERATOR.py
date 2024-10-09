import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(entry_length.get())  # Get the length from the entry
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid positive integer for password length.")
        return
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    entry_password.delete(0, tk.END)
    entry_password.insert(0, password)
def copy_to_clipboard():
    password = entry_password.get()
    if password:
        app.clipboard_clear()
        app.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "No password to copy. Generate one first!")
app = tk.Tk()
app.title("Password Generator")
label_length = tk.Label(app, text="Enter password length:")
label_length.pack(pady=10)
entry_length = tk.Entry(app)
entry_length.pack(pady=5)
label_characters = tk.Label(app, text="Random characters include: A-Z, a-z, 0-9, and special characters (!@#$%^&*)")
label_characters.pack(pady=10)
button_generate = tk.Button(app, text="Generate Password", command=generate_password)
button_generate.pack(pady=10)
label_password = tk.Label(app, text="Generated Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(app, width=30)
entry_password.pack(pady=5)
button_copy = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
button_copy.pack(pady=10)
app.mainloop()
