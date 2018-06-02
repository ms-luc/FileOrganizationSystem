

class file_reader:

    text = None

    def __init__(self, file, location):

        item = location + file

        f = open(item,'r',encoding = 'utf-8')

        self.text = f.read()

    def getText(self):

        return self.text

#a = file_reader('loops.bat','C:/Users/Luciant/Desktop/Cloud/Documents/Workspace/Batch/')

# r'C:/'/'/'/'' ...

#print(a.getText())