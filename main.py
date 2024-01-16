# from graphics import Window, Line, Point 
# from book import Book
# # from shelves import Now_reading, Past_read, Future_read
# import sys

# def main(): 
#     win = Window(800, 600)
#     # l = Line(Point(50, 50), Point(450, 500))
#     # win.draw_line(l, "black")
#     win.wait_for_close()

#     print("bookshelf in progress.")

#     sys.setrecursionlimit(10000)
#     print("BOOKs!!!!")

#     num_rows = 12
#     num_cols = 3
#     margin = 50
#     screen_x = 800
#     screen_y = 600
#     # cell_size_x = (screen_x - 2 * margin) / num_cols
#     # cell_size_y = (screen_y - 2 * margin) / num_rows


#     sys.setrecursionlimit(10000)
#     win = Window(screen_x, screen_y)

#     # shelf = Window(5000, 10)


# main()

import string
import tkinter as tk
from tkinter import *


root = tk.Tk()

listboxes = [tk.Listbox(root) for _ in range(3)]
# for i in range(3):
#     if i == 0:
#         tk.Label(root, text= "Past books").grid(row=0, column=i)
#         tk.Listbox(root, bg = "pink", width=40).grid(row=1, column=i)
#     elif i == 1:
#         tk.Label(root, text= "Currently reading").grid(row=0, column=i)
#         tk.Listbox(root, bg = "lightgreen", width=40).grid(row=1, column=i)
#     else:
#         tk.Label(root, text= "Future books").grid(row=0, column=i)
#         tk.Listbox(root, bg = "lightblue", width=40).grid(row=1, column=i)

title = Label(text="Past reading, Current reading, & Future reading below, respectively")
title.pack(side=TOP)


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

listbox = tk.Listbox(root)
listbox.pack()
for i, listbox in enumerate(listboxes):
    listbox.insert('end', f'Item in list {i+1}')
    listbox.pack(side='left')


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


    
root.mainloop()