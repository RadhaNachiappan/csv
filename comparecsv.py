import ConfigParser
import pandas as pd
import csv
class Csvfile:
	#edited by radha
	def config(self):
		self.config=ConfigParser.ConfigParser()
		self.location=raw_input("Enter The Location : ")
		self.config.read(self.location)
		self.c=self.config.sections()
		self.c=self.c
		self.result=[]
		print "came here", self.c
