from tkinter import *
import tkinter
import os
 
from topMenu import TopMenu

from reader import Reader

class Main:

    root = Tk()

    '''
    FRAMES
    '''

    #main
    frame = Frame(root)
    frame.pack()

    #left

    left_frame = Frame(frame)
    left_frame.pack( side = LEFT )

    #right

    
    right_frame = Frame(frame)
    right_frame.pack( side = RIGHT )
    
    #Reader
    archives = Reader('archives.xml')
    #list of languages
    languageList = []
    #right pane listbox
    rightPane_list = None
    #tut / project mode
    tp_show = 'Tutorials'
    def decriptionPane(self,):

            text = Text(self.right_frame)
            text.insert(INSERT, "Hello.....")

            text.pack( side = BOTTOM )


    def rightPane(self):

        button_frame = Frame(self.right_frame)
        button_frame.pack( side = TOP )

        tutorial_button = Button(button_frame, text = 'Tutorials', command = lambda: self.tp_showMode('t'))
        project_button = Button(button_frame, text = 'Projets', command = lambda: self.tp_showMode('p'))

        tutorial_button.pack( side = LEFT )
        project_button.pack( side = LEFT )

        self.rightPane_list = Listbox(self.right_frame)

        self.rightPane_list.bind("<Double-Button-1>", self.OnDouble)

        self.rightPane_list.pack( side = TOP, fill = BOTH)

    
    '''
    List functions
    '''
    def listDelete(self, rightPane_list):
        rightPane_list.delete(0, 'end')

    def listUpdate(self, rightPane_list,branch):
        if(branch):
            self.listDelete(rightPane_list)
            self.listAdd(rightPane_list,branch)
        else:
            self.rightPane_list = Listbox(self.right_frame)

    def listAdd(self,rightPane_list,branch):
        list = []
        
        if(self.tp_show == 'Projects'):
            branch = branch[0]
            self.archives.all_roots(branch,'entry',list)

        if(self.tp_show == 'Tutorials'):
            branch = branch[1]
            self.archives.all_roots(branch,'entry',list)

        for a in list:
            #print(self.archives.attributeString(a, 'entry'))
            rightPane_list.insert(END, self.archives.attributeString(a, 'entry'))

    #tutorial or project show mode
    def tp_showMode(self, state):
        print('click')
        if (state == 'p'):
            self.tp_show = 'Projects'
            self.listUpdate(self.rightPane_list,self.languageList[selection[0]])
        elif (state == 't'):
            self.tp_show = 'Tutorials'
            self.listUpdate(self.rightPane_list,self.languageList[selection[0]])

    '''
    end list functions
    '''

    def OnDouble(self,event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        #self.rightPane(self.languageList[selection[0]])
        self.listUpdate(self.rightPane_list,self.languageList[selection[0]])

    def leftPane(self):

       #LEFT PANE FRAME
       holder_frame = Frame(Main.left_frame)
       holder_frame.pack( side = LEFT )

       #List declaration
       mylist = Listbox(holder_frame, height = 30)
    
       #Obtain xml 
       self.languageList = self.archives.get_subRoot(self.archives.root, 0)

       #input xml
       for a in self.languageList:
           
           mylist.insert(END, self.archives.attributeString(a, 'name'))

       mylist.bind("<Double-Button-1>", self.OnDouble)

       mylist.pack( side = TOP, fill = BOTH)

       #text bar
       var = StringVar()
       label = Label( holder_frame, textvariable = var, relief = RAISED )

       var.set("Status: ...")
       label.pack(side = BOTTOM)


    def excecute(self):

        self.leftPane()
        self.rightPane()
        self.decriptionPane()

        tm = TopMenu(self.root)

        self.root.mainloop()

        
    


exe = Main()

exe.excecute()
