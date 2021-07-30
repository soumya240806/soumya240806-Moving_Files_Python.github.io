import os
import shutil

path=input("enter the name of the directory to be sorted")

list_files=os.listdir(path);

for  file in list_files:
    name,ext=os.splitext(file)

    ext=ext[1:]
    if ext=='':
        continue

if os.path.exists(path+'/'+ext):shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

    # This will create a new directory,
    # if the directory does not already exist
else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

        

