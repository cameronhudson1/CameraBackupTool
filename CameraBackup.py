import shutil
import os
import datetime

settingsPath =
deleteOriginals = False;


# Moves a single file to a new directory
# Ignores files that already exist
def moveFile(sourceDir, destinationDir, file):
    files = os.listdir(destinationDir)
    if file in files:
        source = sourceDir + "\\" + file
        os.rename(source, source + " COPY")
        moveFile(source, destinationDir, file + " COPY")
    else:
        source = sourceDir + "\\" + file
        shutil.move(source, destinationDir)


def copyFile(sourceDir, destinationDir, file):
    files = os.listdir(destinationDir)
    if file in files:
        source = sourceDir + "\\" + file
        os.rename(source, source + " COPY")
        copyFile(source, destinationDir, file + " COPY")
    else:
        source = sourceDir + "\\" + file
        shutil.move(source, destinationDir)


# Moves a directory to a defined destination directory
def moveDirectoryWithDest(source, destination):
    files = os.listdir(source)
    for file in files:
        moveFile(source, destination, file)


def generateDirectoryName(root):
    currDate = datetime.date.today().strftime("%Y_%m_%d")
    return root + "\\Backup_" + currDate


# Moves a directory to a new destination directory in a root directory
def moveDirectory(source, destination):
    files = os.listdir(source)
    if destination[9:] in files:
        moveDirectoryWithDest(source, destination)
    else:
        os.makedirs(destination)
        moveDirectoryWithDest(source, destination)

def clearDirectory(source):
    files = os.listdir(source)
    for file in files:
        os.remove(file)

def handleBackup():
    source = "E:\\DCIM\\100D3400"
    rootDeposit = "C:\\Users\\cmrnh\\Pictures\\CameraBackup"
    print(rootDeposit)
    directories = os.listdir(rootDeposit)
    newDirectory = generateDirectoryName(rootDeposit)

    # Move fFiles
    if(newDirectory in directories):
        moveDirectoryWithDest(source, newDirectory)
    else:
        moveDirectory(source, newDirectory)

    # Delete Originals
    if(deleteOriginals):
        os.remove(source)

handleBackup