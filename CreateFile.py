import time
import random
from operator import mod
import json
from AdvancedFunctionsVal import *
from SearchFile import SearchFile
months = ['jan',
'feb',
'mar',
'apr',
'may',
'jun',
'jul',
'aug',
'sep',
'oct',
'nov',
'dec']
thirtyDays = ['apr',
'jun',
'sep',
'nov']
thirtyOneDays = ['jan',
'mar',
'may',
'jul',
'aug',
'oct',
'dec']




def CreateFile():
    filename = lowput("What do you want to call this file as? \n>>> ")
    directory = "index/" + filename
    try:
        file = open(directory + '.txt', "x")
        index = open('index.txt', "a")
        index.write('\n' + filename)
        index.close()



#Date
        while True:
            error = False
            print('Is there a specific date? (Y/N/Today)')
            answer = lowput('>>> ')
            error = False
            if answer == 'y':
                print('Ok')

                #Infinite loop until a valid answer breaks out from the year category
                while True:
                    print('Is there a specific year that this happened/happens? (Enter number, enter "n" if none)')
                    answer = lowput('>>> ')
                    if answer != "n":
                        try:
                            year = int(answer)
                            break

                        except:
                            print('ERROR: Not an integer')
                    elif answer == "n":
                        print("Ok")
                        year = ("Nul")
                        break

                

                #Infinite loop until a valid answer breaks out from the month category
                
                while True:
                    
                    print('Is there a specific month? (Enter number, enter "n" if none)')
                    answer = lowput('>>> ')
                    if answer != 'n':
                        try:
                            #Checking for valid month
                            month = int(answer)
                            if month > 12:
                                print('ERROR: Larger than 12')
                            elif month < 1:
                                print('ERROR: Smaller than 1')
                            else:
                                month = months[month - 1]
                                print("Got it, it's on " + str(month.capitalize()))

                                

                

                #Infinite loop until a valid answer breaks out of the days category


                            while True:
                                
                                print('Is there a specific day? (Enter number, enter "n" if none)')
                                answer = lowput(">>> ")
                                if answer != 'n':
                                    try:

                                        #checking for valid date
                                        day = int(answer)
                                        if day < 1:
                                            print('ERROR: Smaller than 1')

                                        #Checking for 30 days
                                        elif month in thirtyDays and day > 30:
                                            print('ERROR: Larger than 30')

                                        #Checking for 31 days
                                        elif month in thirtyOneDays and day > 31:
                                            print('ERROR: Larger than 31')
                            
                                        #Checking for febuary and leap years
                                        elif month == "feb":
                                            if mod(year, 4) != 0:
                                                leap = False
                                            else:
                                                leap = True
                                                if mod(year, 100) == 0:
                                                    leap = False
                                                    if mod(year, 400) == 0:
                                                        leap = True
                                            if leap == False:
                                                febDays = 28

                                            else:
                                                febDays = 29
                                            print(febDays)

                                            if day > febDays:
                                                print('ERROR: Larger than '+ str(febDays))
                                        else:
                                            print(str(day) + ", got it")
                                            break
                                            
                                    except ValueError:
                                        print("ERROR: Not an integer")
                                elif answer == 'n':
                                    day = 'Nul'
                                    print('Ok')
                            break

                        except ValueError:
                            print('ERROR: Not an integer')

                    elif answer == 'n':
                        print("Got it")
                        month = 'Nul'
                        day = "Nul"
                        break

                         

            elif answer == 'n':
                print('Alright')
                year = "Nul"
                month = "Nul"
                day = "Nul"
            elif answer == 'today':
                print('Got it')
                year = time.strftime("%Y")
                month = months[int(time.strftime("%m")) - 1]
                day = time.strftime("%d")
            else:
                error = True
            #To not write break every line
            if error != True:
                break
            else:
                print('ERROR: Meaningless string.')
        fileDay = open(directory + '_day.txt', 'x')    
        fileDay.write(str(day))   
        fileDay.close()
        fileMonth = open(directory + "_month.txt", 'x')
        fileMonth.write(str(month.capitalize()))
        fileMonth.close()
        fileYear = open(directory + "_year.txt", 'x')
        fileYear.write(str(year))
        fileYear.close()
            
        #Completed Date, start Abstract
        print(
            'Enter abstract (Enter nothing if none)'
        )
        abstract = lowput(">>> ")
        if abstract == "":
            abstract = "Nul"
        fileAbstract = open(directory + "_abstract.txt", 'x')
        fileAbstract.write(abstract)
        fileAbstract.close()
        

        print(
            'Enter full text:'
        )
        
        textList = []
        while True:
            textAppend = lowput(">>> ")
            textList.append(textAppend)
            textList.append('\n')
            if textAppend == '':
                if textList == ['','\n']:
                    print('Cannot have empty texts')
                    textList = []
                else:
                    textList.pop()
                    textList.pop()
                    textList.pop()
                    break
        

        text = ""
        for item in textList:
            text += item

        file.write(text)
        file.close()
        print("Completed")
            


    except FileExistsError:
        print("I found another file under this name.")
        print('Do you want to open it? (Y/N)')
        openFile = lowput(">>>")
        if openFile == "y":
            PrintReturn(SearchFile(filename))
        elif openFile == "n":
            print("Ok")
        else:
            print("I don't exactly understand.")
