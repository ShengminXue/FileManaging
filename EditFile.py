from stat import filemode
from AdvancedFunctionsVal import *
from os import remove
from time import strftime
from operator import mod
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

def EditFiles(filename):
    try:
        file = open(txtIndex(filename))
        file.close

    except FileNotFoundError:
        return('Sorry, the requested file "' + filename + '" does not exist.')
    PrintReturn(SearchFile(filename))
    print('What do you want to edit? (enter "name"/"text"/"abstract"/"date")')
    print(
        'Enter "q" to exit.'
    )
    choice = lowput('>>> ')
    if choice == 'name':
        print(EditName(filename))
    elif choice == 'text':
        print(EditText(filename))
    elif choice == 'abstract':
        print(EditAbstract(filename))
    elif choice == 'date':
        print(EditDate(filename))
    elif choice == 'q':
        return('Ok')
    else:
        return('Sorry, that is not part of the choice')
    return('Completed')



def EditName(filename):
    #Get name
    print('What do you want to change the name of ' + filename + ' into?')
    while True:
        newName = lowput('>>> ')
        if newName == '':
            print('Name cannot be empty!')
        else:
            try:
                break
            except FileExistsError:
                f = open(txtIndex(filename))
                print('The file "' + newName + '" already exists')
                f.close()

    #Dealing with index part
    index = returnIndex()
    i = 0
    for item in index:
        if item == filename:
            index[i] = newName
        i += 1
    
    indexFile = open('index.txt', 'w')
    i = 1
    length = len(index)
    for item in index:
        indexFile.write(item)
        if i < length:
            indexFile.write('\n')
        i += 1
    indexFile.close()

    

    #Store data and delete files 
    fText = open(txtIndex(filename))
    text = fText.readlines()
    fText.close()
    remove(txtIndex(filename))

    fAbstract = open(txtIndex(filename + '_abstract'))
    abstract = fAbstract.readlines()
    fAbstract.close()
    remove(txtIndex(filename + '_abstract'))

    fDay = open(txtIndex(filename + '_day'))
    day = fDay.readlines()
    fDay.close()
    remove(txtIndex(filename + '_day'))

    fMonth = open(txtIndex(filename + '_month'))
    month = fMonth.readlines()
    fMonth.close()
    remove(txtIndex(filename + '_month'))

    fYear = open(txtIndex(filename + '_year'))
    year = fYear.readlines()
    fYear.close()
    remove(txtIndex(filename + '_year'))


    #Create new files
    newText = open(txtIndex(newName), 'x')
    newAbstract = open(txtIndex(newName + '_abstract'), 'x')
    newDay = open(txtIndex(newName + '_day'), 'x')
    newMonth = open(txtIndex(newName + '_month'),'x')
    newYear = open(txtIndex(newName + '_year'), 'x')

    #Replace files and migrate data

    for line in text:
        newText.write(line)
    newText.close()

    newAbstract.write(abstract[0])
    newAbstract.close()

    newDay.write(day[0])
    newDay.close()

    newMonth.write(month[0])
    newMonth.close()

    newYear.write(year[0])
    newYear.close()

    return('completed')


def EditText(filename):
    print('Enter full text')
    textFile = open(txtIndex(filename), 'w')
    textList = []

    while True:
        textAppend = lowput('>>> ')
        textList.append(textAppend)
        textList.append('\n')
        if textAppend == '':
            if textList == ['', '\n']:
                print('You cannot have empty texts')
                textList = []
            else:
                textList.pop()
                textList.pop()
                textList.pop()
                break

    text = ''
    for line in textList:
        text += line
    
    textFile.write(text)
    textFile.close()
    return('completed')


def EditAbstract(filename):
    abstractFile = open(txtIndex(filename + '_abstract'), 'w')
    print(
        'Enter abstract (Enter nothing if none)'
    )
    abstract = lowput('>>> ')
    if abstract == '':
        abstractFile.write('Nul')
    else:
        abstractFile.write(abstract)
    abstractFile.close()
    return('completed')


def EditDate(filename):
    #Note how this time i didn't all just just use "answer" this time
    #This is for less confusion
    #However might take a while to defer from the two codes
    while True:
        error = False
        print('Is there a specific date? (Y/N/Today)')
        date = lowput('>>> ')
        if date == 'n':
            
            year = 'Nul'
            month = 'Nul'
            day = 'Nul'
            print('Got it')
            break
        elif date == 'today':
            
            year = time.strftime("%Y")
            month = months[int(time.strftime("%m")) - 1]
            day = strftime('%d')
            print('Got it')
            break
        
        elif date == 'y':

            #Year loop is independent from the month/day loop
            while True:
                print('Is there a specific year that this happened/happens? (Enter number, enter "n" if none)')
                yearStr = lowput('>>> ')

                if yearStr == 'n':
                    print('Got it, no year')
                    year = 'Nul'
                    break
                else:
                    try:
                        year = int(yearStr)
                        print('Got it')
                        break
                    except ValueError:
                        print('Must be an integer!')

            #The real fun begins
            #The month/day loop depends on itself so that if the month doesnt exist you cant input day
            while True:
                print('Is there a specific month? (Enter number, enter "n" if none)')
                monthStr = lowput('>>> ')
                #This time i'll try getting the "n" Categories out of the way first
                if monthStr == 'n':
                    print('Got it, no month')
                    month = 'Nul'
                    year = 'Nul'

                else:
                    try:
                        month = int(monthStr)
                        if month > 12:
                            print('After December it is January')
                        elif month < 1:
                            print('Before January it is December')

                        else:
                            month = months[month - 1]
                            print("Got it, it's on " + str(month.capitalize()))

                            #And let the madness begin
                            #The following is the day category
                            while True:
                                print('Is there a specific day? (Enter number, enter "n" if none)')
                                dayStr = lowput('>>> ')
                                if dayStr == 'n':
                                    print('Got it')
                                    day = 'Nul'
                                
                                else:
                                    try:      
                                        #Start checking for valid date!
                                        day = int(dayStr)
                                        if day < 1:
                                            print("Can't be smaller than 1!")
                                        
                                        elif day > 30 and month in thirtyDays:
                                            print("Can't be larger than 30!")
                                        
                                        elif day > 31 and month in thirtyOneDays:
                                            print("Can't be larger than 31!")
                                        
                                        #Febuary and leap year 
                                        elif month == 'feb':
                                            if mod(year, 4) != 0:
                                                leap = False
                                            else:
                                                leap = True
                                                if mod(year, 100) == 0:
                                                    leap = False
                                                    if mod(year, 400) == 0:
                                                        leap = True

                                            if leap == True:
                                                febDays = 29
                                            else:
                                                febDays = 28

                                            if day > febDays:
                                                print("Can't be larger than " + str(febDays))

                                        else:
                                            print(str(day) + ', got it.')
                                            break

                                    except ValueError:
                                        print('Must be an integer!')
                            
                            break

                    except ValueError:
                        print("Must be an integer!")
        else:
            error = True
        if error != True:
            break
        else:
            print('Meaningless String!')
    
    #Start entering data
    dayFile = open(txtIndex(filename + '_day'), 'w')
    dayFile.write(str(day))
    monthFile = open(txtIndex(filename + '_month'), 'w')
    monthFile.write(month.capitalize())
    yearFile = open(txtIndex(filename + '_year'), 'w')
    yearFile.write(str(year))

    #Closing
    dayFile.close()
    monthFile.close()
    yearFile.close()

    return('Completed')


