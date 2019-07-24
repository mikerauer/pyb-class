#!/usr/bin/python3

story = open('romeo.txt')
story_list = story.readlines()
r_count = 0

for romeo in story_list:                    #create var to look for in list
    if romeo.lower().strip() == "romeo":    #looks for var(lower and strip whitespace) matching defined text
        r_count += 1                        #add 1 to counter

print(r_count)

