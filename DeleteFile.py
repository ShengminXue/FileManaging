from os import remove
from AdvancedFunctionsVal import *

def DeleteFile(filename):
    index = returnIndex()
    try:
        file = open(txtIndex(filename))
        file.close()

    except FileNotFoundError:
        return('This file does not exist. \nPerhaps it is already deleted.')

    #This here assumes that the file exists because or else it would've already returned an answer and therefore no longer continue

    for item in index:
        if item == filename:
            index.remove(filename)
    
    indexFile = open('index.txt', 'w')
    i = 1
    length = len(index)
    for item in index:
        indexFile.write(item)
        if i < length:
            indexFile.write('\n')
        i += 1
    indexFile.close()

    remove(txtIndex(filename))
    remove(txtIndex(filename + '_abstract'))
    remove(txtIndex(filename + '_day'))
    remove(txtIndex(filename + '_month'))
    remove(txtIndex(filename + '_year'))
    return('Completed')
