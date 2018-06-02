from tkinter import *
import tkinter
from rightPanel import RightPanel

from reader import Reader

class LeftPanel:

    def __init__(self, left_frame):
        self.left_frame = left_frame

    def menuPane(self,):


        holder_frame = Frame(self.left_frame)
        holder_frame.pack( side = LEFT )

        '''def OnDouble(event):
            widget = event.widget
            selection=widget.curselection()
            value = widget.get(selection[0])
            print ("selection:", selection, ": '%s'" % value)'''

        mylist = Listbox(holder_frame, height = 30)

        archives = Reader('archives.xml')

        list = Reader.get_languages()

        def OnDouble(event):
            widget = event.widget
            selection=widget.curselection()
            value = widget.get(selection[0])
            print (selection[0])
            print (list[selection[0]])

        

        for a in list:
            mylist.insert(END, a)

        mylist.bind("<Double-Button-1>", OnDouble)

        mylist.pack( side = TOP, fill = BOTH)

        var = StringVar()
        label = Label( holder_frame, textvariable = var, relief = RAISED )

        var.set("Status: ...")
        label.pack(side = BOTTOM)
        