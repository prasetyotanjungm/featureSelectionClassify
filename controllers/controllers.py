import sys
sys.path.append('D://Bahan Belajar/SKRIPSI COY/Skripsi_road_to_jan/AppClassifOrder/view')
sys.path.append('D://Bahan Belajar/SKRIPSI COY/Skripsi_road_to_jan/AppClassifOrder/model')
print(sys.path)

import tkinter as tk
from start import StartPage
from main import MainPage 
from model import Model

class Controller(tk.Tk):
    """docstring for orderApp"""
    def __init__(self, *args):
        tk.Tk.__init__(self, *args)

        container =tk.Frame(self)
        container.pack(side="top",fill="both",expand = True)

        # rows=0
        # while rows < 50:
        #     container.grid_rowconfigure(rows,weight=1)
        #     container.grid_columnconfigure(rows,weight=1)
        #     rows += 1
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)


        self.frames = {}
# loop for switch the page
        for F in (StartPage,MainPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column = 0, sticky="nsew")

        self.show_frame(StartPage)
        # self.model = Model()
        # self.view = StartPage(container,self)
        # self.view.buttonExit.bind("<Button>",self.quit())
        # self.frames[StartPage].buttonExit.bind("<Button>",self.quit)

# raise the page 
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

    def tomainpage(controller,page):
    	controller.show_frame(MainPage)

    def quit():
        container.destroy

    def featureText(self):
        pass


    # def load_file(textSelectFile):
    #     fname = askopenfilename(filetypes=(("*.csv","Template files"),
    #                                        ("HTML files", "*.html;*.htm"),
    #                                        ("All files", "*.*") ))
    #     print(fname)
    #     # mlabel = tk.Label(self,text="%s" % fname)
    #     # mlabel.grid(row=0,column=3)
    #     # getText=self.textSelectFile.get()
    #     textSelectFile.configure(state=tk.NORMAL)
    #     textSelectFile.delete(1.0,tk.END)
    #     textSelectFile.insert(tk.END,fname)
    #     textSelectFile.configure(state=tk.DISABLED)
    
    # def quit(self):
    #     containers = self.container
    #     containers.destroy()



