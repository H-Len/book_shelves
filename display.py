from tkinter import *
import tkinter as tk

# # Create a frame
# frame = tk.Frame(root)
# frame.pack()

root = tk.Tk()

listboxes = [tk.Listbox(root) for _ in range(3)]

for i, listbox in enumerate(listboxes):
    listbox.insert('end', f'Item in list {i + 1}')
    listbox.pack(side='left')

selected = {'box': None, 'item': None}

def select_item(listbox):
    try:
        item = listbox.get('active')
        selected['box'] = listbox
        selected['item'] = item
    except tk.TclError:
        pass

# Attach the select_item function to each listbox's selection event
for i, listbox in enumerate(listboxes):
    listbox.bind('<<ListboxSelect>>', lambda e, lb=listbox: select_item(lb))

def move_left():
    try:
        index = listboxes.index(selected['box'])
        selected['box'].delete('active')
        listboxes[index - 1].insert('end', selected['item'])
    except (tk.TclError, ValueError):
        pass

def move_right():
    try:
        index = listboxes.index(selected['box'])
        selected['box'].delete('active')
        listboxes[(index + 1) % 3].insert('end', selected['item'])
    except (tk.TclError, ValueError):
        pass

move_left_button = tk.Button(root, text="Move Left", command=move_left)
move_left_button.pack()

move_right_button = tk.Button(root, text="Move Right", command=move_right)
move_right_button.pack() 