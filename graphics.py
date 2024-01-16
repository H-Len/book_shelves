# from typing import Any
from tkinter import Entry, Canvas, Checkbutton, Radiobutton, Frame, RADIOBUTTON, Grid, PanedWindow, Tk, BOTH
#May use the following:
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_entry.htm#M56
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_checkbutton.htm
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_radiobutton.htm
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_frame.htm
#https://tcl.tk/man/tcl8.6/TkCmd/grab.htm#M12
#https://tcl.tk/man/tcl8.6/TkCmd/grid.htm
#https://tcl.tk/man/tcl8.6/TkCmd/ttk_panedwindow.htm

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("All Books")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg = "yellow", height = height, width = width)
        self.__canvas.pack(fill = BOTH, expand = 5)
        self.__running = False


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
 
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def draw_line(self, line, fill_color="brown"):
        line.draw(self.__canvas, fill_color)

    def close(self):
        self.__running = False