import os
filePath = 'C:/Users/Nursultan/Desktop/raduga/1/'
if os.path.exists(filePath):
    os.remove(filePath)
else:
    print("Can not delete the file as it doesn't exists")