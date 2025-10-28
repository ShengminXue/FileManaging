import random
import time
import json
from AdvancedFunctionsVal import *

def SearchFile(filename):
    #getting index into list to allow better use
    index = returnIndex()
    found = False
    for item in index:
        if filename == item:
            found = True
            name = item.capitalize()

            #Opening items
            f = open(txtIndex(item))
            fullText = ""
            text = f.readlines()
            for line in text:
                fullText += line

            fAbstract = open(txtIndex(item + "_abstract"))
            abstract = fAbstract.readline()

            fYear = open(txtIndex(item + '_year'))
            fYear = fYear.readline()
            fMonth = open(txtIndex(item + '_month'))
            fMonth = fMonth.readline()
            fDay = open(txtIndex(item + '_day'))
            fDay = fDay.readline()

            #Printing and 格式化
            print(name + ":")

            if fMonth == "Nul":
                monthDay = ""
            else:
                month = fMonth
                if fDay == "Nul":
                    monthDay = ""
                else:
                    monthDay = month + " " + fDay
            if fYear == "Nul":
                date = monthDay
            elif monthDay != "":
                date = monthDay + ', ' + fYear
            else:
                date = fYear

            if abstract == 'Nul':
                abstract = 'none'
                
            return("Date: " + date + "\nAbstract:\n" + abstract.capitalize() + "\nFull text:\n" + fullText.capitalize())


    if found == False:
        return("NUL")

