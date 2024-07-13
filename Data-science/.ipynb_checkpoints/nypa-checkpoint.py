import numpy as np 
import pandas as pd 


#create numpy array
data=np.array([[2,3,5],[0,2,4]])

#Create a datafram from Numpy array
df=pd.DataFrame(data, columns=["A","B","C"])
print(df)