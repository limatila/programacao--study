import numpy as np
#! In VsCode, USE THIS FOLDER AS THE ROOT FOLDER

#np.loadtxt
#or np.genfromtxt for more customization

dataset1 = np.genfromtxt( "spambase.csv", delimiter=',') 
#needs to specify delimiter between data in the '.csv' or '.txt'. Specifying dType is a convention.
# can use 'usecols=np.arange(0,x)' where x is the max number of columns, to specify how many columns the dataSet needs to have

dataset1 = np.delete(dataset1, -1, axis=0) #deleting the last row...

print(dataset1.shape) # data imported.
print(dataset1[-1, 0]) #? first of the second to last row.