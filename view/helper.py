from main import *

class Helper(object):
	"""docstring parent,*args,*kwargs Helper"""
	def __init__(self, parent,*args,*kwargs):
		self.dataX = main.dataX
		self.sfm = main.sfm

		print(self.dataX)