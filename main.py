import tkinter as tk
from tkinter import *
import json
import os

root = tk.Tk()
root.geometry("700x600")
root.title("bookshelves")
root.configure(background='slategray')
# Create a frame
frame = tk.Frame(root)
frame.pack()
title = Label(text="(Box 1) Past reading, (Box 2) Current reading, (Box 3) Future reading")
title.pack(side=TOP)
title.configure(background='lightgrey')
filename = "book_list.txt"


#opens previously saved copy of saved text and uses it to replace anything in each book box 
def open_text():
    global filename
    if os.path.isfile(filename):
        books_dict = load_dict_from_file(filename)
        load_dict(listboxes, books_dict)
    

# Function for saving the selected listbox value(s)
def save_text():
    global filename
    saved_dict = {}
    for i in range(3):
        curr_books = []
        for book in listboxes[i].get(0, END):
            curr_books.append(book)
        saved_dict[i] = curr_books
    json_dict = json.dumps(saved_dict)
    text_file = open(filename, "w")
    text_file.write(json_dict)
    text_file.close()


def load_list(listbox, books_list):
    listbox.delete(0,tk.END)
    #func will load 1 list of books into 1 listbox
    for book in books_list:
        listbox.insert('end', book)

def load_dict(listboxes, books_dict):
    for i in range(3):
        load_list(listboxes[i], books_dict[str(i)])


def load_dict_from_file(file_name):
    text_file = open(file_name, "r")
    content = text_file.read()
    text_file.close()
    books_dict = json.loads(content)
    return books_dict
    
open_btn = Button(root, text="Open Text File", command=open_text)
open_btn.pack()

# Create a button to save the text
save = Button(root, text="Save File", command=save_text)
save.pack()

listboxes = [tk.Listbox(frame) for _ in range(3)]
l_colors = ["lightblue"]
curlistbox = listboxes[2]


def sel_listbox(event):
    global curlistbox
    curlistbox = event.widget

for i, listbox in enumerate(listboxes):
    listbox.pack(side='left')
    listbox.configure(background = l_colors)
    listbox.bind("<FocusIn>", sel_listbox)

    
# used to move items (many buttons)
def move_item(src, dest):
    try:
        # 'active' is the line which has been selected
        item = src.get('active') 
        if item:
            src.delete('active')
            dest.insert('end', item)
    except tk.TclError:
        pass

def move_left():
    src = curlistbox
    i = listboxes.index(src)
    dest = listboxes[(i-1)%3]
    move_item(src, dest)

def move_right():
    src = curlistbox
    i = listboxes.index(src)
    dest = listboxes[(i+1)%3]
    move_item(src, dest)


# Move item to the right
button_right = tk.Button(root, text=f'Move >',
                            command=move_right)
button_right.pack(side="top")


# Move item to the left
button_left = tk.Button(root, text=f'Move <',
                        command=move_left)
button_left.pack(side="top",)



def add_item():
    item = entry.get()
    placement = curlistbox.curselection()
    if not placement:
        placement = 'end'
    if item != '':
        curlistbox.insert(placement, item)
        entry.delete(0, tk.END)  # Clear the entry field


#select item to delete and then click delete button
def del_current():
    for item in curlistbox.curselection():
        curlistbox.delete(item)


add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(side='bottom')


entry = tk.Entry(root)
entry.pack(side='bottom', after=add_button)

for i in listboxes:
    if i['state'] == ACTIVE:
        print(i)
remove_button = tk.Button(root, text="Delete", command=del_current)
remove_button.pack(side='bottom', before=add_button)

root.mainloop()