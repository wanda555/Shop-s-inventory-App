# gui.py

import tkinter as tk
from tkinter import ttk, messagebox
import db  # Import your database logic

class InventoryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inventory Management System")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Product Name:").grid(column=0, row=0, sticky=tk.W)
        self.name_entry = ttk.Entry(frame, width=25)
        self.name_entry.grid(column=1, row=0)

        ttk.Label(frame, text="Quantity:").grid(column=0, row=1, sticky=tk.W)
        self.quantity_entry = ttk.Entry(frame, width=25)
        self.quantity_entry.grid(column=1, row=1)

        ttk.Label(frame, text="Price:").grid(column=0, row=2, sticky=tk.W)
        self.price_entry = ttk.Entry(frame, width=25)
        self.price_entry.grid(column=1, row=2)

        add_btn = ttk.Button(frame, text="Add Product", command=self.add_product)
        add_btn.grid(column=1, row=3, pady=10)

    def add_product(self):
        name = self.name_entry.get()
        try:
            quantity = int(self.quantity_entry.get())
            price = float(self.price_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Quantity must be integer and price must be numeric.")
            return

        if not name:
            messagebox.showerror("Missing Name", "Product name is required.")
            return

        db.add_product(name, quantity, price)
        messagebox.showinfo("Success", f"Product '{name}' added successfully!")

if __name__ == "__main__":
    db.create_tables()  # Create the table when app starts
    app = InventoryApp()
    app.mainloop()
