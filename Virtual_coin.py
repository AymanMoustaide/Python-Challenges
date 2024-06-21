# Virtual coin toss program

import random


flip_coin = random.randint(1, 2)

if flip_coin == 1:
    print('Heads')
else: 
    print('Tails')