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

    gameOver = random.randint(1, 2)
    time.sleep(2)
    if entrance == gameOver:
        print('''You open the door and step inside. Immediately you trip
over an upturned corner of rug and fall into a trap door. The sound of
howling fills yours ears as a pack of rabid dogs descend on you and turn
you into their meal. Rest in pieces.''')
    else:
        print('''You open the door and find an empty corridor with blood
on one end and a mysterious fog at the other end. You get the feeling 
you're being watched and get the overwhelming urge to run back out the
door as fast as you can, living to see another day.''')
        
playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    chooseEntrance()

    print('Do you want to play again? (yes or no)')
    playAgain = input()
