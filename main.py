import tkinter as tk
from tkinter import *
# import display

root = tk.Tk()
root.title("bookshelves")

# Create a frame
frame = tk.Frame(root)
frame.pack()
title = Label(text="Past reading, Current reading, & Future reading")
title.pack(side=TOP)
# title1 = Label(root, text="Past reading")
# title2 = Label(text="Current reading")
# title3 = Label(text="Future reading")
# title3.pack(side='top')
# title2.pack(side='top', before=title3)
# title.pack(side='top', before=title2)


listboxes = [tk.Listbox(frame) for _ in range(3)]
# listbox = tk.Listbox(frame)
l_colors = ["lightblue", "lightgreen", "pink"]
shelf_label = ["Past read", "Currently reading", "Future read"]




for i, listbox in enumerate(listboxes):
    listbox.insert('end', f'{shelf_label[i]}')
    listbox.pack(side='left')
    listbox.configure(background = l_colors[i])



#//////////////////////////////////
# used to move items (many buttons)
def move_item(src, dest):
    try:
        # 'active' is the line which has been selected
        item = src.get('active') 
        src.delete('active')
        dest.insert('end', item)
    except tk.TclError:
        pass

#bottons to move items left or right
for i in range(3):
    # Move item to the right
    button_right = tk.Button(root, text=f'Move {i}->{(i+1)%3}',
                             command=lambda src=listboxes[i], dest=listboxes[(i+1)%3]: move_item(src, dest))
    button_right.pack(side="left")

    # Move item to the left
    button_left = tk.Button(root, text=f'Move {i}->{(i-1)%3}',
                            command=lambda src=listboxes[i], dest=listboxes[(i-1)%3]: move_item(src, dest))
    button_left.pack(side="right")


def add_item():
    item = entry.get()
    if item != '':
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)  # Clear the entry field

def del_current():
    for item in listbox.curselection():
        listbox.delete(item)


entry = tk.Entry(root)
entry.pack()

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack()

remove_button = tk.Button(root, text="Delete", command=del_current)
remove_button.pack()

# Create a Frame for border
border_color = Frame(root, background="red")
 
# Label Widget inside the Frame
label = Label(border_color, text="Move book to right most box and select it before clicking delete", bd=5)
 
# Place the widgets with border Frame
label.pack(padx=1, pady=1)
border_color.pack(padx=40, pady=40)

label.pack(side= "bottom")

root.mainloop()