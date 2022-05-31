print("Welcome to myAnagram. It stricly uses only GB English.\nIf you do not use words found in the Englsih dictionary you would have to run the program from the start.\nHave fun and Good luck!")

import enchant
d = enchant.Dict("en_GB")
str1 = str(input("Enter your first word \n"))
if d.check(str1) == True:
    print("Your first word is an English word")
    str2 = str(input("Enter a second word \n"))
    if d.check(str2) == True:
        print("Your second word is also an English word")
        lenstr1 = len(str1)
        lenstr2 = len(str2)
        if (lenstr1) == (lenstr2):
            if sorted(str1) == sorted(str2):
                print(True)
                print("Congratulations your two words are anangrams")
            else:
                print(False)
                print("Sorry try again, these are not anagrams")
        else:
            print("Sorry try again these are not anagrams")
    else:
        print("This is not an English word")
else:
    print("This is not an Enlish word")
