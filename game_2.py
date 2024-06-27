import random
import TC
from RandomisationandPythonLists import Final_Prj

def game_2():
    while True:
        u_3 = random.choice(rps)
        u_4 = random.choice(rps)

    #! USER ONE WIN     
        if rps.index(u_3) == 0 and rps.index(u_4) == 2:
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i

    #! STORE WINNER NAME
            winner_name = u_3
            print(winner_name)
            print(f'{u_3} WIN, {u_4} LOSS')
            break

    #! USER TWO WIN
        elif rps.index(u_4) == 0 and rps.index(u_3) == 2:
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i

    #! STORE WINNER NAME
            winner_name = u_4
            print(winner_name)
            print(f'{u_4} WIN, {u_3} LOSS')
            break

    #! USER TWO WIN
        elif rps.index(u_4) > rps.index(u_3):
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i

    #! STORE WINNER NAME
            winner_name = u_4
            print(winner_name)
            print(f'{u_4} WIN, {u_3} LOSS')
            break
    
    #! USER ONE WIN
        elif rps.index(u_3) > rps.index(u_4):
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i
            print(f'{u_3} WIN, {u_4} LOSS')
            break

    #! DRAW CONDITION
        elif rps.index(u_3) == rps.index(u_4):
            print (f'{u_3}\n{u_4}')
            u_3 = u4i
            u_4 = u4i
        #! IF DRAW WE NEED TO REPLAY THE GAME
            r = input('THIS IS A DRAW, PRESS "R" TO PLAY AGAIN:\n')
            if r == 'R':
                continue
            else:
                print('OKK')
                break


rps = [Final_Prj.rock, Final_Prj.paper, Final_Prj.scissors]

#! THIRD AND FORTH PERSON
u_3_n = input('FIRST ENTER YOUR NAME:\n')
u_4_n = input('SECOND ENTER YOUR NAME:\n')

u3i = u_3_n
u4i = u_4_n

#! START THE GAME       
# game_2()