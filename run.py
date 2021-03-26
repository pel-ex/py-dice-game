#Account Verification to game import - Pygame hashed out because school zzz

#import pygame
import sys
import random
from sys import exit

#pygame paramaters
#pygame.init()
#pygame.display.set_caption('2 Player Dice Game')
#programIcon = pygame.image.load('icon.jpg')

#pygame.display.set_icon(programIcon)

#size = 500                      # window size

logstate = False

acc1 = False
found1 = False
while acc1 == False:
    username1=input("username: ")
    password1=input("password: ")
    file=open("{file destination.csv}", "r+")
    for line in file:
        details=line.split(",")
        if details[0]==username1 and details [1]==password1 +"\n":
            print("account found")
            found1 = True
            acc1 = True
    if found1 == False:
        print ("account not found" +"\n")
        answer1=input("Would you like to make an account with the details given? (Y/n)")
        if answer1=="Y" or answer1=="y":
            file.write(username1+","+password1)
            print("Account saved")
            acc1 = True
        elif answer1=="N" or answer1=="n":
            print("")
        else:
            print("Unexpected Value")
file.close()

acc2 = False
found2 = False
while acc2 == False:
    username2=input("username: ")
    password2=input("password: ")
    file=open("{file destination.csv}", "r+")
    for line in file:
        details=line.split(",")
        if details[0]==username2 and details [1]==password2 +"\n":
            print("account found")
            found2 = True
            acc2 = True
    if found2 == False:
        print ("account not found" +"\n")
        answer2=input("Would you like to make an account with the details given? (Y/n)")
        if answer2=="Y" or answer=="y":
            file.write(username2+","+password2)
            print("Account saved")
            acc2 = True
        elif answer2=="N" or answer2=="n":
            print("")
        else:
            print("Unexpected Value")
file.close()

if acc1 and acc2 == True:
    LogState = True

print ("Options:")
print ("1: Open Game")
print ("2: Open Leaderboard")
print ()
choice = input("Goto: ")
while LogState == True:
    if choice = 1:
        import dice
        #execfile('dice.py')
    elif choice = 2:
        import leaderboard
        #exectfile('leaderboard.py')
    else:
        ("error: restart programme")
