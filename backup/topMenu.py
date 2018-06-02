from tkinter import *
import tkinter


class TopMenu:

    def __init__(self, root):
        self.root = root

        def donothing():
           filewin = Toplevel(self.root)
           button = Button(filewin, Text='Do nothing button')
           button.pack()

        def closeTask():
            root.close()

        def endProcess():
            root.destroy()

        menubar = Menu(self.root)

        #File

        filemenu = Menu(menubar, tearoff = 0)

        filemenu.add_command(label="New", command = donothing)
        filemenu.add_command(label="Save", command = donothing)
        filemenu.add_command(label="Save as...", command = donothing)
        filemenu.add_command(label="Close", command = closeTask)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command = endProcess)

        menubar.add_cascade(label = "File", menu = filemenu)

        #View

        viewmenu = Menu(menubar, tearoff = 0)

        viewmenu.add_command(label="Archives", command = donothing)
        viewmenu.add_command(label="Task", command = donothing)
        viewmenu.add_command(label="Progress", command = donothing)

        viewmenu.add_separator()
        viewmenu.add_command(label="Useful Links", command = donothing)

        menubar.add_cascade(label = "View", menu = viewmenu)


        self.root.config(menu = menubar)

    

    