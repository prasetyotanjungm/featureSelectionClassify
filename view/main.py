import tkinter as tk
from tkinter import ttk
import start
from tkinter.filedialog import askopenfilename
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
import classify

LARGE_FONT=("Verdana", 12)

class MainPage(tk.Frame):
	"""docstring for MainPage"""
	def __init__(self, parent,controller):
		tk.Frame.__init__(self,parent)
		self.controller = controller
		self.read = []
		self.getColumn = []
		self.dataX = []
		self.dataY = []
		self.variables = []
		self.featureImportance = []
		self.clf = []
		self.featureFix = []
		self.sfm = []
		self.createWidgets()
		
		# nb = ttk.Notebook(self)
		# nb.grid(row=1,column=0,columnspan=50,rowspan=49,sticky="NESW")
		# page1 = ttk.Frame(nb)
		# nb.add(page1,text="MainPageing"
	
	def createWidgets(self):
		self.createPanel()

	def createPanel(self):
		nb = ttk.Notebook(self)
		nb.grid(row=1,column=0,columnspan=50,rowspan=49,sticky="NEWS")
		self.createMainPageTab(nb)
		self.addTab(nb)

	def addTab(self,nb):
		page2 = classify.Classify(nb,self)
		nb.add(page2,text="Classify")


	def createMainPageTab(self,nb):
		self.featureSelection = tk.IntVar()
		self.varScale = tk.DoubleVar()

		page1 = ttk.Frame(nb)
		nb.add(page1,text="Preprocessing")

		selectFileFrame = tk.LabelFrame(page1,text = "Select File")
		selectFileFrame.grid(row=0,column=0,sticky="WE",padx=5,pady=5,ipady=5,columnspan=10)

		selectRoleFrame = tk.LabelFrame(page1,text = "select Role")
		selectRoleFrame.grid(row=1,column=0,sticky="NEWS",padx=5,pady=5,ipady=5,columnspan=1,rowspan=1)

		selectFeatureFrame = tk.LabelFrame(page1,text = "Feature Selection")
		selectFeatureFrame.grid(row=1,column=1,sticky="NEWS",padx=5,pady=5,ipady=5)

		text = tk.Label(selectFileFrame,text="Select The File")
		text.grid(row=0,column=0, sticky="W")

		textSelectFile = tk.Text(selectFileFrame,width = 28, height = 1)
		textSelectFile.grid(row=0,column=1,sticky="WE",pady=3,padx=5)

		buttonSelectFile = tk.Button(selectFileFrame,text="browse...",command=lambda : self.load_file(textSelectFile,frameCheckBox))
		buttonSelectFile.grid(row=0,column=2,sticky="E")

	
		# canvasScroll=tk.Canvas(selectRoleFrame,width=100,height=100,scrollregion=(0,0,100,200))

		# vBar = tk.Scrollbar(selectRoleFrame,orient = "vertical")
		# vBar.grid(row=0,column=1,sticky="ns")
		# vBar.config(command=canvasScroll.yview)
		# canvasScroll.config(yscrollcommand=vBar.set)
		# canvasScroll.grid()

		canvasScroll = tk.Canvas(selectRoleFrame,bg="Yellow")
		canvasScroll.grid(row=0,column=0)

		vBar = tk.Scrollbar(selectRoleFrame,orient="vertical",command=canvasScroll.yview)
		vBar.grid(row=0,column=1, sticky="ns")
		canvasScroll.configure(yscrollcommand=vBar.set)

		buttonCek2 = tk.Button(selectRoleFrame,text = "Print" , command= lambda:self.dropAttribute())
		buttonCek2.grid(row=1,column=0)

		frameCheckBox = tk.Frame(canvasScroll,bg="blue",bd=2,relief=tk.GROOVE)
		canvasScroll.create_window((0,0), window=frameCheckBox,anchor="nw")

		result = self.resize(canvasScroll)
		frameCheckBox.bind("<Configure>",lambda event:self.resize(canvasScroll))

		checkButtonFeatureSelection = tk.Checkbutton(selectFeatureFrame, text= "Feature Selection",variable = self.featureSelection)
		checkButtonFeatureSelection.grid(row=0,column=0,sticky="w") 

		# textFeature = tk.Text(selectFeatureFrame)
		# textFeature.grid(row=2,column=0, sticky ="news")
		listBoxFeature = tk.Listbox(selectFeatureFrame)
		listBoxFeature.grid(row=2,column=0,sticky="news")

		forScaleFrame = tk.Frame(selectFeatureFrame)
		forScaleFrame.grid(row = 2,column = 1,sticky="NEWS")

		# listBoxFeatureSelected = tk.Listbox(selectFeatureFrame)
		# listBoxFeatureSelected.grid(row=2,column = 2,sticky="NEWS")

		buttonCek = tk.Button(selectFeatureFrame, text='Show', command= lambda : self.feature_importance(listBoxFeature,checkButtonFeatureSelection))
		buttonCek.grid(row=1,column=0,sticky="W")

		# buttonSaveModel = tk.Button(selectFeatureFrame,text="save..")
		# buttonSaveModel.grid(row=1,column=2,sticky="w")

		self.labelThreshold = tk.Label(forScaleFrame,text="Threshold")
		self.labelThreshold.grid(row=0,column=0)

		scale = tk.Scale(forScaleFrame, variable = self.varScale,from_ = 0, to = 1.0, resolution= 0.01)
		scale.grid(row=1,column=0)

		buttonScale = tk.Button(forScaleFrame, text="Select",command = lambda : self.featureSelected(listBoxFeatureSelected))
		buttonScale.grid(row=2,column=0)

		self.labelTest = tk.Label(forScaleFrame)
		self.labelTest.grid(row=3,column=0)



		# checkButtonFeatureSelection = tk.Checkbutton(selectRoleFrame, text= "Feature Selection",variable = self.featureSelection)
		# checkButtonFeatureSelection.grid(row=0,column=0,sticky="w")
		# checkButtonFeatureSelection.configure(state=tk.DISABLED)
		
		# buttonSelectFile = tk.Button(selectRoleFrame,text="browse...",command=lambda : self.contoh())
		# buttonSelectFile.grid(row=1,column=0,sticky="w")
	def resize(self,canvasScroll):
		canvasScroll.configure(scrollregion=canvasScroll.bbox("all"),width=235,height=200)	


	def readingCsv(self,fname):
		readCsv = pd.read_csv(fname)
		return readCsv

	def load_file(self,textSelectFile,frameCheckBox):
		for child in frameCheckBox.winfo_children():
			child.destroy()
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


		# scrollbar = tk.Scrollbar(selectRoleFrame, orient="vertical")
		# scrollbar.grid(row=0,column=1, sticky="ns")

		# textForScroll = tk.Text(selectRoleFrame,width =30,height = 5,yscrollcommand = scrollbar.set)
		# textForScroll.grid(row=0,column=0,sticky="nesw")

		# scrollbar.config(command=textForScroll.yview)				
		# readColumn = self.readColumn(getColumn)

	def contoh(self):
		getColumn = self.getColumn
		print(getColumn)

	def getColumnFromCsv(self,readCsv):
		numeric_variables = list(readCsv.dtypes[readCsv.dtypes != "object"].index)
		return numeric_variables

	def var_states(self):
		alabel = tk.Label(self,text="%s" % self.featureSelection.get())
		alabel.grid(row=3,column=0)
		print("tes : %d" %(self.featureSelection.get()))	

	def makeData(self,read,getColumn):
		dataX = read[getColumn]
		return dataX

	def dropAttribute(self):
		getColumn = self.getColumn
		for key,var in enumerate(self.variables):
			if var.get() > 0:
				getCol=getColumn[key]
				self.dataX=self.dataX.drop(getCol,axis = 1)
		self.dataY = self.read[getCol]
		print(self.dataY)
		print(getCol)
		return self.dataX

	def feature_importance(self,listBoxFeature,checkButtonFeatureSelection):
		fmt = '{:<8}{:<20}{}'
		self.clf = RandomForestClassifier(n_estimators=25,random_state=42,n_jobs=-1)
		model = self.clf.fit(self.dataX,self.dataY)
		for featureImportance in zip(self.getColumn, self.clf.feature_importances_):
			self.featureImportance.append((featureImportance))
		featureT = self.featureText(listBoxFeature,checkButtonFeatureSelection)
		return self.featureImportance 

	def featureText(self,listBoxFeature,checkButtonFeatureSelection):
		listBoxFeature.configure(state=tk.NORMAL)
		listBoxFeature.delete(0,tk.END)
		if self.featureSelection.get() > 0:
			for i,feature in enumerate(self.featureImportance):
				listBoxFeature.insert(i,feature)
		listBoxFeature.configure(state=tk.DISABLED)

	def featureSelected(self,listBoxFeatureSelected):
		sfm = SelectFromModel(self.clf, threshold = self.varScale.get())
		sfm.fit(self.dataX,self.dataY)

		for feature_list_index in sfm.get_support(indices=True):
			self.featureFix.append(self.getColumn[feature_list_index])
			print(self.getColumn[feature_list_index])

		listBoxFeatureSelected.configure(state =tk.NORMAL)
		listBoxFeatureSelected.delete(0, tk.END)
		for feature in self.featureFix:
			listBoxFeatureSelected.insert(0,feature)
		listBoxFeatureSelected.configure(state=tk.DISABLED)
		self.X_importantTrain = self.transformIntoSameColumn(sfm,self.dataX)
		self.X_importantTest = self.transformIntoSameColumn(sfm,self.dataXTest)
		return sfm

	def transformIntoSameColumn(self,sfm,data):
		X_important = sfm.transform(data)
		return X_important

		# selection = "Value" + str(self.varScale.get())
		# self.labelTest.config(text = selection)

	# def createMainPageTab(self,nb):
	# 	page1 = ttk.Frame(nb)
	# 	nb.add(page1,text="MainPageing")
	# 	selectFileFrame = tk.LabelFrame(page1, text = "Select")
	#   selectFileFrame.grid(row=0,column=0,sticky="NES",padx=5, pady=5, ipadx=2, ipady=5,rowspan=6)

	#   text = tk.Label(page1,text="when the the snows fall")
	#   text.grid(row=1,column=0,sticky="w")

	#   buttonKlasifikasi = tk.Button(page1,text="Klasifikasi")
	#   buttonKlasifikasi.grid(row=5,column=5,sticky="new",pady=2)

	#   button1 = tk.Button(page1,text="Back",command=lambda: controller.show_frame(start.StartPage))
	#   button1.grid(row=10,column=0,sticky="w")


	
