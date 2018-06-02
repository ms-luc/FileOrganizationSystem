import xml.etree.ElementTree as ET

'''
Class Reader

This class obtains data from an XML file

Part of the Progress Task application

@version 1.0
@since 05.08.2017
'''

class Reader:

    '''
    @constructor

    @param xml_file
    '''
    def __init__(self, xml_file):
        tree = ET.parse(xml_file)
        Reader.root = tree.getroot()

    '''
    @attributeString

        Obtains a single attribute from an XML Root or Child.

    @param branch >>> the given root
    @param attribute >>> the xml attribute
    '''
    def attributeString(self,branch, attribute):
        return branch.attrib.get(attribute)

    '''
    @get_subRoot

        Retrieves the next level of a branch. Returns them in a list

    @var list >>> returned list with children

    @param branch >>> the root of the sub root
    @param item >>> the item number in the Root
    
    @return list
    '''
    def get_subRoot(self, branch, item):

        list = []

        for child in branch[item]:
            list.append(child)

        return list

    '''
    @all_roots

        Puts all the Children of a root into a list. If specified the function
        puts only elements with specific attributes into the list.

    @param list >>> given list
    @param branch >>> specified branch
    @param item >>> XML attribute
    '''
    def all_roots(self, branch, item, list):

        for child in branch:
            if(item):
                if (child.attrib.get(item)):
                    list.append(child)
                    print("%s" % child.attrib.get("entry"))
                else:
                    self.all_roots(child, item, list)
            else:
                list.append(child)
                self.all_roots(child, item, list)
                


'''
archives = Reader('archives.xml')

list = []
print(archives.root[0][0].tag, archives.root[0][0].attrib)
'''

        
'''
root[0][0].tag
root[0][0][0].text

child.attrib.get("name")


if (child.tag == 'location' and child.text == 'default'):
    print('\t %s: %s' %(child.tag, loc))

'''