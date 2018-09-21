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
		
	#getting options from the section	
    def ConfigSectionMap(self,section):
		self.dict1 = {}
		#self.config=ConfigParser.ConfigParser()
		self.options = self.config.options(section)
		print "self. options",self.options
		print "section",section
	    
		#converting option to dictionary
		
		for option in self.options:
			try:
				self.dict1[option] = self.config.get(section, option)
				if self.dict1[option] == -1:
					DebugPrint("skip: %s" % option)
			except:
				print("exception on %s!" % option)
				self.dict1[option] = None

		return self.dict1
	#Converting dictionary to dataframe	
	def Convertdf(self):
		file1 = {}
		for i in self.c:	

			file1=self.ConfigSectionMap(i)
			print file1
			file2=file1.keys()
			src_table=pd.read_csv(file1[file2[0]],sep=',')
			dest_table=pd.read_csv(file1[file2[1]],sep=',')
			
			df1= pd.DataFrame(data=src_table)
			df2= pd.DataFrame(data=dest_table)

			
			print df1
			print df2

	#Returns a tuple with number of rows and number of column
			tuple1=df1.shape
			tuple2=df2.shape

			#print tuple1
			#print tuple2
	#Compare number of 
			if((tuple1[0]==tuple2[0]) and (tuple1[1]==tuple2[1])):
				if(len(df1.columns.intersection(df2.columns))==tuple1[1]):
					"""
				#print df1.columns
				newlis=[]
				for i in range(len(df1.columns)):
					newlis.append(df1.columns[i])
				#print newlis
				final_df = pd.merge(df1, df2,  how='inner', on =newlis)
				print final_df
				if(final_df.shape==df1.shape):
					result.append("TRUE - Table matched")
				else:
					result.append("FALSE - Record missmatch")
					"""
					flag=0
					for k in range(len(df1.index)):
						for n in range(len(df1.index)):
							if(df1.iloc[k].equals(df2.iloc[n])==True):
								flag=flag+1
								break
						#print flag
					if(flag==len(df1.index)):
						self.result.append("TRUE")
					else:
						self.result.append("FALSE - Record mismatch")
				
				else:
					self.result.append("FALSE - Column mismatch")
			else:
				self.result.append("FALSE - Size mismatch")
				
			print self.result		
			