import tkinter as tk
from tkinter import *

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

#opens previously saved copy of saved text into each book box 
def open_text():
   text_file = open("book_list.txt", "r")
   content = text_file.read()
   for listbox in listboxes:
       listbox.insert(END, content)
   text_file.close()

# saves text entered in box
def save_text():
   text_file = open("book_list.txt", "w")
   text_file.write(my_text_box.get(1.0, END))
   text_file.close()

######################
#TO DO NEXT:
def load_list(listbox, books_list):
    #func will load 1 list of books into 1 listbox
    for book in books_list:
        listbox.insert('end', book)

def load_dict(listboxes, books_dict):
    for i in range(3):
        print(listboxes[i])
        load_list(listboxes[i], books_dict[str(i+1)])


def load_dict_from_file(file_name):
    books_dict_sample = {"1": ["once", "twice", "never", "ago"], "2": ["Good morning"], "3": ["a", "b", "c", "d"]}
    return books_dict_sample


###################

# # Creating a text box widget
my_text_box = Text(root, height=10, width=40)
my_text_box.pack()

open_btn = Button(root, text="Open Text File", command=open_text)
open_btn.pack()

# Create a button to save the text
save = Button(root, text="Save File", command=save_text)
save.pack()

# #label to state what is presented in the app
# tk_title = Label(text="Books in my bookshelf: ")
# tk_title.place(bordermode='outside')
# tk_title.configure(background="brown")

listboxes = [tk.Listbox(frame) for _ in range(3)]
# listbox = tk.Listbox(frame)
l_colors = ["lightblue"]
shelf_label = ["Past read", "Currently reading", "Future read"]
curlistbox = listboxes[2]


def sel_listbox(event):
    global curlistbox
    curlistbox = event.widget

for i, listbox in enumerate(listboxes):
    listbox.insert('end', f'{shelf_label[i]}')
    listbox.pack(side='left')
    listbox.configure(background = l_colors)
    listbox.bind("<FocusIn>", sel_listbox)

books_dict = load_dict_from_file('test.txt')
load_dict(listboxes, books_dict)
    
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
button_right.pack(side="left")


# Move item to the left
button_left = tk.Button(root, text=f'Move <',
                        command=move_left)
button_left.pack(side="left",)



def add_item():
    item = entry.get()
    placement = curlistbox.curselection()
    if not placement:
        placement = 'end'
    if item != '':
        curlistbox.insert(placement, item)
        entry.delete(0, tk.END)  # Clear the entry field



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