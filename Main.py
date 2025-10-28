import random
import time
import json
from CreateFile import CreateFile
from AdvancedFunctionsVal import *
from SearchFile import SearchFile
from SearchFileKey import SearchFileKey as SearchSimilarity
from Settings import Settings
from CrockpotUnderstanding import CrockpotUnderstandingMechanism


while True:
    
    request = lowput(">>> ")
    time.sleep(.2)
    #Why are you using this in school?
   # with open('schoolConcern.txt') as f_obj:
    #    contents = f_obj.readline()
     #   if contents == True:
      #      if currentHour > 7 and currentHour < 16 and currentDayNum  < 6:
       #         print("Shouldn't you be in school?")
        #        time.sleep(1)
         #       print("Nevermind\n")
          #      time.sleep(1)
           #     inSchool = True
            #else:
             #   inSchool = False

    #settings
    if request == "/settings":
        print("Openning settings...")
        time.sleep(.2)
        Settings()
    
    elif request == '/close':
        print('Good night, Mike')
        time.sleep(.2)
        break
        
    else:
        CrockpotUnderstandingMechanism(request)
