from tkinter import *
from subprocess import check_output
from subprocess import Popen
import subprocess


import tkinter

from place import Place

class TopMenu:

    def __init__(self, root, placer):
        self.root = root

        def donothing():
           filewin = Toplevel(self.root)
           button = Button(filewin, Text='Do nothing button')
           button.pack()

        def openWithNPP():

           print(placer.getCurrentFile())
           cmd = 'npp ' + placer.getCurrentFile()
           subprocess.call([r'C:\Users\Luciant\Desktop\Cloud\Documents\Projects\Batch\npp.bat',
                            placer.getCurrentFile()])

        def closeTask():
            root.close()

        def endProcess():
            root.destroy()

        menubar = Menu(self.root)

        #File

        filemenu = Menu(menubar, tearoff = 0)

        filemenu.add_command(label="Open File with NotePad++ ", command = openWithNPP)
        filemenu.add_command(label="Open Archive (.xml)", command = donothing)
        filemenu.add_command(label="Close", command = closeTask)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command = endProcess)

        menubar.add_cascade(label = "File", menu = filemenu)

        # Edit

        editMenu = Menu(menubar, tearoff = 0)

        editMenu.add_command(label="New Entry", command = donothing)
        editMenu.add_command(label="Edit Current", command = donothing)

        menubar.add_cascade(label = "Edit", menu = editMenu)

        # View

        viewmenu = Menu(menubar, tearoff = 0)

        viewmenu.add_command(label="Archives", command = lambda: placer.setFile("archives.xml"))
        viewmenu.add_command(label="Task", command = lambda: placer.setFile("task.xml"))
        viewmenu.add_command(label="Progress", command = lambda: placer.setFile("progress.xml"))
        viewmenu.add_command(label="Tools", command = lambda: placer.setFile("progress.xml"))

        viewmenu.add_separator()
        viewmenu.add_command(label="Useful Links/Notes", command = donothing)
        viewmenu.add_command(label="General Items", command = donothing)

        menubar.add_cascade(label = "View", menu = viewmenu)


        self.root.config(menu = menubar)
