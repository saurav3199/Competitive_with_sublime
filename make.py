#!/usr/bin/python3

import sys,os
import glob
import subprocess

extension=".cpp"
snippet="snippet.cpp"


def createfile(dirname,file):
    with open(dirname+"/"+file,"w+") as f:
        if os.path.exists(snippet):
            f.write(open(snippet,"r").read())



def runFiles(listOfFiles):                      # Open all files of the directory
    listOfFiles.reverse()                       # To open your first files    
    for i in listOfFiles:
        os.popen("/mnt/c/Program\ Files/Sublime\ Text\ 3/subl.exe "+i)

# We can also open the directory in single command but
# that will not configure your layout settings 
# as it will open your folder in new window


def main():
    if len(sys.argv) != 2:
        print("Usage Format : " + "./" + sys.argv[0] + " " + "{Contest-Name}" + " {Problem-Counts}")
        exit()
    dirname = str(sys.argv[1])
    if os.path.exists(dirname):
        print("File or Directory with the name '{}' already exists".format(dirname))
        return 
    os.mkdir(dirname)
    numberOfFiles=int(sys.argv[2])
    files=[chr(96+i)+extension for i in range(1,numberOfFiles)]
    for i in files:
        createfile(dirname,i)
    listOfFiles=glob.glob(dirname+"/*.cpp")
    runFiles(listOfFiles)

if __name__ == "__main__":
    main()
