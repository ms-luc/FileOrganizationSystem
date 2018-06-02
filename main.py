'''

MAP OUT ALL FRAMES

frame
->left_frame
    -langList

->right_frame
    -itemList
    -itemDetails

Progress/Archives

left_frame  / right_frame
--------------------------------------
|           |      button_frame      |
|  langList |------------------------|
|           | itemList | itemDetails |
|           |------------------------|
|           |       itemText         |
--------------------------------------

Tasks:
--------------------------------------
list all tasks
-
-
-
-
--------------------------------------

Links:
--------------------------------------
list all links
-
-
-
-
--------------------------------------

Progress/Graph
--------------------------------------
some visualisation
       |
|   |  | -  =   |   |          |
|   |  | |  |   |   |   |   |  |
--------------------------------------



name rules:

    frames have '_' for spaces:
        frame_title

    widgets have capitals for spaces:
        widgetTitle

code layout:

    -declaration of frames and widgets
    -right_frame button functions
    -right_frame()
    -left_frame()
    -excecute() # excecutes all functions


'''
from functools import partial
from tkinter import *
import tkinter
import os

from topMenu import TopMenu
from place import Place
from list_maker import Lister
from file_reader import file_reader
from config import Config


class Main:

    '''
    CONFIG PROMPT
    '''


    global cloudDirectory
    cloudDirectory = Config.configPrompt()

    '''
    CONFIG PROMPT END
    '''

    global root
    root = Tk()

    root.title("Progress Task")

    '''
    # global variables
    '''

    # ~

    '''
    # end global variables
    '''

    '''
    #global functions
    '''
    global fillList
    def fillList(thisList, getBranch, branch, attrib):
        thisList.delete(0, 'end')

        #print(lister.toList(getBranch(), branch, attrib))

        for a in lister.toList(getBranch(), branch, attrib):

            thisList.insert(END, a)

        #clear list
        #fill with selected

       # =---------------------------------------------------=

    global addList
    def addList(thisList, getBranch, branch, attrib):

        for a in lister.toList(getBranch(), branch, attrib):

            thisList.insert(END, a)
        #fill with selected
       # =---------------------------------------------------=

    global clearList
    def clearList(thisList):
        thisList.delete(0, 'end')

    #@listBox_OnDouble
    #
    # selectFunction is a function from 'placer' class used to select a row
    # from an XML file
    #
    #returns: void

    global listBox_OnDouble
    def listBox_OnDouble(event, selectFunction, listFunction):#, selectFunction):

        widget = event.widget
        selection=widget.curselection()
        #value = widget.get(selection[0])

        # select item using appropriate select function for list from placer
        selectFunction(selection[0])

        # call function assigned to the list
        listFunction()

    #@langListFunct
    #
    # this function will update the itemList list after clicking on
    # a language from langList
    #
    #returns: void
    global langListFunct
    def langListFunct():

        # reset all selection values to avoid error

        #none because the function excecutes and sets disp item when called
        if placer.checkChildSection(0,1):
            placer.setChildSection(0,1)

        if placer.checkChildSection(0,0):
            placer.setChildSection(0,0)

        clearFrame(button_options_frame)
        clearFrame(button_frame)
        rightPane()

        #clear disp panes
        itemText.delete(1.0, 'end')
        itemDetails.delete(0, 'end')
        #clear end

        fillList( itemList, placer.getSelectedItem, 'attrib', 'entry')

    #@itemDetailsListFunct
    #
    # this function will update the itemDetails list and itemText after clicking on
    # a file from itemList
    #
    #returns: void
    global itemListFunct
    def itemListFunct(event):

        #list OnDouble function part

        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])

        # end -> list OnDouble function part

        # selection algorithm for selecting correct display item

            #for tutorials  ^^^^^^^^^
        if(tut):
            if( value in orderItemDetailsBasDict ):

                temp = orderItemDetailsBasDict[value]

                placer.setChildSection(1,0)
                placer.setSourceSection( list(sourceSelectedBasicDict.keys()).index( temp ) )
                placer.setSelectedDispItem( list(lister.toList(placer.get_disp(),
                                            'attrib', 'entry')).index( value ) )

            elif( value in orderItemDetailsAdvDict ):

                print('\nTHING\n')
                print(orderItemDetailsAdvDict)
                print(sourceSelectedAdvancedDict)
                print('\nTHING')

                temp = orderItemDetailsAdvDict[value]

                print(temp )

                placer.setChildSection(1,1)
                print( list(sourceSelectedAdvancedDict.keys()).index( temp ) )
                placer.setSourceSection( list(sourceSelectedAdvancedDict.keys()).index( temp ) )
                placer.setSelectedDispItem( list(lister.toList(placer.get_disp(),
                                            'attrib', 'entry')).index( value ) )

            #for projects  ^^^^^^^^^
        if(pro):

            if( value in orderItemDetailsBasDict):
                placer.setChildSection(0,0)
                placer.setSelectedDispItem( selection[0] )


            else:
                placer.setChildSection(0,1)
                placer.setSelectedDispItem( selection[0] - len(orderItemDetailsBasDict) )


        # itemDetails

        #reset contents
        itemText.delete(1.0, 'end')
        itemDetails.delete(0, 'end')

        #variables to be retrieved from the loop
        disp_file_name = None
        disp_file_location = None
        disp_file_non_cloud_location = None

        #this loop places all of the file descriptors
        for a in placer.getSelectedDispItem():
            string = ''
            string = '%s:      %s' %(a.tag, a.text)
            itemDetails.insert(END, string)

            if(a.tag == 'name'):
                disp_file_name = a.text

            if(a.tag == "location"):
                disp_file_location = a.text
            if(a.tag == "non_cloud"):
                disp_file_non_cloud_location = a.text

        # itemDetails end

        # itemText

        if(disp_file_location == 'default' and tut):

            disp_file_location = cloudDirectory + placer.getSourceLocation()
            #source dir check: print("%s%s" %(self.cloudDirectory, placer.getSourceLocation()))

        elif(disp_file_location == 'non cloud'):

            disp_file_location = disp_file_non_cloud_location

        elif(disp_file_location == None):

            #no location found
            return None

        else:

            #set to given location
            disp_file_location = cloudDirectory + disp_file_location


        #read file
        current_file = file_reader(disp_file_name, disp_file_location)

        #print to pane
        itemText.insert(END, current_file.getText())

        # itemText end

        # sets the file name and location for 'File -> Open with NPP'
        placer.setCurrentFile(disp_file_location, disp_file_name)

    global clearFrame
    def clearFrame(frame):
        list = frame.grid_slaves()
        for l in list:
            l.destroy()

    '''
    #global functions end
    '''

    '''
    FRAMES
    '''

    #main
    frame = Frame(root)
    frame.pack()

    #left

    left_frame = Frame(frame)
    left_frame.grid(row = 0, column = 0 )

    #right
    global right_frame
    right_frame = Frame(frame)
    right_frame.grid( row = 0, column = 1 )

    #button frame
    global button_frame
    button_frame = Frame(right_frame)
    button_frame.grid( row = 0, column = 0 )

    #button options frames
    global button_options_frame
    button_options_frame = Frame(right_frame)
    button_options_frame.grid( row = 0, column = 1 )

    '''
    #external file functions
    '''

    #leftPaneList
    leftPaneList = None

    #placer

    global placer
    placer = Place('archives.xml')
    placer.setBranchList(placer.getRootList(), 0)
    placer.setSelectedItem(0)

    #lister
    global lister
    lister = Lister()

    #TopMenu

    topMenu = TopMenu(root, placer)

    '''
    # ext file funct END
    '''

    '''
    # list boxes
    '''
    global langList
    global itemList
    global itemDetails
    global itemText

    # Right Pane File/Item List box

    itemList = Listbox(right_frame)

    #itemList.bind("<Double-Button-1>", lambda event:  listBox_OnDouble(event, placer_funct, list_funct))
    itemList.grid( row = 1, column = 0 )
    itemList.bind("<Double-Button-1>", lambda event: itemListFunct(event))
    #end

    # Right Pane description/details of file/item list box

    itemDetails = Listbox(right_frame, width = 80)
    itemDetails.grid( row = 1, column = 1 )

    #end

    #file display pane in right pane

    itemText = Text(right_frame)
    #self.itemText.grid( row = 2, column = 0 )
    itemText.grid( row = 2, columnspan = 2 )
    #end

    # Left Pane Lang list box

    langList = Listbox(frame, height = 30)
    langList.grid( row = 0, column = 0 )

    #sets initial section to avoid error
    placer.setChildSection(0,0)
    #clear source to avoid error
    placer.clearSource()

    langList.bind("<Double-Button-1>", lambda event:
                  listBox_OnDouble(event, placer.setSelectedItem, langListFunct))

    '''
    # end list boxes
    '''

    '''
    # RIGHT Pane
    '''

    '''

    Description:
    ------------

    right pane consts of a display frame
    and of a button frame

    the button frame contains options managing which items to display in
    the itemList

    -------------


    Button frame:
    -------------

    rightPane()
    ->radioButtons
        -projectsButton
            command:
                projectsButtonFunct()
                ->checkBoxes
                    command:
                        itemListOptions()

        -tutorialsButton
            command:
                projectsButtonFunct()
                ->checkBoxes
                    command:
                        itemListOptions()
                ->menu
                    command:
                        setTutorialSource()




    -------------

    Display frame:
    -------------

    Contains 3 widgits

    itemList: lists all items/files related to the selected language
    itemDetails: details of selected item/file
    itemText: text of selected item/file

    -------------


    '''

    global tut
    global pro

    tut = 0
    pro = 0

    global projectsButtonFunct
    def projectsButtonFunct():

        #delete tut buttons and clear panes

        global orderItemDetailsBasDict
        global orderItemDetailsAdvDict
        orderItemDetailsBasDict = {}
        orderItemDetailsAdvDict = {}

        global currentOpt1
        global currentOpt2
        currentOpt1 = 0
        currentOpt2 = 0

        global tut
        global pro

        tut = 0
        pro = 1

        clearFrame(button_options_frame)

        clearList( itemList )

        #clear
        itemText.delete(1.0, 'end')
        itemDetails.delete(0, 'end')
        #clear end

        #test if exists
        if not placer.checkSubSection(0):
            return None

        if not (placer.checkChildSection(0,0) or placer.checkChildSection(0,1)) :
            return None
        #end

        #solitary/ incorporated

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()

        C1 = Checkbutton(button_options_frame, text = "Solitary",
                         variable = CheckVar1, \
                         onvalue = 1, offvalue = 0,
                         command = lambda :
                         itemListOptions( 0 ,
                         CheckVar1.get(),
                         CheckVar2.get(), ))

        C2 = Checkbutton(button_options_frame, text = "Incorporated",
                         variable = CheckVar2, \
                         onvalue = 1, offvalue = 0,
                         command = lambda :
                         itemListOptions( 0 ,
                         CheckVar1.get(),
                         CheckVar2.get(), ))

        C1.grid( row = 0, column = 2, sticky = E, pady = 1 )
        C2.grid( row = 0, column = 3, sticky = E, pady = 1 )

        #solitary/ incorporated end

    global sourceSelectedBasicDict
    global sourceSelectedAdvancedDict
    sourceSelectedBasicDict = {}
    sourceSelectedAdvancedDict = {}

    global setBasTutorialSource
    def setBasTutorialSource(source):

        print('bas', source, sourceSelectedBasicDict[source])

        sourceSelectedBasicDict[source] = sourceSelectedBasicDict[source] * -1

        print('bas hit',sourceSelectedBasicDict[source])

        itemListOptions( 1, currentOpt1, currentOpt2)

    global setAdvTutorialSource
    def setAdvTutorialSource(source):

        print('adv', source, sourceSelectedAdvancedDict[source])

        sourceSelectedAdvancedDict[source] = sourceSelectedAdvancedDict[source] * -1

        print('adv hit',sourceSelectedAdvancedDict[source])

        itemListOptions( 1, currentOpt1, currentOpt2)


    #check below funct
    global sourceTestList

    global tutorialsButtonFunct
    def tutorialsButtonFunct():

        #clear

        global orderItemDetailsBasDict
        global orderItemDetailsAdvDict
        orderItemDetailsBasDict = {}
        orderItemDetailsAdvDict = {}

        global sourceSelectedBasicDict
        global sourceSelectedAdvancedDict
        sourceSelectedBasicDict = {}
        sourceSelectedAdvancedDict = {}

        global currentOpt1
        global currentOpt2
        currentOpt1 = 0
        currentOpt2 = 0

        global tut
        global pro

        pro = 0
        tut = 1

        #delete project butons
        clearFrame(button_options_frame)
        clearList( itemList )

        itemText.delete(1.0, 'end')
        itemDetails.delete(0, 'end')
        #clear end

        #test if tutorials exist
        if not placer.checkSubSection(1):
            return None

        if not (placer.checkChildSection(1,0) or placer.checkChildSection(1,1)) :
            return None
        #end

        #source menu
        sourceMenu = Menubutton ( button_options_frame, text="Source", relief=RAISED )

        sourceMenu.menu =  Menu ( sourceMenu, tearoff = 0 )
        sourceMenu["menu"] =  sourceMenu.menu

        #test list for repetition #global declaration above
        global sourceTestList
        sourceTestList = []

        counter = 0

        #this loop places all sources from basic branch
        placer.setChildSection(1,0)
        for a in lister.toList(placer.get_disp(),'attrib', 'category'):

            sourceTestList.append(a)

            s = IntVar()


            chk = sourceMenu.menu.add_checkbutton ( label = a,
                              variable = IntVar(),
                              command = lambda a=a: setBasTutorialSource( a ))

            sourceSelectedBasicDict[a] = -1

        #this loop places all sources from advanced branch
        placer.setChildSection(1,1)
        for b in lister.toList(placer.get_disp(),'attrib', 'category'):

            s = IntVar()
            if( not (b in sourceTestList) ):
                sourceMenu.menu.add_checkbutton ( label = b,
                              variable = IntVar(),
                              command = lambda b=b: setAdvTutorialSource( b ))

            sourceSelectedAdvancedDict[b] = -1

        sourceMenu.grid( row = 0, column = 4, sticky = E, pady = 1 )

        #source menu end

        #basic/ Advanced

        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        C1 = Checkbutton(button_options_frame, text = "Basic",
                         variable = CheckVar1, \
                         onvalue = 1, offvalue = 0,
                         command = lambda :
                         itemListOptions(  1,
                         CheckVar1.get(),
                         CheckVar2.get()))

        C2 = Checkbutton(button_options_frame, text = "Advanced",
                         variable = CheckVar2, \
                         onvalue = 1, offvalue = 0,
                         command = lambda :
                         itemListOptions( 1,
                         CheckVar1.get(),
                         CheckVar2.get()))

        C1.grid( row = 0, column = 2, sticky = E, pady = 1 )
        C2.grid( row = 0, column = 3, sticky = E, pady = 1 )

        #basic/ Advanced end

    # itemListOptions( proORtut, opt1, opt2, source):
    # uses two global variables, sets opt1 and opt2 to global
    #
    # opt1 for basic
    # opt2 for advanced
    #
    # proORtut tells the function which to display projects or tutorials
    #
    # this function is used in both tutorialsButtonFunct() and projectsButtonFunct()
    #
    global itemListOptions
    global currentOpt1
    global currentOpt2

    # these dictionaries hold file to source correspondace
    # for basic and advanced sections
    global orderItemDetailsBasDict
    global orderItemDetailsAdvDict
    orderItemDetailsBasDict = {}
    orderItemDetailsAdvDict = {}

    def itemListOptions( proORtut, opt1, opt2 ):

        global currentOpt1
        global currentOpt2
        currentOpt1 = opt1
        currentOpt2 = opt2

        global orderItemDetailsBasDict
        global orderItemDetailsAdvDict
        orderItemDetailsBasDict = {}
        orderItemDetailsAdvDict = {}


        if(opt1 and opt2):
            clearList( itemList )

            placer.setChildSection( proORtut, 0 )
            if(proORtut):
                counter = 0

                for a in lister.toList(placer.get_disp(),'attrib', 'category'):
                    if( sourceSelectedBasicDict[a] == 1 ):
                        placer.setSourceSection( counter )

                        for item in lister.toList(placer.get_disp(), 'attrib', 'entry'):

                            itemList.insert(END, item)

                            orderItemDetailsBasDict[item] = a

                    counter+=1

                print('bas', orderItemDetailsBasDict)

            else:
                addList( itemList, placer.get_disp, 'attrib', 'entry' )

                for item in lister.toList(placer.get_disp(), 'attrib', 'entry'):

                    orderItemDetailsBasDict[item] = -1

            placer.setChildSection( proORtut, 1 )
            if(proORtut):
                counter = 0

                for a in lister.toList(placer.get_disp(),'attrib', 'category'):

                    if( a in sourceSelectedBasicDict ):
                        if( sourceSelectedBasicDict[a] == 1 ):
                            placer.setSourceSection( counter )

                            for item in lister.toList(placer.get_disp(), 'attrib', 'entry'):

                                itemList.insert(END, item)

                                orderItemDetailsAdvDict[item] = a

                    if( sourceSelectedAdvancedDict[a] == 1 ):
                        placer.setSourceSection( counter )

                        for item in lister.toList(placer.get_disp(), 'attrib', 'entry'):

                            itemList.insert(END, item)

                            orderItemDetailsAdvDict[item] = a
                    counter+=1

                print('adv', orderItemDetailsAdvDict)
            #placer.setSourceSection(source)
            else:
                addList( itemList, placer.get_disp, 'attrib', 'entry' )


        if( opt1 and (not opt2) ):

            clearList( itemList )

            placer.setChildSection( proORtut, 0 )

            if( proORtut ):
                counter = 0

                for a in lister.toList(placer.get_disp(),'attrib', 'category'):
                    if( sourceSelectedBasicDict[a] == 1 ):
                        placer.setSourceSection( counter )

                        for item in lister.toList(placer.get_disp(), 'attrib', 'entry'):

                            itemList.insert(END, item)

                            orderItemDetailsBasDict[item] = a

                    counter+=1
                print('bas', orderItemDetailsBasDict)
            else:
                fillList( itemList, placer.get_disp, 'attrib', 'entry' )

                for item in lister.toList(placer.get_disp(), 'attrib', 'entry'):

                    orderItemDetailsBasDict[item] = -1

        if( (not opt1) and opt2 ):

            clearList( itemList )

            placer.setChildSection( proORtut, 1 )

            if( proORtut ):
                counter = 0

                for a in lister.toList(placer.get_disp(),'attrib', 'category'):

                    if( a in sourceSelectedBasicDict ):
                        if( sourceSelectedBasicDict[a] == 1 ):
                            placer.setSourceSection( counter )

                            for item in lister.toList(placer.get_disp(), 'attrib', 'entry'):

                                itemList.insert(END, item)

                                orderItemDetailsAdvDict[item] = a

                    if( sourceSelectedAdvancedDict[a] == 1 ):
                        placer.setSourceSection( counter )

                        for item in lister.toList(placer.get_disp(), 'attrib', 'entry'):

                            itemList.insert(END, item)

                            orderItemDetailsAdvDict[item] = a

                    counter+=1
                print('adv', orderItemDetailsAdvDict)

            else:
                fillList( itemList, placer.get_disp, 'attrib', 'entry' )

        if( ( not opt1 ) and  ( not opt2 ) ):
            clearList( itemList )


    '''
    #itemListOptions helper functions
    '''


    '''
    #itemListOptions helper functions END
    '''

    global rightPane
    def rightPane():

        v = IntVar()

        projectsButton = Radiobutton(button_frame,
                            text="Projects",
                            variable = v,
                            value = 1,
                            command = projectsButtonFunct)

        tutorialsButton = Radiobutton(button_frame,
                               text="Tutorials",
                               variable = v,
                               value = 2,
                               command = tutorialsButtonFunct)

        projectsButton.grid( row = 0, column = 0, sticky = W, padx = 1 )
        tutorialsButton.grid( row = 0, column = 1, sticky = E, pady = 1 )


    '''
    # RIGHT Pane END
    '''

    #@makeList
    #
    #note: framePackSide takes: LEFT, RIGHT, TOP, BOTTOM.
    #
    #toList(self,branch,attrib)
    #
    #returns: void
    def makeList(self, frame, branch, attrib):

       mylist = Listbox(frame, height = 30)

       #input branch list
       for a in lister.toList(placer.getBranchList(), branch, attrib):

           mylist.insert(END, a)

       # a placer function for selecting a row in XML file
       placer_funct = placer.setSelectedItem
       list_funct = print

       mylist.bind("<Double-Button-1>", lambda event:  listBox_OnDouble(event, placer_funct, list_funct))

       mylist.pack( side = framePackSide, fill = BOTH)


    def excecute(self):

        #left frame list
        #holder_frame = Frame(Main.left_frame)
        #holder_frame.grid( column = 0 )
        fillList(langList,placer.getBranchList,'attrib', 'name')



        rightPane()


        #tm = TopMenu(self.root)

        root.mainloop()

exe = Main()
exe.excecute()
