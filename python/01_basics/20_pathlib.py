from pathlib import Path
#Path is class

path = Path("ecommerce18")
print(path.exists())#check if path exists. bool type
if not path.exists():
    path.mkdir()#makes dirrectory. doesn't retirn any value. .rmdir to remove.

path = Path()#path is equal local dirretory
for files in path.glob('*.*'):#search for files and dirs in current path
    print(files)#and print them


######################################
#pip install openpyxl
#package for working with excel (files?)


