import tkinter as tk
import main 
from PIL import ImageTk,Image

LARGE_FONT=("Verdana", 12)
class StartPage(tk.Frame):
    """docstring for StartPage"""
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        # edited
        self.controller = controller
        
        load = Image.open("D://676392.JPG")
        render = ImageTk.PhotoImage(load)

        img = tk.Label(self,image=render)
        img.image = render
        img.grid(row=0,rowspan=4,sticky="nw",columnspan=4)

        # path = "D://67639.JPG"
        # img = ImageTk.PhotoImage(Image.open(path))
        # panel = tk.Label(self,image=img)
        # panel.grid(row=0,columnspan=2)
        

        text = tk.Label(self,text="when the the snows fall")
        text.grid(row=4,column=0,sticky="w")

        text = tk.Label(self,text="and the white winds blow, the lone")
        text.grid(row=5,column=0,sticky="w")
        
        text = tk.Label(self,text="wolf dies but the pack survives")
        text.grid(row=6,column=0,sticky="w")
        

        buttonFrame = tk.LabelFrame(self, text = "Application")
        buttonFrame.grid(row=0,column=1,sticky="NES",padx=5, pady=5, ipadx=2, ipady=5,rowspan=6,columnspan=5)
        
        buttonCreateModel = tk.Button(buttonFrame,text="Create Model",command=lambda: controller.show_frame(main.MainPage))
        buttonCreateModel.grid(row=0,column=1,sticky="new",pady=2)

        buttonKlasifikasi = tk.Button(buttonFrame,text="Klasifikasi")
        buttonKlasifikasi.grid(row=1,column=1,sticky="new",pady=2)

        buttonHistory = tk.Button(buttonFrame,text="History")
        buttonHistory.grid(row=3,column=1,sticky ="new",pady=2)

        buttonExit = tk.Button(buttonFrame,text="Exit",command= quit)
        # buttonExit.bind("<Button>",self.controller.quit())
        buttonExit.grid(row=4,column=1,sticky="new",pady=2)


    def load_file(self):
        fname = askopenfilename(filetypes=(("*.csv","Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))

    