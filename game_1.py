import random
import TC
from RandomisationandPythonLists import Final_Prj

hjs = ''

def game_1():

    while True:
        u_1 = random.choice(rps)
        u_2 = random.choice(rps)

    #! USER ONE WIN     
        if rps.index(u_1) == 0 and rps.index(u_2) == 2:
            print (f'{u_1}\n{u_2}')        
            u_1 = u1i
            u_2 = u2i
            print(f'{u_1} WIN, {u_2} LOSS')

            #! STORE WINNER NAME
            winner_name_1 = u_1
            print(winner_name_1)
            break

    #! USER TWO WIN
        elif rps.index(u_2) == 0 and rps.index(u_1) == 2:
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{u_2} WIN, {u_1} LOSS')
            
            #! STORE WINNER NAME
            winner_name_1 = u_2
            print(winner_name_1)
            break

    #! USER TWO WIN 
        elif rps.index(u_2) > rps.index(u_1):    
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{u_2} WIN, {u_1} LOSS')

            #! STORE WINNER NAME
            winner_name_1 = u_2
            print(winner_name_1)
            break
        
    #! USER ONE WIN 
        elif rps.index(u_1) > rps.index(u_2):
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{u_1} WIN, {u_2} LOSS')

            #! STORE WINNER NAME
            winner_name_1 = u_1
            print(winner_name_1)
            break

    #! DRAW CONDITION:
        elif rps.index(u_1) == rps.index(u_2):
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
        #! IF DRAW WE NEED TO REPLAY THE GAME
            r = input('THIS IS A DRAW, PRESS "R" TO PLAY AGAIN:\n')
            if r == 'R':
                continue
            else:
                print('OKK')
                break


#! FIRST AND SECOND PERSON
u_1_n = input('FIRST ENTER YOUR NAME:\n')
u_2_n = input('SECOND ENTER YOUR NAME:\n')

rps = [Final_Prj.rock  , Final_Prj.paper, Final_Prj.scissors]

u1i = u_1_n
u2i = u_2_n

#! START THE GAME      
game_1()