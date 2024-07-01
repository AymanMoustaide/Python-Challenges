import random
from TC import green_s,green_e,red_s,red_e
from RandomisationandPythonLists import Final_Prj


def game_2():
    global winner_name_2  #* DECLARE AS GLOBAL TO USE IT OUTSIDE THE FUNCTION
    winner_name_2 = None
    
    while True:
        u_3 = random.choice(rps)
        u_4 = random.choice(rps)
        

    #! USER ONE WIN     
        if rps.index(u_3) == 0 and rps.index(u_4) == 2:
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i
            print(f'{green_s}{u_3.upper()} WIN{green_e}, {u_4.upper()} LOSS')

    #! STORE WINNER NAME
            winner_name_2 = u_3
            # print(winner_name_2)
            break

    #! USER TWO WIN
        elif rps.index(u_4) == 0 and rps.index(u_3) == 2:
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i
            print(f'{green_s}{u_4.upper()} WIN{green_e}, {u_3.upper()} LOSS')
    #! STORE WINNER NAME
            winner_name_2 = u_4
            #// print(winner_name_2)
            break

    #! USER TWO WIN
        elif rps.index(u_4) > rps.index(u_3):
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i
            print(f'{green_s}{u_4.upper()} WIN{green_e}, {u_3.upper()} LOSS')
    #! STORE WINNER NAME
            winner_name_2 = u_4
            #// print(winner_name_2)
            break
    
    #! USER ONE WIN
        elif rps.index(u_3) > rps.index(u_4):
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i
            print(f'{green_s}{u_3.upper()} WIN{green_e}, {u_4.upper()} LOSS')
    #! STORE WINNER NAME
            winner_name_2 = u_4
            #// print(winner_name_2)
            break

    #! DRAW CONDITION
        elif rps.index(u_3) == rps.index(u_4):
            print (f'{u_3}\n{u_4}')
            u_3 = u4i
            u_4 = u4i
        #! IF DRAW WE NEED TO REPLAY THE GAME
            restart = input(f'{red_s}THIS IS A DRAW, PRESS "R" TO PLAY AGAIN:{red_e}\n')
            if restart == 'R':
                continue
            else:
                print(f"{red_s}SORRY WE CAN'T KNOW WHO WIN{red_e}")
                break
    return  winner_name_2


#! LIST OF ROCK PEPER SICOSSOR
rps = [Final_Prj.rock, Final_Prj.paper, Final_Prj.scissors]

#! THIRD AND FORTH PERSON
u_3_n = input('FIRST ENTER YOUR NAME:\n')
u_4_n = input('SECOND ENTER YOUR NAME:\n')

#! UPDATE VARIABLE TO TAKE INPUT VALUE
u3i = u_3_n
u4i = u_4_n

#! START THE GAME       
game_2()