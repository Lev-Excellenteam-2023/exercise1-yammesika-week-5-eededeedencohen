#==================================
# הארי רציונלי אבל לא נורא - 5.4
#==================================

import os
import zipfile
import re 

POTTER_ZIP_PATH = os.getcwd() + "/resources/potter.zip"
POTTER_PATH = os.getcwd() + "/resources/potter" 


#----------------------------------------------------------
# get_chapter_number function:
# The function gets a number of file of a chapter in the potter series.
# Returns the real chapter number 
#----------------------------------------------------------
def get_chapter_number(fileNum):
    fileNum = str(fileNum) # convert to string
    with open(POTTER_PATH+"/"+fileNum+".html", "r", encoding="utf-8") as f:
        html = f.read()
    pattern = r"chapter-title\">[^\d]*([\d]*)"
    chapterNum = re.search(pattern, html).group(1)
    return chapterNum

#----------------------------------------------------------
# change File Name function:
# The function gets a string and a path to a file.
# The function changes the file name to the string.
#----------------------------------------------------------
def change_file_name(newName, filePath):
    os.rename(filePath, newName)


#----------------------------------------------------------
# chaneToRealChapterName function:
# The function gets a number of file of a chapter in the potter series.
# The function changes the file name to the real chapter number.
#----------------------------------------------------------
def changeToRealChapterName(fileNum):
    realChapterNumber = get_chapter_number(fileNum)
    path = POTTER_PATH + "/"+str(fileNum)+".html"
    change_file_name(newName=POTTER_PATH+"/_"+realChapterNumber+".html", filePath=path)


#----------------
# Main function
#----------------
def main():

    # unzip the resouce\potter.zip file to the current directory into a folder named potter
    with zipfile.ZipFile(POTTER_ZIP_PATH, 'r') as zip_ref:
        zip_ref.extractall(POTTER_PATH)

    # change all the files names to the real chapter number
    for i in range(1,123):
        changeToRealChapterName(i)

    # change all the files names from _i.html to i.html
    for i in range(1,123):
        change_file_name(newName=POTTER_PATH+"/"+str(i)+".html", filePath=POTTER_PATH+"/_"+str(i)+".html")

if __name__ == "__main__":
    main()