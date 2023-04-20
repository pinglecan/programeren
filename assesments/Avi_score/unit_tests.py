from functies import *

# test 1: getNumberOfCharacters
if getNumberOfCharacters('aap') == 3:
    print("Test geslaagd 1")
else:
    print("Deze test is niet geslaagd 1")

if getNumberOfCharacters('aap.') == 3:
    print("Test geslaagd 2")
else:
    print("Deze test is niet geslaagd 2")

if getNumberOfCharacters('i love big fat chicken') == 22:
    print("Test geslaagd 3")
else:
    print("Deze test is niet geslaagd 3")


# test 2: getNumberOfSentences
if getNumberOfSentences(getText('easy')) == 14:
    print("Test geslaagd 4")
else:
    print("Deze test is niet geslaagd")

if getNumberOfSentences(getText('data\john.txt')) == 3664: 
    print("Test geslaagd 5")
else:
    print("Deze test is niet geslaagd 5")


# test 3: getNumberOfWords
if getNumberOfWords(getText('data\difficult1.txt')) == 82:
    print("Test geslaagd 6")
else:
    print("Deze test is niet geslaagd 6")

if getNumberOfWords(getText('data\easy1.txt')) == 11:
    print("Test geslaagd 7")
else:
    print("Deze test is niet geslaagd 7")

if getNumberOfWords(getText('data\john.txt')) == 18841:
    print("Test geslaagd 8")
else:
    print("Deze test is niet geslaagd 8")
