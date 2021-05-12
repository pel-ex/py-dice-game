#Made by Alex Brand (pel-ex)
#Published under MIT Licence
#School Project - Not updated much, do with this as you like

import random
import sys

overtime = 1 #set cvar to 0 to turn off overtime

p1score = 0
p2score = 0
p1total = 0
p2total = 0
p1dice = 0
p2dice = 0

#set file destination of score.txt
score_destination = "{file destination}"

for rounds in range (1,6):
    print ("round: ", rounds, "")
    p1dice = input("user 1 ready? (Y/n) ")
    if p1dice == "Y" or p1dice == "y":
        p1dice1 = random.randint(1, 6)
        p1dice2 = random.randint(1, 6)
        p1total = p1dice1 + p1dice2
        print ("you rolled a "  + str(p1dice1) + " and a " + str(p1dice2) +  " giving you ", p1total)
        p1even = p1total % 2
        if p1even == 0:
            p1total = p1total + 10
            print ("your total is even so 10 has been added to your score giving you:", p1total)
        elif p1even == 1:
            p1total = p1total - 5
            print ("total is odd so your score is deducted by 5 giving you :", p1total)
        if p1dice == p2dice:
            print("you rolled a double so you can role again")
            p1dice3 = random.randint(1,6)
            print ("you rolled a, " , p1dice3)
            p1total = p1total + p1dice3
            print ("making your total after round", rounds, ":", p1total)
            if p1total< 0:
                p1total = 0
                print ("your total is so bad we set it back to 0")

            p1score = p1score + p1total
            print ("your score for this game is", p1score)

for rounds in range (1,6):
    print ("round: ", rounds)
    p2dice = input("user 2 ready? (Y/n)")
    if p2dice == "Y" or p2dice == "y":
        p2dice1 = random.randint(1, 6)
        p2dice2 = random.randint(1, 6)
        p2total = p2dice1 + p2dice2
        print ("you rolled a "  + str(p2dice1) + " and a " + str(p2dice2) +  " giving you ", p2total)
        p2even = p2total % 2
    else:
        print ("\n error \n")
        if p2even == 0:
            p2total = p2total + 10
            print ("your total is even so 10 has been added to your score giving you:", p2total)
        elif p2even == 1:
            p2total = p2total - 5
            print ("total is odd so your score is deducted by 5 giving you :", p2total)
        if p2dice == p2dice:
            print("you rolled a double so you can role again")
            p2dice3 = random.randint(1,6)
            print ("you rolled a, ", p2dice3)
            p1total = p2total + p2dice3
            print ("making your total after round", rounds, ":", p2total)
            if p2total< 0:
                p2total = 0
                print ("your total is so bad we set it back to 0")

            p2score = p2score + p2total
            print ("your score for this game is", p2score)

while p1total == p2total:
    print ("scores are equal \n")

    if overtime == 1:
       while p1total == p2total:
        num1 = random.randint(1,6)
        num2 = random.randint(1,6)
        print ("player 1 rolled:", num1, "/n player 2 rolled", num2)
        p1total = p1total + num1
        p2total = p2total + num2
        print ("player 1 game total:", p1total, "/n player 2 game total", p2total)

if p1total > p2total:
    winner = input("player 1 name: ")
    score == p1total
elif p2total > p1total:
    winner = input ("player 2 name: ")
    score == p2total
else:
    error - game crashed

file = open(score_destination)
file.write("\n" + winner + "," + str(score))
file.close

import leaderboard
