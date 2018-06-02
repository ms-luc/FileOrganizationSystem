from tkinter import *
import tkinter
import os

import rightPanel
import leftPanel

root = Tk()



'''
FRAMES
'''

# MAIN FRAME
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

# LEFT FRAME

leftFrame = Frame(frame)
leftFrame.pack( side = LEFT )

'''
FUNCTIONS
'''

#functions

def closeTask():
    root.close()

def endProcess():
	root.destroy()

'''
TOP MENU
'''

def donothing():
       filewin = Toplevel(root)
       button = Button(filewin, Text='Do nothing button')
       button.pack()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="New", command = donothing)
filemenu.add_command(label="Save", command = donothing)
filemenu.add_command(label="Save as...", command = donothing)
filemenu.add_command(label="Close", command = closeTask)

filemenu.add_separator()

filemenu.add_command(label="Exit", command = endProcess)

menubar.add_cascade(label = "File", menu = filemenu)

root.config(menu = menubar)


'''
BUTTONS
'''

def openLoc():
   os.popen(r'npp C:\Users\Luciant\Desktop\ReadFromWeb.class')

#buttons

quitbutton = Button(leftFrame, text = "Quit", fg = 'red' , command = closeTask)
quitbutton.pack( side = RIGHT )

quitbutton = Button(frame, text = "Open", fg = 'blue' , command = openLoc)
quitbutton.pack( side = RIGHT )


'''
LABEL
'''

var = StringVar()
label = Label(frame, textvariable  = var, relief = FLAT)

var.set("MENU")

label.pack( side = TOP )

'''
LIST
'''

Lb = Listbox(leftFrame)
Lb.insert(1, "Python")
Lb.insert(2, "Java")

Lb.pack( side = LEFT )

''' END '''

root.mainloop()
