import shutil
import os
import datetime


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


# Moves a directory to a defined destination directory
def moveDirectoryWithDest(source, destination):
    files = os.listdir(source)
    for file in files:
        moveFile(source, destination, file)


def generateDirectoryName():
    currDate = datetime.date.today().strftime("%Y_%m_%d")
    return "D:\Test1\Backup_" + currDate


# Moves a directory to a new destination directory in a hard-coded root directory
# TODO Make root directory Generic
def moveDirectory(source):
    files = os.listdir("D:\Test1")
    destination = generateDirectoryName()
    if destination[9:] in files:
        moveDirectoryWithDest(source, destination)
    else:
        os.makedirs(destination)
        moveDirectoryWithDest(source, destination)


root = "D:\Test1"
sourceName = "D:\Test1\Backup_2018_03_19"
moveDirectory(sourceName)
