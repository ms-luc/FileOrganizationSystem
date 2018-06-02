from reader import Reader

'''
Class Place

This class returns data collected from an xml file

Part of the Progress Task application

@version 1.0
@since 13.08.2017
'''


class Place:

    #Reader
    file = None

    #list of languages
    rootList = []

    # ELEMENTS

    #left pane listbox
    branchList = None

    #selected language
    selected_item = None

    # ATTRIBUTES

    #displayed_items
    disp_item = None

    #selected disp item
    selected_disp_item = None

    #tut / project mode
    subSection = 0 #tutorials
    #adv / basic mode
    childSection = 0

    sourceSection = 0

    # selected file name and directories
    currentFile = ''

    '''
    @constructor

    @param section >>> the xml file, selected from the topMenu
    '''
    def __init__ (self, section):

        self.file = Reader(section)
        self.rootList = self.file.root

    def setFile (self, section):
        self.file = Reader(section)

    def getRootList(self):

        return self.rootList

    #root

    def getRootList(self):

        return self.rootList

    #Left Pane list

    def setBranchList(self, branch, item):

        self.branchList = self.file.get_subRoot(branch, item)

    def getBranchList(self):

        return self.branchList

    def setSelectedItem(self, item):

        self.selected_item = self.getBranchList()[item]

    def getSelectedItem(self):

        return self.selected_item

    # selected item sections

    def setSubSection(self,section):

        self.subSection = section

        self.disp_item = self.getSelectedItem()[section]


    def checkSubSection(self,section):

        if not self.getSelectedItem()[section] :
            return False

        return True


    #---additional sub methods

    def checkChildSection(self, section, child):

        if not self.getSelectedItem()[section][child] :
            return False

        return True


    def setChildSection(self, section, child):

        if(section >= 0):
            self.subSection = section

        if(child >= 0):
            self.childSection = child

        self.disp_item = self.getSelectedItem()[self.subSection][self.childSection]


    #Source section

    def getSource(self, itr):
        return self.getSelectedItem()[self.subSection][self.childSection][itr].attrib.get('category')

    def getSourceSection(self):
        return self.sourceSection

    def checkSource(self):
        if not self.getSelectedItem()[self.subSection][self.childSection]:
            return False
        return self.getSelectedItem()[self.subSection][self.childSection][0].tag == 'Source'

    def clearSource(self):

        self.sourceSection = -1

    def setSourceSection(self,source):

        if(self.checkSource()):
            self.sourceSection = source
            self.disp_item = self.getSelectedItem()[self.subSection][self.childSection][self.sourceSection]

    def getSourceLocation(self):
        if(self.checkSource()):
            return self.disp_item.attrib.get('location')

    # get display item / or get source

    def get_disp(self):
        if(self.checkSource()):
            print("Source exists")
        return self.disp_item

    def setSelectedDispItem(self,item):

        self.selected_disp_item = self.disp_item[item]

    def getSelectedDispItem(self):

        return self.selected_disp_item

    # ============================================ #

    def setCurrentFile(self, location, name):
        self.currentFile = location + name

    def getCurrentFile(self):
        return self.currentFile



'''

placer = Place('archives.xml')
placer.setBranchList(placer.getRootList(), 0)
placer.setSelectedItem(0)

liste = []
dict = {}
sources_dict = {}

bind_x = {}
bind_y = {}
bind_z = {}

placer.button_level(liste, dict, sources_dict, bind_x, bind_y, bind_z)
print(dict)

print(bind_x)
print(bind_y)
print(bind_z)

#IMPORTANT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!         sources_dict[list(sources_dict.keys())[0]]

print(sources_dict[list(sources_dict.keys())[0]])

'''

'''
print(placer.button_level_a())
print(placer.button_level_b())
print(placer.button_level_c())
'''
'''
b = placer.button_level(a[0])
print(b)
   '''
'''

placer = Place('archives.xml')

a = placer.setRootList()

print('>>> set file')
print(placer.getRootList().tag)


print('>>> set branch to \'languages\' ')
placer.setBranchList(placer.getRootList(), 0)

print('>>> print root list')
for child in placer.getBranchList():
    print(child.get('name'))

print('>>> select item')
#placer.selected_item = placer.getBranchList()[0]
placer.setSelectedItem(0)
print('>>> print selected item')
print(placer.getSelectedItem())

print('>>> print first item')
print(placer.getSelectedItem().tag)
print(placer.getSelectedItem().attrib)

print('>>> item - [0][0]')
print(placer.getSelectedItem()[0][0].tag)

print('setting sub and sub child')
placer.setSubSection(1,1)

print('>>> item - [0][0]')

print(placer.get_sub().tag)

print('>>> all items - Source ')
for child in placer.get_sub():
    for child in child:
        print(child.tag)
        print(child.attrib.get('entry'))

'''
