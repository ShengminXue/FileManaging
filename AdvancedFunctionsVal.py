import time
def lowput(prompt):
    answer = input(prompt)
    answer = answer.lower()
    return(answer)

def returnIndex():
    indexList = []
    file = "index.txt"

    try:
        f = open(file)
        for line in f.readlines():
            line = line.rstrip()
            indexList.append(line)

        f.close()
        return(indexList)

    except:
        print("Error in returnIndex")

def txtIndex(input):
    return("index/" + input + '.txt')

def PrintReturn(returnedLines):
    lines = returnedLines.split("\n")
    for line in lines:
        print(line)
        time.sleep(.2)
