#shelves on which to store books

# from typing import Any
from tkinter import Entry, Canvas, Checkbutton, Radiobutton, Frame, RADIOBUTTON, Grab, Grid, PanedWindow, tkinter as tk
#May use the following:
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_entry.htm#M56
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_checkbutton.htm
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_radiobutton.htm
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_frame.htm
#https://tcl.tk/man/tcl8.6/TkCmd/grab.htm#M12
#https://tcl.tk/man/tcl8.6/TkCmd/grid.htm
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_panedwindow.htm

class to_read:
    def __init__(self, to_read_books):
        self.to_read_books = to_read_books

class currently_reading:
    def __init__(self, reading):
        self.reading = reading

class completed_books:
    def __init__(self, book_read):
        #completed doesn't mean the entire book was read, necessarially, just that you won't be reading anymore, ever
        self.book_read = book_read
