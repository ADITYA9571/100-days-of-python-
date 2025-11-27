#shutil modules
import shutil
import os
shutil.copy("mail.py","main2.py")#meta data are not saved
shutil.copy2("mail.py","main2.py")#exact data are saved 
shutil.copytree("mail.py","main2.py")#directory data are copied
shutil.move(".mailfile/mail.py","main2.py")#files are moved
shutil.rmtree("mytutorial")#use to delete the folder
os.remove("mytutorial.file")#use to delete the file using os module, not in shutil

