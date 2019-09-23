'''

driveSorter.py

A small lil script to sort your google drive if you are using google drive sync.

Just place this .py into your drive, configure the folderList in the script, and run the script every time you want to organize your drive folder.


'''

import os
import getpass #used for getting username

#folderList - a list of 2-tuples. the first element in the tuple is the path to the given folder.
#the second element is a list of strings. these strings are the file extensions you want to be moved to the respective folder
folderList = [
    ("\\Documents + Powerpoints", ['.gdoc','.pdf','.gmap','.gslides'] ),
    ("\\Spreadsheets", ['.gsheet'] ),
    ("\\Pictures", ['.png','.jpg'] ),
    ("\\_iPhone Recordings", ['.m4a'] )
    ]

driveDirectory = "C:\\Users\\" + getpass.getuser() + "\\Google Drive"

def main():
    #go through each item in drive directory (includes both folders and files)
    for item in os.listdir(driveDirectory):

        #go through every tuple in the folderList and compare the item's extension to the folderTuple's extensions
        for folder in folderList:

            for extension in folder[1]: #ew, nested for loops.

                if item.lower().endswith(extension): #if the extensions match
                    print(" -moving \"" + driveDirectory + "\\" + item + "\" to \"" + driveDirectory + folder[0] + "\\" + item + "\"") 
                    try:
                        os.rename(driveDirectory + "\\" + item, driveDirectory + folder[0] + "\\" + item)
                    except:
                        print(" -\"" + item + "\" is already in directory. skipping...")

    print("driveSorting complete.")

main()