import sys
sys.path.append('D://Bahan Belajar/SKRIPSI COY/Skripsi_road_to_jan/AppClassifOrder/view')
sys.path.append('D://Bahan Belajar/SKRIPSI COY/Skripsi_road_to_jan/AppClassifOrder/model')
from main import MainPage
from classify import Classify

class ControllerClassify(MainPage): 
	def __init__(self,MainPage,controller):
		self.controller = controller
		m = MainPage()
		self.sfm = MainPage.sfm
		self.dataX = MainPage.dataX
		self.button = Classify.buttonStart
		self.button.bind("<Button-1>",transform)

	def transform(self):
		dataTransform = self.sfm.transform(self.dataX)
		print (dataTransform)
		return dataTransform

