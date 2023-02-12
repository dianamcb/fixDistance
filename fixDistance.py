# Author: Diana Marlén Castañeda Bagatella
# Description: Prepare all the files to make a manual scan automatically for evry structure that is inside the folder were tou are ejecuting the code. Per structure create the number of structures that you ask between the distances that you need. The distance is between 2 atoms. This code is made to work with big structures.

from re import sub, search
from os import system, listdir, mkdir
from os.path import isdir

nCopies = 10
lowerDistance = 1.80
upperDistance = 2.20

unitDist = abs(upperDistance-lowerDistance)/nCopies
for comFile in listdir('./'):
    if not comFile.endswith('.com'): continue
    comDir = comFile[:-4]
    if isdir(f'{comDir}/'): system(f'rm -r {comDir}/')
    mkdir(comDir)
    with open(comFile,'r') as file: fileLines = file.readlines()
    for i in range(len(fileLines)-1,0,-1):
        if search('(B( \d+){2} F)',fileLines[i]):
            for j in range(int(nCopies)):
                dist = lowerDistance+unitDist*j
                txtDist = sub('\.','',f'{dist:.2f}')
                fileLines[i] = sub('(B( \d+){2})( \d+\.\d+)? F.*',r'\1 '+f'{dist:.2f} F',fileLines[i])
                fileContent = ''.join(fileLines)
                with open(f'{comDir}/{comFile[:-4]}-{txtDist}.com','w') as fileToWrite:
                    fileToWrite.write(fileContent)
            break

