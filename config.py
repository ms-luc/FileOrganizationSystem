
from tkinter import *
import tkinter

class Config:

    def configPrompt():
        rawConfig = ''

        #read ProgressTask.config
        configuration= open("ProgressTask.config",'a+',encoding = 'utf-8')
        configuration.seek(0,0)

        #initialize dir prompt
        dirPrompt = Tk()
        dirPrompt.title("Progress Task")

        # dirPrompt button function
        def dirPromptButton():

            nonlocal dirEntry
            nonlocal dirPrompt
            nonlocal rawConfig
            rawConfig = dirEntry.get()

            toWrite = "dir=\"" + rawConfig + "\""
            configuration.write(toWrite)

            dirPrompt.destroy()

        #in the case that there is no configuration preset. prompt user to enter the dir of Cloud
        if(configuration.read() == "" ):

            dirPrompt_Left_Panel = Frame(dirPrompt)
            dirPrompt_Right_Panel = Frame(dirPrompt)
            dirPrompt_Left_Panel.pack( side = LEFT )
            dirPrompt_Right_Panel.pack( side = RIGHT )

            dirLabel = Label(dirPrompt_Left_Panel, text="Enter the directory of Cloud: \n *Note leave \\ at the end")
            dirLabel.pack( side = LEFT)

            dirEntry = Entry(dirPrompt_Left_Panel)
            dirEntry.pack( side = RIGHT )



            dirFinish = Button(dirPrompt_Right_Panel, text = "Done", command = dirPromptButton )
            dirFinish.pack( side = RIGHT )


            dirPrompt.mainloop()

        else:
            #brings pointer to the beggining of the file.
            #needed because of the first comparion if(configuration.read() == "" )
            #takes pointer to end
            configuration.seek(0,0)

            #splits all config parameters. (P.S.) only odd numbers should be parameters but uncertain
            rawConfig = configuration.read().split("\"")[1]

            dirPrompt.destroy()

        configuration.close()

        return rawConfig
