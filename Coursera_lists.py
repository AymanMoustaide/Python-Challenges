import random
from random import randrange
import TC
from RandomisationandPythonLists import Final_Prj

#_ IMAGINE A GROUP OF FRIENDS GO TO A RESATAURENT, AFTER  FINSISHING THERE DINNER THEY WANNA PLAY A GAME THAT WHO'S GONNA PAY THE BILL, 
#* THE WAITER SUGGSET TO PLAY A GAME:
#* EVERYONE WILL WRITE A NUMBER IN PAPER BESIDE HER NAME THE WAITER WILL PICK ONE 
# THE CHOICEN ONE IS HOW GONNA PAY THE BILL



#! FIRST AND SECOND PERSON
u_1_n = input('FIRST ENTER YOUR NAME:\n')
u_2_n = input('SECOND ENTER YOUR NAME:\n')

u1i = u_1_n
u2i = u_2_n


#____________________________________________//

#! THIRD AND FORTH PERSON
# u_3_n = input('FIRST ENTER YOUR NAME:\n')
# u_4_n = input('SECOND ENTER YOUR NAME:\n')

# u3i = u_3_n
# u4i = u_4_n



def game_1():

    while True:
        rps = [Final_Prj.rock  , Final_Prj.paper, Final_Prj.scissors]
        u_1 = random.choice(rps)
        u_2 = random.choice(rps)
    
    #! USER ONE WIN     
        if rps.index(u_1) == 0 and rps.index(u_2) == 2:
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{u_1} WIN, {u_2} LOSS')
            # u1i = u_1 
            # print(f'test', {u1i})
            break

    #! USER TWO WIN
        elif rps.index(u_2) == 0 and rps.index(u_1) == 2:
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{u_2} WIN, {u_1} LOSS')
            break

    #! USER TWO WIN 
        elif rps.index(u_2) > rps.index(u_1):    
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{u_2} WIN, {u_1} LOSS')
            break
        
    #! USER ONE WIN 
        elif rps.index(u_1) > rps.index(u_2):
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
            print(f'{u_1} WIN, {u_2} LOSS')
            break
    
    #! DRAW CONDITION:
        elif rps.index(u_1) == rps.index(u_2):
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
        #! IF DRAW WE NEED TO REPLAY THE GAME
            r = input('THIS IS A DRAW, PRESS "R" TO PLAY AGAIN')
            if r == 'R':
                continue
            else:
                print('OKK')
                break



#! START THE GAME        
game_1()

def game_2():
    while True:
        rps = [Final_Prj.rock, Final_Prj.paper, Final_Prj.scissors]
        u_3 = random.choice(rps)
        u_4 = random.choice(rps)

    #! USER ONE WIN     
        if rps.index(u_3) == 0 and rps.index(u_4) == 2:
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i
            print(f'{u_3} WIN, {u_4} LOSS')
            break
   
    #! USER TWO WIN
        elif rps.index(u_4) == 0 and rps.index(u_3) == 2:
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i
            print(f'{u_4} WIN, {u_3} LOSS')
            break

    #! USER TWO WIN
        elif rps.index(u_4) > rps.index(u_3):
            print (f'{u_3}\n{u_4}')
            u_3 = u3i
            u_4 = u4i
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
            print (f'{u_1}\n{u_2}')
            u_1 = u1i
            u_2 = u2i
        #! IF DRAW WE NEED TO REPLAY THE GAME
            r = input('THIS IS A DRAW, PRESS "R" TO PLAY AGAIN')
            if r == 'R':
                continue
            else:
                print('OKK')
                break

#! START THE GAME        
# game_2()


















# def write_name_on_paper():
#     paper = input('WRITE YOUR NAME:\n')
    
#     list_of_peopel = paper.split()
#     waiter = random.choice(list_of_peopel)
    
#     print(f'{TC.red_s}I CHOOSE {waiter.upper()}{TC.red_e}')

#     wpa = input(f'{TC.bleu_s}WANNA PLAY AGAIN?:{TC.bleu_e}\n')

#     if wpa == 'yes':
#         write_name_on_paper()
#     elif wpa == 'no':
#         print(f'{TC.green_s}{waiter.upper()}{TC.green_e} GONNA PAY THE BILL, SEE YOU GUYS NEXT TIME :)')

    

# write_name_on_paper()
