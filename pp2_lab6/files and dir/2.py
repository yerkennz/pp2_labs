import os

print('Exist:', os.access('C:/Users/Nursultan/Desktop/raduga/', os.F_OK))
print('Readable:', os.access('C:/Users/Nursultan/Desktop/raduga/', os.R_OK))
print('Writable:', os.access('C:/Users/Nursultan/Desktop/raduga/', os.W_OK))
print('Executable:', os.access('C:/Users/Nursultan/Desktop/raduga/', os.X_OK))