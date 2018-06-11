import sys
import os.path

if(len(sys.argv) < 3):
    print("Usage: provide an input file and output file as arguments to this program.")
    quit()

if(not(os.path.isfile(sys.argv[1]))):
    print("Could not locate input file (argument 1)")

#Open
# inFile = open("pyIn.txt", "r")
# outFile = open("pyOut.txt", "w+")
inFile = open(sys.argv[1], "r")
outFile = open(sys.argv[2], "w+")

#Read
fl = inFile.readlines()

#Sort
fl.sort()

#Write
for line in fl:
    outFile.write(line)

#Close
inFile.close()
outFile.close()

print("All sorted!")
