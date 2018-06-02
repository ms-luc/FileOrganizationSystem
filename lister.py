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

    def toList(branch,attrib):

        list = []

        for child in branch:
           list.append(child.attrib.get(attrib))

        return list
