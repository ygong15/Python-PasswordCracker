'''
Created on Jul 22, 2022

@author: ag0115
'''
#There are three necessary libraries for the script:
# 1. hashlib -> to hash the randomly generated phrase
# 2. random -> to randomly select multiple chars from the word set
# 3. timeit -> instantiate a timer object to calculate how long it takes to crack a password
import hashlib
import random
from timeit import default_timer as timer


#file reading function: read in all hashes from the txt file and store them in a array
def addToList(fileName):
    passList = []
    with open(fileName) as f:
        for line in f:
            #put each line of hashes in the file into the array and strip the "\n" at the end of each line
            passList.append(line.rstrip('\n'))
    f.close()
    #return passList which is filled with hashes
    return passList

#main function for generate random phrases and hashe them, meanwhile checking if they match hashes in the array
def bruteforce (passLength, passList):
    #delimiter to determine when to break from the while loop, default to False
    found = False
    #start timer before generating random phrases
    start = timer()
    while not found:
        #generate a random password according to the passed in lenght and turn it into a hashed one
        guess = ''.join(random.choices(wordSet, k = passLength))
        hashGuess = hashlib.md5(guess.encode()).hexdigest()


        #checking if the guessed password matches, if so print the password (txt form) and the time it takes
        #since the hashes are organized based on its lengthes (1 word, 2 word...), thus we can locate the
        #correct hash by relying on its length to get its position in the array
        if hashGuess == passList[passLength-1]: #if the generated hashes == the hash in the array spot -> we found the password
            #end timer
            end = timer()
            #print result
            print('\nPassword Found: ' + guess + '\tTime it takes: ' + str((end - start)) + ' seconds')
            #change the delimiter to True
            found = True

#wordSet contains all upper and lower cases letters, numbers, and special characters
wordSet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()?<>;:-_=+"
passList = addToList('Hashes.txt')
#the bruteForce function will only crack one hash at a time, thus we use a for loop to traverse the passList array
for i in range(0,len(passList)):
    bruteforce(i+1, passList)
