import time
import random

def displayIntro():
    print('''Welcome to the Monster Mansion, where danger lurks around
every corner and while everyone is allowed in, not everyone who enters
makes it to the exit. Would you like to test your courage?''')
    
def chooseEntrance():
    entrance = ''
    while entrance != 'f' and entrance != 's':
        print('Would you like to go in the front door (f) or side door (s)?')
        entrance = input()

    if entrance == 'f':
        entrance = 1
    else:
        entrance = 2

    return entrance


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()

    print('Do you want to play again? (yes or no)')
    playAgain = input()
