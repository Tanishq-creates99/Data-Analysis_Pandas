import pandas as pd

myList = [['Apple', 'Red'],['banana','yellow'],['orange','Orange']]

#myDataframe = pd.DataFrame(myList)
myDataframe = pd.DataFrame(myList,columns=('Fruits','Color'))
print(myDataframe)