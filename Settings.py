from CrockpotUnderstanding import CrockpotUnderstandingMechanism

import time
settingTitles = {
    'Use of technology in school': 'schoolConcern.txt'
    
}

settingsExtract = {
    'Use of technology in school': 'Reminds you "Why are you using this in school?"'
}

def Settings():
    for name in settingTitles:
         with open(settingTitles[name]) as f_obj:
            contents = f_obj.readline()
            print("1 " + name + ": " + contents)

    request = input('\nDo you want to check details (enter "1") or change a specific setting (enter "2")? \nEnter "q" to quit settings.\n>>> ')

    #Getting extract
    if request == '1':
        for name in settingsExtract:
            extract = settingsExtract[name]
            print(name + ": " + extract)
        time.sleep(.2)
        print("... ")
        time.sleep(.2)
        Settings()

    #Change true/false  
    elif request == '2':
        settingNum = len(settingTitles)
        print("Which setting do you want to change? Enter serial number.")
        serialRequest = input(">>> ")

        try:
            requestNum = int(serialRequest) - 1
        except ValueError:
                print("That is not a valid serial number!")
                print("Please Try again")
                time.sleep(.2)
                Settings()

        else:
            if requestNum > settingNum or requestNum < 0:
                print("That is not a valid serial number!")
                print("Please Try again")
                time.sleep(.2)
                Settings()
            else :
                i = 0
                for name, setting in settingTitles.items():
                    if i == requestNum:
                        fileObject = open(settingTitles[name])
                        contentsFile = fileObject.readline()
                        f = open(settingTitles[name], "w")
                        if contentsFile == "True":
                            f.writelines("False")
                            time.sleep(.2)
                            print(name + ' is now set to "False"')   
                            f.close()
                        else:
                            f.writelines("True")
                            time.sleep(.2)
                            print(name + ' is now set to "True"') 
                            f.close()
                        time.sleep(.2) 
                        Settings()
                            
                    i += 1                      
    elif request == "q":
        print("Exited settings")
        return("")
    elif request == "/settings":
        print('You are already in settings')
    else:
        print("Excuse me?")
        print("Is this outside of settings?")
        print("...")
        CrockpotUnderstandingMechanism(request)    
