import tkinter as tk
from tkinter import *


root = tk.Tk()
title = Label(text="Past reading, Current reading, & Future reading below, respectively")
title.pack(side=TOP)
listboxes = [tk.Listbox(root) for _ in range(3)]
listbox = tk.Listbox(root)
l_colors = ["lightblue", "lightgreen", "pink"]
shelf_label = ["Past read", "Currently reading", "Future read"]
for i, listbox in enumerate(listboxes):
    listbox.insert('end', f'{shelf_label[i]}')
    listbox.pack(side='left')
    listbox.configure(background = l_colors[i])

def move_item(e, src, dest):
    try:
        # 'active' is the line which has been selected
        item = src.get('active') 
        src.delete('active')
        dest.insert('end', item)
    except tk.TclError:
        pass
    
buttons = [tk.Button(root, text=f'Move {i}->{(i+1)%3}', 
                     command=lambda src=listboxes[i], dest=listboxes[(i+1)%3]: move_item(root, src, dest)) 
            for i in range(3)]
for button in buttons:
    button.pack()

def add_item():
    item = entry.get()
    if item != '':
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)  # Clear the entry field

# root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Add Item", command=add_item)
# remove_button = tk.Button(root, text="Drop Item", command=)
add_button.pack()
    
root.mainloop()