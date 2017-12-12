import tkinter as tk 
from tkinter.filedialog import askopenfilename


LARGE_FONT=("Verdana", 12)
class orderApp(tk.Tk):
    """docstring for orderApp"""
    def __init__(self, *args):
        tk.Tk.__init__(self,*args)
        container =tk.Frame(self)
        container.pack(side="top",fill="both",expand = True)

        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        self.frames = {}
# loop for switch the page
        for F in (StartPage,MainPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0,column = 0, sticky="nsew")

        self.show_frame(StartPage)
# raise the page 
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

    def quit():
        container.destroy

# controller for reference to orderApp
# parent reference to tk.frame
class StartPage(tk.Frame):
    """docstring for StartPage"""
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = "StartPage", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self,text="Start",command=self.load_file)
        button1.pack()

        button2 = tk.Button(self,text="MainPage",command=lambda: controller.show_frame(MainPage))
        button2.pack()

        button3 = tk.Button(self,text="Exit",command= quit)
        button3.pack()


    def load_file(self):
        fname = askopenfilename(filetypes=(("Template files", "*.tplate"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))

class MainPage(tk.Frame):
    """docstring for MainPage"""
    def __init__(self, parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self,text = "MainPage", font = LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self,text="Back",command=lambda: controller.show_frame(StartPage))
        button1.pack()


if __name__ == "__main__":
    app = orderApp()
    app.geometry("800x200")
    app.mainloop()
    



