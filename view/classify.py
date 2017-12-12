import tkinter as tk
from tkinter import ttk
import main

class Classify(tk.Frame):

	def __init__(self, parent,controller):
		tk.Frame.__init__(self,parent)

		self.controller = controller

		# self.dataX = main.dataX
		# self.sfm = main.sfm

		selectClassFrame = tk.LabelFrame(self,text = "Select Test File")
		selectClassFrame.grid(row=0,column=0,sticky="WE",padx=5,pady=5,ipady=5,columnspan=10)

		selectTestOptionFrame = tk.LabelFrame(self,text = "Test Option")
		selectTestOptionFrame.grid(row=2,column=0,sticky="W",padx=5,pady=5,ipady=5)

		outputFrame = tk.LabelFrame(self,text = "Classifier Output")
		outputFrame.grid(row = 2,column =1,sticky="W",padx=5,pady=5,ipady=5)

		textSelectFile = tk.Text(selectClassFrame,width = 28, height = 1)
		textSelectFile.grid(row=0,column=1,sticky="WE",pady=3,padx=5)

		button1 = tk.Button(selectClassFrame,text = "hallo")
		button1.grid(row= 0,column = 0)

		buttonStart = tk.Button(selectTestOptionFrame,text = "Start" , command = lambda: controller.transform())
		buttonStart.grid(row = 0, column = 0 )

		buttonStop = tk.Button(selectTestOptionFrame,text = "Stop" )
		buttonStop.grid(row = 0, column = 1 )

		outputCanvas = tk.Text(outputFrame,width = 60, height = 15)
		outputCanvas.grid(row = 0,column = 0,sticky = "news" )



	def transform(a):
		dataTransform = a.sfm.transform(a.dataX)
		print (dataTransform)
		return dataTransform


