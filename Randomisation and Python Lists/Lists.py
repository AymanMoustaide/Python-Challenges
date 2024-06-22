import random

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
# "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", 
# "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
# "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
# "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

#! TO DISPLAY SPECIFIC ITEMS 
# print(states_of_america[2], states_of_america[4])

# ! TO ADD ANOTHER ITEM TO THE LIST 
# states_of_america.append('Fez')

#! TO EXTEND ITEM TO EACH LETTER 
# states_of_america.extend('Hawaii')

#! TO ADD ITEM TO SPECIFC PLACE 
# states_of_america.insert(49, 'Fez')

# ! TO REMOVE ITEM FROM THE LIST
# states_of_america.remove('Hawaii')


#! HOW MANY TIMES ITEM APPEARS IN LIST 
# print(states_of_america.count('Alaska'))

#! TO REMOVE SPECIFIC ITEM FROM THE LIST
# states_of_america.pop(49)
# print(states_of_america)

#//----------                        END                             -------------##
#//----------                        END                             -------------##

#_ CODE CHALLANGE : A PROGRAM WHICH WILL SELECT A RANDOM NAME FROM A LIST OF NAMES. THE PERSON SELECTED WILL HAVE TO PAY FOR EVERYBODY'S FOOD BILL.

#* TO PICK A RANDOM PERSON FROM AN INPUT

# names_string = input ("Give me everybody's names, seperated by a comma. ") # ! INPUT NAMES
# names = names_string.split(", ") # ! SPLIT EACH NAME ALONE
# number_of_peopel = len(names) #! COUNT HOW MUCH PEOPEL WE INPUT
# random_choice = random.randint(0, number_of_peopel -1) #! CONVERT PEOPEL ENTRED TO NUMBER & PICK ONE NUMBER 
# payer = names[random_choice] #! ASSIGNE THE NUMBER TO THE PERSON
# print(f'{payer} ' + 'who has gonna pay the bill today')

# #* TO PICK A RANDOM PERSON FROM A LIST 
# # names = ['Ayman', 'Angela', 'leila', 'imran', 'tamer', 'iphone'] #! List of peopel
# # random_index = random.randint(0, len(names) -1) #!CONVERT PEOPEL ENTRED TO NUMBER & PICK ONE NUMBER 
# # random_name = names[random_index] #!ASSIGNE THE NUMBER TO THE PERSON
# # print(f'{random_name}'who has gonna pay the bill today')

# # print(len(names))



#//----------                        END                             -------------##
#//----------                        END                             -------------##


#? #* DON'T CHANGE THE CODE BELOW

# row1 = [' ', ' ', ' ']
# row2 = [' ', ' ', ' ']
# row3 = [' ', ' ', ' ']
# map = [row1, row2, row3]



# print(f'{row1}\n{row2}\n{row3}')

# position = input( "Where do you want to put the treasure? ")

# horizonal = int(position[0]) #! HOLD THE FIRST INPUT NUMBER
# vertical = int(position[1]) #! HOLD THE SECOND INPUT NUMBER

# selected_row = map[vertical - 1] #! 

# selected_row[horizonal - 1] = "X"

# print(f'{row1}\n{row2}\n{row3}')


# #* DON'T CHANGE THE CODE ABOVE
# #Write your code below this row'

#//----------                        END                             -------------##
#//----------                        END                             -------------##





