# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

#Timing stuff
start_time = time.time()

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Calls main() to begin program
def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])

    #Check if they want to end program
    doNotLeave = True
    while doNotLeave:
        print(f'''
Main Menu
1: Spell Check a Word (Linear Search)
2: Spell Check a Word (Binary Search)
3: Spell Check Alice In Wonderland (Linear Search)
4: Spell Check Alice In Wonderland (Binary Search)
5: Exit
        ''')
        selection = int(input("Selection: "))
        #Linear Search Spell Check
        if selection == 1:
            word = input("Input a word:").lower()
            startTimer = time.time()
            position = linearSearch(dictionary, word)
            endTimer = time.time()
            searchTime = endTimer-startTimer
            print(f"{word} is {'found' if position != -1 else 'not found'} in the dictionary. Run Time : {searchTime}")
            
        #Binary Search Spell Check
        elif selection == 2:
            word = input("Input a word:").lower()
            startTimer = time.time()
            position = binarySearch(dictionary, word)
            endTimer = time.time()
            searchTime = endTimer-startTimer
            print(f"{word} is {'found' if position != -1 else 'not found'} in the dictionary. Run Time : {searchTime}")
            
        #Linear Search AIW
        elif selection == 3:
            notFound = 0
            startTimer = time.time()
            print('Spell Checking...')
            for word in aliceWords:
                if linearSearch(dictionary, word) == -1:
                    notFound += 1
            endTimer = time.time()
            searchTime = endTimer - startTimer
            print(f'How many word were not found in the dictionary: {notFound} ({searchTime} seconds)')
        # #Binary Search AIW
        elif selection == 4:
            notFound = 0
            startTimer = time.time()
            print('Spell Checking...')
            for word in aliceWords:
                if binarySearch(dictionary, word) == -1:
                    notFound += 1
            endTimer = time.time()
            searchTime = endTimer - startTimer
            print(f'How many word were not found in the dictionary: {notFound} ({searchTime} seconds)')
        # #Exit
        elif selection == 5:
            doNotLeave = False

#Linear Search
def linearSearch(listName, element):
    for i in range(len(listName)):
        if listName[i] == element:
            return i
    return -1

#Binary Search
def binarySearch(listName, element) :
    upperIndex = len(listName) - 1
    lowerIndex = 0
    while lowerIndex <= upperIndex:
        middleIndex = (upperIndex+lowerIndex) // 2
        if listName[middleIndex] == element:
            return middleIndex
        elif element < listName[middleIndex]:
            upperIndex = middleIndex - 1
        else:
            lowerIndex = middleIndex + 1
    return -1
#Call main 
main()