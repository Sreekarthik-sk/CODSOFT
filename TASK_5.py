import tkinter as tk
from tkinter import messagebox, simpledialog

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self, master):
        self.master = master
        self.contacts = []
        
        master.title("Contact Book")

        self.label = tk.Label(master, text="Contact Book", font=("Arial", 24))
        self.label.pack(pady=10)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=5)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.pack(pady=5)

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.pack(pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(pady=5)

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        if name:
            phone = simpledialog.askstring("Input", "Enter Phone Number:")
            email = simpledialog.askstring("Input", "Enter Email:")
            address = simpledialog.askstring("Input", "Enter Address:")
            new_contact = Contact(name, phone, email, address)
            self.contacts.append(new_contact)
            messagebox.showinfo("Success", "Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
            return
        
        contacts_list = "\n".join([f"{c.name} - {c.phone}" for c in self.contacts])
        messagebox.showinfo("Contacts", contacts_list)

    def search_contact(self):
        search_term = simpledialog.askstring("Input", "Enter Name or Phone Number to search:")
        results = [c for c in self.contacts if search_term in (c.name, c.phone)]
        
        if results:
            results_list = "\n".join([f"{c.name} - {c.phone} | {c.email} | {c.address}" for c in results])
            messagebox.showinfo("Search Results", results_list)
        else:
            messagebox.showinfo("Info", "No contacts found.")

    def update_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to update:")
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = simpledialog.askstring("Input", "Enter new Phone Number:", initialvalue=contact.phone)
                contact.email = simpledialog.askstring("Input", "Enter new Email:", initialvalue=contact.email)
                contact.address = simpledialog.askstring("Input", "Enter new Address:", initialvalue=contact.address)
                messagebox.showinfo("Success", "Contact updated successfully!")
                return
        messagebox.showinfo("Info", "Contact not found.")

    def delete_contact(self):
        name = simpledialog.askstring("Input", "Enter the name of the contact to delete:")
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
                return
        messagebox.showinfo("Info", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()


