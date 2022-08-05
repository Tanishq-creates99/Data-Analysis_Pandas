import pandas as pd
import numpy as np

myList = ([[0,1],
                   [2,3],
                   [4,5]])
mydataframe = pd.DataFrame(myList,columns=['even','odd'])
print(mydataframe)

myDictionary = {'Fruit': ['Apple','Banana','Orange'],
'Color':['Red','Yellow','Orange']}
myDataFrames = pd.DataFrame(myDictionary)
#print(myDataFrames)

#to readcsv file use 
#pd.read_csv(File Name.csv)

#-----------------------

#df = pd.read_csv(filename.csv)
#df.set_index('name of coloumn u wanna keep as head')

#------------------------

#df.set_index('name',inplace=True)

#-----------------------

#to get first 8 names  use 
#name of obj.head(8)

#to get last 8 names use 
#name of obj.tail(8)

#---------------------

#to get a quick statistical summary of columns use
#name of obj.describe()

#--------------------

#to slice row in any number use 
#nameofobj[1:9]

#---------------------

#to pick few specific rows use their names in []
#df[['name','rating']]

#---------------------

#Boolean list
#thirdrow[false ,false ,false ,true ,false]
#it will only pick 3rd row from the table since that is what we called true

#-----------------------

#FIltering rows with specific values 
#condition =  df['Calories' > 70]
#print(df)

#and it will pick the ones as per condn and show them

#---------------------
#we can also group the condition using &

#condition = df[  (df['calories' >70] )  &
#             (df['protein'] > 9 )   ]


#--------------------

#to index few values like bot rows and columns we use
#df.loc[1:9,'name','protein']

#and it will show that row and that column only

#---------------------


#Adding Deleting rows
#df. loc[6] = ['Trix', 110, 1, 25, 27.753301]

#df.drop (6, axis=0, inplace=True)

#-----------------------

#Adding deleting columns
#df['My Column'] = ['A', 'B', 'C', 'D', 'E']

#df.drop('My Column', axis=1, inplace =True)

#------------------------
#Sorting Values for ascending

#df.sort_values(by='calories')

#for descending
#df.sort_values(by ='calories' , ascending=False)
#----------------------

#To create new files 

#df.to_csv('Name.csv' , index_label =False)
