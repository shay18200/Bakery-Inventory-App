import tkinter as tk
from tkinter import messagebox

# Function to add bakery item
def add_item():
    item = entry.get()

    if item == "":
        messagebox.showwarning("Warning", "Enter a bakery item")
    else:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
        count_label.config(text="Total Items: " + str(listbox.size()))

# Main window
window = tk.Tk()
window.title("Bakery Inventory")
window.geometry("300x350")

# Frame
frame = tk.Frame(window)
frame.pack(pady=10)

# Entry
label = tk.Label(frame, text="Bakery Item:")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

# Add button
button = tk.Button(frame, text="Add", command=add_item)
button.grid(row=1, column=0, columnspan=2, pady=10)

# Listbox
listbox = tk.Listbox(window)
listbox.pack(pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Counter
count_label = tk.Label(window, text="Total Items: 0")
count_label.pack()

# Quit button
quit_button = tk.Button(window, text="Quit", command=window.destroy)
quit_button.pack(pady=10)

window.mainloop()
