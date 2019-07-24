#!/usr/bin/python3

round = 0           #INT round init to 0
while(True):        #set up an infinit loop condition
    round = round + 1       #increase counter
    print('Finish the movie title, "Monty Python\'s The Life of _____"')
    answer = input()        #string answer collected from user
    if (answer.lower() == 'brian'): #logic to check if user gave correct ans
        print('Correct')    
        break
    elif (answer.lower() == 'shrubbery'): #logic for super secret answer
        print('You gave the super secret answer!')
        break
    elif (round==3):        #logic to ensure round has not yet reached 3
        print('Sorry, the answer was Brian')
        break               
    else:                   # if answer was wrong, and round not = to 3
        print('Sorry! Try again!')
