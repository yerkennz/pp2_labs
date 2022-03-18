import os
print("Test a path exists or not:")
path = 'C:/Users/Nursultan/Desktop/raduga/'
print(os.path.exists(path))
path = 'C:/Users/Nursultan/Desktop/raduga/'
print(os.path.exists(path))
print("File name of the path:")
print(os.path.basename(path))
print("Dir name of the path:")
print(os.path.dirname(path))