#Comments 
#!INSTUCTION
#* Big Lines
#// End 
#? Need Fix

#_VIRTUAL COIN TOSS PROGRAM

import random

# flip_coin = random.randint(1, 2)

# if flip_coin == 1:
#     print('Heads')
# else: 
#     print('Tails')

#//----------                        END                             -------------##
#//----------                        END                             -------------##


#_ WIN A BRAND NEW CAR GIVEAWAY"


#*THERE ARE THREE BRAND NEW CARS & EIGHT GENERATED NUMBERS, YOU NEED TO MATCH THE SAME GENERATED NUMBER TO GET THE CAR

print('MERCEDES = 1\nBMW = 2\nAUDI = 3')

#!USER NEED TO TYPE FROM 1 TO 3
car_choicen = int(input('CHOICE YOUR DREAM CAR FROM THE LIST AND TYPE HER NUMBER: '))

#! COMPUTER GENERATE A RANDOM NUMBER FROM 1 TO 8
generated_number = random.randint(1, 8)

print(f'The generated number is: ', generated_number)

#!CHECKER FOR USER INPUT AND GENERATED NUMBER
if car_choicen == 1 and generated_number == 1:
    print('CONGRAT YOU WIN A MERCEDES')
elif car_choicen == 2 and generated_number == 2:
    print('CONGRAT YOU WIN A BRAND NEW BMW')
elif car_choicen == 3 and generated_number == 3:
    print('CONGRAT YOU WIN A AUDI')
else:
    print('YOUR ARE UNLUCKY:(')


#//----------                        END                             -------------##
#//----------                        END                             -------------##
    
    