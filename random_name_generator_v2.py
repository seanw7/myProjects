import random
import string

# This program creates a 9 digit string of user selected or randomized letters

vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letters = string.ascii_lowercase

# This function takes in 9 inputs which are turned into global variables
# they are then used by the generator function to create the random string sequence
def takeIn():
    global letter_in_1,letter_in_2,letter_in_3,letter_in_4,letter_in_5,letter_in_6,letter_in_7,letter_in_8,letter_in_9
    letter_in_1 = input("First letter? Enter 1 for vowels, 2 for consonants, 3 for random, or type any letter: ")
    letter_in_2 = input("Second letter? Enter 1 for vowels, 2 for consonants, 3 for random, or type any letter: ")
    letter_in_3 = input("Third letter? Enter 1 for vowels, 2 for consonants, 3 for random, or type any letter: ")
    letter_in_4 = input("Fourth letter? Enter 1 for vowels, 2 for consonants, 3 for random, or type any letter: ")
    letter_in_5 = input("Fifth letter? Enter 1 for vowels, 2 for consonants, 3 for random, or type any letter: ")
    letter_in_6 = input("Sixth letter? Enter 1 for vowels, 2 for consonants, 3 for random, or type any letter: ")
    letter_in_7 = input("Seventh letter? Enter 1 for vowels, 2 for consonants, 3 for random, or type any letter: ")
    letter_in_8 = input("Eigth letter? Enter 1 for vowels, 2 for consonants, 3 for random, or type any letter: ")
    letter_in_9 = input("Ninth letter? Enter 1 for vowels, 2 for consonants, 3 for random, or type any letter: ")

###
#function that generate a randomized 9 digit string.
#Press c for a consonant
#Press v for a vowel
#Press l for a random number
#Or type any other random letter(that isn't c,v, or l)
###
def generator():
    if letter_in_1 =='1':
        let1 = random.choice(vowels)
    elif letter_in_1 =='2':
        let1 = random.choice(consonants)
    elif letter_in_1 =='3':
        let1 = random.choice(letters)
    else:
        let1 = letter_in_1

    if letter_in_2 =='1':
        let2 = random.choice(vowels)
    elif letter_in_2 =='2':
        let2 = random.choice(consonants)
    elif letter_in_2 =='3':
        let2 = random.choice(letters)
    else:
        let2 = letter_in_2

    if letter_in_3 =='1':
        let3 = random.choice(vowels)
    elif letter_in_3 =='2':
        let3 = random.choice(consonants)
    elif letter_in_3 =='3':
        let3 = random.choice(letters)
    else:
        let3 = letter_in_3

    if letter_in_4 =='1':
        let4 = random.choice(vowels)
    elif letter_in_4 =='2':
        let4 = random.choice(consonants)
    elif letter_in_4 =='3':
        let4 = random.choice(letters)
    else:
        let4 = letter_in_4

    if letter_in_5 =='1':
        let5 = random.choice(vowels)
    elif letter_in_5 =='2':
        let5 = random.choice(consonants)
    elif letter_in_5 =='3':
        let5 = random.choice(letters)
    else:
        let5 = letter_in_5

    if letter_in_6 =='1':
        let6 = random.choice(vowels)
    elif letter_in_6 =='2':
        let6 = random.choice(consonants)
    elif letter_in_6 =='3':
        let6 = random.choice(letters)
    else:
        let6 = letter_in_6

    if letter_in_7 =='1':
        let7 = random.choice(vowels)
    elif letter_in_7 =='2':
        let7 = random.choice(consonants)
    elif letter_in_7 =='3':
        let7 = random.choice(letters)
    else:
        let7 = letter_in_7

    if letter_in_8 =='1':
        let8 = random.choice(vowels)
    elif letter_in_8 =='2':
        let8 = random.choice(consonants)
    elif letter_in_8 =='3':
        let8 = random.choice(letters)
    else:
        let8 = letter_in_8

    if letter_in_9 =='1':
        let9 = random.choice(vowels)
    elif letter_in_9 =='2':
        let9 = random.choice(consonants)
    elif letter_in_9 =='3':
        let9 = random.choice(letters)
    else:
        let9 = letter_in_9

    name = let1+let2+let3+let4+let5+let6+let7+let8+let9
    return(name)

def restartPrg():
    askRstrt = input("Press Q to quit, press any other button to restart: ")
    if askRstrt == 'q':
        exit()
    else:
        main()


    
def main():
    takeIn()
    
    for i in range(20):
       print(generator())
    print("")
    restartPrg()
    print("")

    
main()
    
