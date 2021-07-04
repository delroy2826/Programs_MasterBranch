import os
import shutil
path=os.chdir("D:\\Users\\deolivei\\Desktop\\FileRecognizer")
PATH = "D:\\Users\\deolivei\\Desktop\\FileRecognizer"
while True:
    lstOfFiles = os.listdir(path)
    if len(lstOfFiles)!=0:
        for FileName in lstOfFiles:
            extension = FileName.split(".")[-1]
            if extension == "xlsx":
                print("D:\\Users\\deolivei\\Desktop\\EXCEL")
                shutil.move(PATH+"\\"+FileName,"D:\\Users\\deolivei\\Desktop\\EXCEL")
            elif extension =="txt":
                print("D:\\Users\\deolivei\\Desktop\\TXT")
                shutil.move(PATH + "\\" + FileName, "D:\\Users\\deolivei\\Desktop\\TXT")
            elif extension=="pdf":
                print("D:\\Users\\deolivei\\Desktop\\PDF")
                shutil.move(PATH + "\\" + FileName, "D:\\Users\\deolivei\\Desktop\\PDF")
    else:
         print("File Directory Is Empty")
         break

