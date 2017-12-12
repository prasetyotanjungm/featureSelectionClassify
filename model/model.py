import csv
import pandas as pd
import pickle 
import tkinter.filedialog

class Model():
	"""docstring for Model"""	
	def __init__(self):
		self.testX = []
		self.testY = []

	def getDataClass():
		pass

	def getDataTrain():
		pass
		
	def save_command(self):
		file = tkFileDialog.asksaveasfile(mode='w')
		if file != None:
			data = self.textPad.get('1.0', END+'-1c')
			file.write(data)
			file.close()

	def saveModel(self,model):
		modelPklFileName = ""
		modelPkl = open(modelPklFileName,'wb')
		pickle.dumb(model,modelPklFileName)
		modelPkl.close()

	def getModel():
		modelPkl = open(modelPklFileName,'rb')
		loadModelPkl = pickle.load(modelPkl)

	def getFile(self,filename):
		self.filename = filename
		file = pd.read_csv("filename")
		return file 

	def featureSelection(self):
		pass

	def readingCsv(self,fname):
		readCsv = pd.read_csv(fname)
		return readCsv

	def load_file(self,textSelectFile,frameCheckBox):
		fname = askopenfilename(filetypes=(("*.csv","Template files"),
										   ("HTML files", "*.html;*.htm"),
										   ("All files", "*.*") ))
		print(fname)
		mlabel = tk.Label(self,text="%s" % fname)
		mlabel.grid(row=0,column=3)
		# getText=self.textSelectFile.get()
		textSelectFile.configure(state=tk.NORMAL)
		textSelectFile.delete(1.0,tk.END)
		textSelectFile.insert(tk.END,fname)
		textSelectFile.configure(state=tk.DISABLED)
		self.read = self.readingCsv(fname)
		self.getColumn = self.getColumnFromCsv(self.read)
		self.dataX = self.makeData(self.read,self.getColumn)

		if self.getColumn:
			for Column in self.getColumn:
				var = tk.IntVar()
				self.variables.append(var)
				l = tk.Checkbutton(frameCheckBox,text=Column,variable=var)
				l.grid(sticky="w")

	def getColumnFromCsv(self,readCsv):
		numeric_variables = list(readCsv.dtypes[readCsv.dtypes != "object"].index)
		return numeric_variables

	def makeData(self,read,getColumn):
		dataX = read[getColumn]
		return dataX

	def transform(self,data,sfm):
		dataTransform = sfm.transform(data)
		return dataTransform

	def coba(self):
		a = 4 + 5
		print(a)
		return a	