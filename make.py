#!/usr/bin/python3

import sys,os
import glob
import subprocess

extension=".cpp"
snippet="snippet.cpp"
input_file = "input.txt"
output_file = "output.txt"


def createfile(dirname,file):
	with open(dirname+"/"+file,"w+") as f:
		if os.path.exists(snippet):
			f.write(open(snippet,"r").read())


def io_files():
	if os.path.exists(input_file):
		os.popen("/mnt/c/Program\ Files/Sublime\ Text\ 3/subl.exe "+input_file)
	if os.path.exists(output_file):
		os.popen("/mnt/c/Program\ Files/Sublime\ Text\ 3/subl.exe "+output_file)



# To open the files one by one in the samw window by using these options.
def runFiles(listOfFiles):
	listOfFiles.reverse()
	for i in listOfFiles:
		os.popen("/mnt/c/Program\ Files/Sublime\ Text\ 3/subl.exe "+i)


# To open the directory at once
def runDirectory(dirname):
	os.popen("/mnt/c/Program\ Files/Sublime\ Text\ 3/subl.exe "+ dirname)



def main():

	# Check the args
	if len(sys.argv) != 3:
		print("Usage Format : " + sys.argv[0] + " " + "{Contest-Name}" + " {Problem-Counts}")
		exit()

	# Check if the directory exist already with the same name

	dirname = str(sys.argv[1])
	if os.path.exists(dirname):
		print("File or Directory with the name '{}' already exists".format(dirname))
		return 
	os.mkdir(dirname)

	# Create files in the directory

	numberOfFiles=int(sys.argv[2])
	files=[chr(96+i)+extension for i in range(1,numberOfFiles)]
	for i in files:
		createfile(dirname,i)


	# Open directory in one instance
	runDirectory(dirname)
	io_files()
	
	# Open files one by one or open the new directory
	listOfFiles=glob.glob(dirname+"/*.cpp")
	runFiles(listOfFiles)

	


if __name__ == "__main__":
	main()
