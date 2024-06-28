import random
import TC
from RandomisationandPythonLists import Final_Prj

def game_1():

    global winner_name_1  #* DECLARE AS GLOBAL TO USE IT OUTSIDE THE FUNCTION
    winner_name_1 = None

    while True:
        u_1 = random.choice(rps)
        u_2 = random.choice(rps)

    #! USER ONE WIN  
        if rps.index(u_1) == 0 and rps.index(u_2) == 2:
            print (f'{u_1}\n{u_2}')        
            u_1 = u1i
            u_2 = u2i
            print(f'{TC.green_s}{u_1.upper()} WIN{TC.green_e}, {u_2.upper()} LOSS')

            #! STORE WINNER NAME
            winner_name_1 = u_1
            #// print(f'{winner_name_1} WIN THIS ROUND!)
            break

    #! USER TWO WIN
        elif rps.index(u_2) == 0 and rps.index(u_1) == 2:
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{TC.green_s}{u_2.upper()} WIN{TC.green_e}, {u_1.upper()} LOSS')
            
            #! STORE WINNER NAME
            winner_name_1 = u_2
            #// print(winner_name_1)
            break

    #! USER TWO WIN 
        elif rps.index(u_2) > rps.index(u_1):    
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{TC.green_s}{u_2.upper()} WIN{TC.green_e}, {u_1.upper()} LOSS')

            #! STORE WINNER NAME
            winner_name_1 = u_2
            #// print(winner_name_1)
            break
        
    #! USER ONE WIN 
        elif rps.index(u_1) > rps.index(u_2):
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{TC.green_s}{u_1.upper()} WIN{TC.green_e}, {u_2.upper()} LOSS')

            #! STORE WINNER NAME
            winner_name_1 = u_1
            #// print(winner_name_1)
            break

    #! DRAW CONDITION:
        elif rps.index(u_1) == rps.index(u_2):
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
        #! IF DRAW WE NEED TO REPLAY THE GAME
            restart = input('THIS IS A DRAW, PRESS "R" TO PLAY AGAIN:\n')
            if restart == 'R':
                continue
            else:
                print("SORRY WE CAN'T KNOW WHO WIN")
                break
    return winner_name_1


#! LIST OF ROCK PEPER SICOSSOR
rps = [Final_Prj.rock  , Final_Prj.paper, Final_Prj.scissors]

#! FIRST AND SECOND PERSON
u_1_n = input('FIRST ENTER YOUR NAME:\n')
u_2_n = input('SECOND ENTER YOUR NAME:\n')

#! UPDATE VARIABLE TO TAKE INPUT VALUE
u1i = u_1_n
u2i = u_2_n

#! START THE GAME
game_1()

