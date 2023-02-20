# Author: Diana Marlén Castañeda Bagatella
# Description: Prepare all the files to make a manual scan automatically for evry structure that is inside the folder were tou are ejecuting the code. Per structure create the number of structures that you ask between the distances that you need. The distance is between 2 atoms. This code is made to work with big structures.

from re import sub, search
from os import system, listdir, mkdir
from os.path import isdir

nCopies = 10
lowerDistance = 1.80
upperDistance = 2.20
path = './'

unitDist = abs(upperDistance-lowerDistance)/nCopies
for comFile in listdir(path):
    if not comFile.endswith('.com'): continue
    comDir = comFile[:-4]
    if isdir(f'{path}{comDir}/'): system(f'rm -r {path}{comDir}/')
    mkdir(comDir)
    with open(path+comFile,'r') as file: fileLines = file.readlines()
    for i in range(len(fileLines)-1,0,-1):
        if search('(B( \d+){2} F)',fileLines[i]):
            ithLine = fileLines[i]
            for j in range(int(nCopies)):
                tmpFileLines = fileLines.copy()
                dist = lowerDistance+unitDist*j
                txtDist = f'{int(100*dist)}'
                tmpFileLines.insert(i, f'{ithLine[:-2]}{dist:.2f}\n')
                fileContent = ''.join(tmpFileLines)
                with open(f'{path}{comDir}/{comFile[:-4]}-{txtDist}.com','w') as fileToWrite:
                    fileToWrite.write(fileContent)
            break

