import random 

# _Make a rock, paper, scissors game.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#    0       2
# Rock B Scissors
#    1       0
#Paper B Rock
#    2        1
#scissors B Paper


user_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')) #! USER INPUT HER CHOICE

choices = [rock, paper, scissors] #! MERGE ROCK, PAPER, SCISSORS IN ONE VARIABLE TO LET COMPUTER CHOICE A RANDOM ITEM
computer_choice = random.choice(choices) #! FUNCTION TO LET COMPUTER CHOICE A RANDOM ITEM AND CONVERT IT TO IMAGE
user_image = (choices[user_choice]) #! CONVERT USER CHOICE TO IMAGE

# print(f'User choice: {user_image}\n Computer Choice: {computer_choice}')


if user_choice >= 3:
    print('YOU ENTRED INVALID NUMBER')
elif user_choice < 2:
    print(f'USER CHOICE: {user_image}\n COMPUTER CHOICE: {computer_choice}\YOU LOSE')
elif user_choice == 0 or 1 or 2:
    print(f'USER CHOICE: {user_image}\n COMPUTER CHOICE: {computer_choice}\THIS IS A DRAW')
elif user_choice > 2:
    print(f'USER CHOICE: {user_image}\n COMPUTER CHOICE: {computer_choice}\YOU WIN')

#? NEED MORE LINES
    
#//----------                        END                             -------------##
#//----------                        END                             -------------##