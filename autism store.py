
import tkinter as tk
from tkinter import messagebox
import random

class AutisticGroceryStoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Leb's Grocery Store")
        self.shopping_list = []

        self.grocery_items = [
            {"name": "Apples", "weight": random.randint(1, 10), "price": random.randint(1, 10)},
            {"name": "Bananas", "weight": random.randint(1, 10), "price": random.randint(1, 10)},
            {"name": "Carrots", "weight": random.randint(1, 10), "price": random.randint(1, 10)},
            {"name": "Milk", "weight": random.randint(1, 10), "price": random.randint(1, 10)},
            {"name": "Bread", "weight": random.randint(1, 10), "price": random.randint(1, 10)},
            {"name": "Eggs", "weight": random.randint(1, 10), "price": random.randint(1, 10)},
            {"name": "Cheese", "weight": random.randint(1, 10), "price": random.randint(1, 10)},
            {"name": "Yogurt", "weight": random.randint(1, 10), "price": random.randint(1, 10)}
        ]

        self.item_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
        for item in self.grocery_items:
            display_text = f"{item['name']} (Weight: {item['weight']}, Price: {item['price']})"
            self.item_listbox.insert(tk.END, display_text)
        self.item_listbox.pack(pady=10)

        self.add_button = tk.Button(root, text="Add to Shopping List", command=self.add_to_shopping_list)
        self.add_button.pack(pady=5)

        self.view_list_button = tk.Button(root, text="View Shopping List", command=self.view_shopping_list)
        self.view_list_button.pack(pady=5)

    def add_to_shopping_list(self):
        selected_index = self.item_listbox.curselection()
        if selected_index:
            selected_item = self.grocery_items[selected_index[0]]
            if selected_item not in self.shopping_list:
                self.shopping_list.append(selected_item)
                messagebox.showinfo("Item Added", f"{selected_item['name']} added to your shopping list. Weight: {selected_item['weight']}, Price: {selected_item['price']}.")
            else:
                messagebox.showwarning("Item Exists", f"{selected_item['name']} is already in your shopping list.")
        else:
            messagebox.showwarning("No Item Selected", "Please select an item to add to your shopping list.")

    def view_shopping_list(self):
        if not self.shopping_list:
            messagebox.showinfo("Shopping List", "Your shopping list is empty.")
        else:
            list_window = tk.Toplevel(self.root)
            list_window.title("Shopping List")
            list_label = tk.Label(list_window, text="Your Shopping List:")
            list_label.pack(pady=5)
            for item in self.shopping_list:
                item_label = tk.Label(list_window, text=f"• {item['name']} (Weight: {item['weight']}, Price: {item['price']})")
                item_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutisticGroceryStoreApp(root)
    root.mainloop()
