import random
import TC
from RandomisationandPythonLists import Final_Prj
import game_F1
import game_F2


def success(): #! PREVIOUS WINNERS

    print(f'{TC.green_s}{game_F1.winner_name_1.upper()} IS THE WINNER FROM THE FIRST GAME{TC.green_e}')
    print(f'{TC.green_s}{game_F2.winner_name_2.upper()} IS THE WINNER FROM THE SECOND GAME{TC.green_e}')
    print()
    print(f'{TC.bleu_s}NOW WE GONNA PLAY BIGGER NUMBER WIN GAME TO FIND OUT WHO GONNA PAY THE BILL{TC.bleu_e}')
    
def bigger_(): #! CHOICE NUMBER FOR BIGGER() AND RANDOM_NAME()

    if bottle[0] < bottle[1]:
        print(f'{_2} IS BIGGER THAN {_1}, SO {TC.green_s}{game_F2.winner_name_2.upper()}{TC.green_e} WIN')
    
    elif bottle[1] < bottle[0]:
        print(f'{_1} IS BIGGER THAN {_2}, SO {TC.green_s}{game_F1.winner_name_1.upper()}{TC.green_e} WIN')

def another_game(): #! ASK USERS IF THEY WANT TO PLAY ANOTHER FUNNY GAME

    another_game = input('WANNA TRY ANOTHER GAME, PRESS "Y" ')

    if another_game == "Y":
        random_name()
    else:
        print('SEE YOU NEXT TIME')


def random_name(): #! RANDOM CHOICE GAME
    
    print('THE WAITRESS GONNA CHOICE RANDOM NUMBER FROM YOUR INPUTS...')
    print(f'{TC.bleu_s} 1...{TC.bleu_e}')
    print(f'{TC.green_s} 2... {TC.green_e}')
    print(f'{TC.yellow_s} 3... {TC.yellow_e}')
    print()

    if _1 == random.choice(bottle):
        print(f'THE WAITRESS CHOSE{TC.green_s} {game_F1.winner_name_1.upper()}{TC.green_e} NUMBER')
    elif _2 == random.choice(bottle):
        print(f'THE WAITRESS CHOSE{TC.green_s} {game_F2.winner_name_2.upper()}{TC.green_e} NUMBER')

    print()
    print(f'{TC.red_s}SEE YOU NEXT TIME{TC.red_e}')


#! START THE GAME

success()

_1 = input(f'{TC.green_s}{game_F1.winner_name_1.upper()}{TC.green_e}, PLEASE WRITE A NUMBER FROM 1 TO 10\n')
_2 = input(f'{TC.green_s}{game_F2.winner_name_2.upper()}{TC.green_e}, PLEASE WRITE A NUMBER FROM 1 TO 10\n')
bottle = [_1 , _2]

bigger_()
another_game()

