import random
import time
import json
from AdvancedFunctionsVal import *
from math import ceil

def SearchFileKey(file):
    fileKeys = file.split()
    fileKeysDic = {}
    fileKeysDicList = []
    totalWordCount = 0
    for key in fileKeys:
        if key not in fileKeysDicList:
            fileKeysDicList.append(key)
            fileKeysDic[key] = 1
        else:
            fileKeysDic[key] += 1
        totalWordCount += 1



        #Getting similarity
    index = returnIndex()
    probabilityIndex = {}
    sixtySimilarity = []
    eightySimilarity = {}
    viableFiles = []

    for item in index:
        probabilityIndex[item] = 0
        for keyWord in fileKeysDicList:
            probability = item.count(keyWord)
            if probability > fileKeysDic[keyWord]:
                probability = fileKeysDic[keyWord]
            probabilityIndex[item] += probability
        if probabilityIndex[item] > 0:
            viableFiles.append(item)

 
    if viableFiles != []:

    
    
        #Conversion of similarity and takes out all that has 60% or more similarity and 80% or more similarity
        eightyAcceptance = 0.8 * totalWordCount
        eightyAcceptance = ceil(eightyAcceptance)
        probabilityIndexSixty = probabilityIndex.copy()
        for item in probabilityIndex:

            if probabilityIndex[item] >= eightyAcceptance:

                abstractFile = open(txtIndex(item + "_abstract"))

                abstract = abstractFile.readlines()
                if abstract[0] == "Nul":
                    abstract[0] = 'None'

                eightySimilarity[item] = abstract[0]
                del probabilityIndexSixty[item]

                abstractFile.close()



            


        sixtyAcceptance = 0.6*totalWordCount
        sixtyAcceptance = ceil(sixtyAcceptance)

        for item in probabilityIndexSixty:
            if probabilityIndexSixty[item] >= sixtyAcceptance:
                sixtySimilarity.append(item)
            
    
        returnItem = 'The following have a really high similarity:'
        for item in eightySimilarity:
            returnItemInc = '\n' + item.capitalize() + "\nAbstract: " + eightySimilarity[item].capitalize()

            returnItem += returnItemInc

        
        
        if sixtySimilarity != []:
            returnItem += "\nThe following have a high similarity:"
            for item in sixtySimilarity:
                returnItemInc = '\n' + item.capitalize()
                returnItem += returnItemInc


        return(returnItem)
    else:
        return('Sorry, but there are no items that are similar')
    


    

    

