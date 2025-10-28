import random
import time
import json
from CreateFile import CreateFile
from AdvancedFunctionsVal import *
from SearchFile import SearchFile
from SearchFileKey import SearchFileKey as SearchSimilarity
from DeleteFile import DeleteFile
from EditFile import EditFiles
daysOfTheWeek = ['Monday', "Tuesday", "Wensday", "Thursday", "Friday", "Saturday", "Sunday"]
abbreviatedMonths = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov' , 'dec']




inSchool = True

#crockpot understanding mechanism
def CrockpotUnderstandingMechanism(theRequest):
    currentHour = int(time.strftime("%H"))
    currentDay = time.strftime("%A")
    i = 0
    for day in daysOfTheWeek:
        i += 1
        if day == currentDay:
            currentDayNum = i
    #Starting variables bc reasons
    #在下面填入你的名字
    name = ""
    if currentHour < 5:
        timeBasedAnswer = "Why are you calling me up at midnight?\nThis better be for a good reason"
    elif currentHour < 11:
        timeBasedAnswer = "Good Morning, " + name
    elif currentHour < 18:
        timeBasedAnswer = "Good Afternoon"
    elif currentHour < 22:
        timeBasedAnswer = "Good Evening,\n" + name
    else:
        timeBasedAnswer = "Why are you calling me up in the middle of the night?\nThis better be for a good reason"

#Lists
    createFiles = ['file', 'document', 'event', 'new', 'item', 'thing', 'create' ]
    searchFiles = ['file', 'document', 'event', 'item', 'thing', 'deadline', 'search', 'look up', 'find', 'open']
    searchCalendar = ['calendar', 'date', 'search', 'look up', 'find', 'open']
    deleteFiles = ['file', 'document', 'event', 'item', 'thing', 'deadline', 'delete', 'remove', 'cancel']
    editFiles = ['file', 'document', 'event', 'item', 'thing', 'deadline', 'edit', 'change', 'alter', 'adjust', 'make adjustments']
    createCalendar = ['calendar', 'date', 'new', 'create', 'calendar event']
    possibleGreetings = ['hello', 'hi', 'greetings', 'howdy', 'good morning', 'good afternoon', 'good evening']
    valerieNormalGreetings = ["Hi", "Hello", "Hello " + name, "Hi " + name, timeBasedAnswer]

    
#Variables
    createFilesProbability = 0
    searchFilesProbability = 0
    searchCalendarProbability = 0
    deleteFilesProbability = 0
    editFileProbability = 0
    createCalendarProbability = 0

    
    


    #testing for probability
    outOfOrder = False
    for key in possibleGreetings:
        if key in theRequest:
            if key == 'good morning':
                if currentHour > 12 or currentHour < 4:
                    outOfOrder = True
            elif key == 'good afternoon':
                if currentHour <12 or currentHour > 17:
                    outOfOrder = True
            elif key == 'good evening':
                if currentHour < 18 or currentHour > 22:
                    outOfOrder = True
            isGreeting = True
            break
        else: 
            isGreeting = False

    for fileKey in createFiles:

        createFilesProbability += theRequest.count(fileKey)

    for searchFileKey in searchFiles:

        searchFilesProbability += theRequest.count(searchFileKey)

    for searchCalendarKey in searchCalendar:
        searchCalendarProbability += theRequest.count(searchCalendarKey)
    
    for editFilesKey in editFiles:
        editFileProbability += theRequest.count(editFilesKey)
    
    for deleteFilesKey in deleteFiles:
        deleteFilesProbability += theRequest.count(deleteFilesKey)
    
    for createCalendarKey in createCalendar:
        createCalendarProbability += theRequest.count(createCalendarKey)


    #sorting for most probable
    probabilities = {
        "Create File": createFilesProbability,
        "Search File": searchFilesProbability,
        "Search Calendar": searchCalendarProbability,
        'Edit File': editFileProbability,
        "Delete File": deleteFilesProbability,
        'Create Calendar': createCalendarProbability
    }

    #getting probabilty and executing cmds
    sortProbabilities = sorted(probabilities.items(), key = lambda x:x[1], reverse = True)
    sortedProbabilities = dict(sortProbabilities)
    
    mostProbable = list(sortedProbabilities.keys())[0]

    
        

    #request
    if True:
        if isGreeting == True:
        #Add Variations later
        #print("Hello")
            #if inSchool == True:
 #               pass
#
            #else:
                greetingChoice = random.randint(0, len(valerieNormalGreetings) - 1)
                print(valerieNormalGreetings[greetingChoice])
                if outOfOrder == True:
                    time.sleep(.2)
                    print("Wait, am I missing somthing?")
    


        elif mostProbable == "Create File" and createFilesProbability > 0:
            CreateFile()
        elif mostProbable == "Search File":
            print('Enter file name')
            searchFileName = lowput('>>> ')
            
            answer = SearchFile(searchFileName)
            if answer == "NUL":
                print("Sorry, the file with the this specific name cannot be found.")
                time.sleep(.2)
                PrintReturn(SearchSimilarity(searchFileName))
            else:
                PrintReturn(answer)

        elif mostProbable == 'Create Calendar':
            print('When does this happen')
        elif mostProbable == "Search Calendar":
            print("What date do you want to search?")
        elif mostProbable == "Edit File":
            print("What file do you want to edit?")
            editFileName = lowput('>>> ')
            PrintReturn(EditFiles(editFileName))
        elif mostProbable == "Delete File":
            print("What file do you want to delete?")
            deleteFileName = lowput('>>> ')
            PrintReturn(DeleteFile(deleteFileName))
        else:
            print("I really do not understand what you are talking about.")
            time.sleep(.2)
            print("Please rephrase it.")



