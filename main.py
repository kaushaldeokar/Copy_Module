# importing the modules
import os
import shutil

# Providing the folder path
origin = 'C:/Users/kaush/Desktop/Copy_Module/Input'
target = 'C:/Users/kaush/Desktop/Copy_Module/Output'

# Fetching the list of all the files
files = os.listdir(origin)
print(len(files))

# Fetching all the files to directory
for file_name in files:
   print(file_name)
   shutil.copy(os.path.join(origin, file_name), os.path.join(target, file_name))
print("Files are copied successfully")