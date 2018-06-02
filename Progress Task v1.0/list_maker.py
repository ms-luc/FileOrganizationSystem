from tkinter import *
import tkinter
from place import Place

class Lister:

    placer = Place('archives.xml')

    placer.setBranchList(placer.getRootList(), 0)

    def __init__(self):
        a = 1

    def listDelete(self, paneList):
        paneList.delete(0, 'end')

    def listAdd(self,paneList,list):
         for child in list:
             paneList.insert(END, child)

    def listUpdate(self,paneList,list):
        self.listDelete(paneList)
        self.listAdd(paneList,list)

    def toList(self, branch, type, attrib):

        list = []

        if( type == 'attrib'):
            for child in branch:
               list.append(child.attrib.get(attrib))
        elif( type == 'text' ):
            for child in branch:
               list.append(child.text)

        return list


'''
placer = Place('archives.xml')

placer.setBranchList(placer.getRootList(), 0)
placer.setSelectedItem(0)
placer.setChildSection(1,0)
#placer.setSourceSection(0)

print(placer.getSelectedItem()[0][0][0].attrib.get('entry'))
print(placer.get_disp()[0][0])
print(Lister.toList(placer.get_disp(), 'attrib', 'category'))
'''
