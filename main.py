import os

def scanfolder(FileDirectory):
    fnn = 1
    for i in os.listdir(FileDirectory):
        if i.isnumeric() == False:
            fn = str(fnn)
            nn = fn+".txt"
            os.rename(FileDirectory+f"{i}",FileDirectory+f"{nn}")
            fnn += 1
# scanfolder("demo_folder/")