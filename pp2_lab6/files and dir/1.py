import os
path = 'C:/Users/Nursultan/Desktop/raduga/'

print("The only directories:")
print([x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))])
print("The only files:")
print([x for x in os.listdir(path) if not os.path.isdir(os.path.join(path, x))])
print("All directories and files:")
print([x for x in os.listdir(path)])