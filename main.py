import tkinter as tk
from tkinter import *
# import display

root = tk.Tk()
root.title("bookshelves")
root.configure(background='slategray')
# Create a frame
frame = tk.Frame(root)
frame.pack()
title = Label(text="(Box 1) Past reading, (Box 2) Current reading, (Box 3) Future reading")
title.pack(side=TOP)
title.configure(background='lightgrey')

#label to state what is presented in the app
tk_title = Label(text="Books in my bookshelf: ")
tk_title.place(bordermode='outside')
tk_title.configure(background="brown")


listboxes = [tk.Listbox(frame) for _ in range(3)]
# listbox = tk.Listbox(frame)
l_colors = ["lightblue", "lightgreen", "purple"]
shelf_label = ["Past read", "Currently reading", "Future read"]




for i, listbox in enumerate(listboxes):
    listbox.insert('end', f'{shelf_label[i]}')
    listbox.pack(side='left')
    listbox.configure(background = l_colors[i])


def switch_buttons(src):
    item = src.get('active')
    print(item)
    for item in listbox:
        if item:
            print(item)
    

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
    # switch_buttons(src)

    
    # Move item to the right
    button_right = tk.Button(root, text=f'Move {i}->{(i+1)%3}',
                             command=lambda src=listboxes[i], dest=listboxes[(i+1)%3]: move_item(src, dest))
    button_right.pack(side="left")
    

    # Move item to the left
    button_left = tk.Button(root, text=f'Move {i}->{(i-1)%3}',
                            command=lambda src=listboxes[i], dest=listboxes[(i-1)%3]: move_item(src, dest))
    button_left.pack(side="left",)




def add_item():
    item = entry.get()
    placement = listbox.curselection()
    if item != '':
        listbox.insert(placement, item)
        entry.delete(0, tk.END)  # Clear the entry field



def del_current():
    for item in listbox.curselection():
        listbox.delete(item)

    to_go = Label(item)
    to_go.configure(after=remove_button)


add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(side='bottom')


entry = tk.Entry(root)
entry.pack(side='bottom', after=add_button)

for i in listboxes:
    if i['state'] == ACTIVE:
        print(i)
remove_button = tk.Button(root, text="Delete", command=del_current)
remove_button.pack(side='bottom', before=add_button)

# Create a Frame for border
border_color = Frame(root, background="red")
 
# Label Widget inside the Frame
label = Label(border_color, text="Move book to right most box and select it before clicking delete", bd=5)
label.configure(background="pink") 
 
# Place the widgets with border Frame
label.pack(padx=1, pady=1)
border_color.pack(padx=40, pady=40)

label.pack(side= "bottom")

root.mainloop()