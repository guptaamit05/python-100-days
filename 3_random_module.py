"""
random.random()  ## random value between 0-1  ( 0 include but 1 is exclude)
random.randint(a,b)   ## both a, b value include in output
random.choice([1,2,3,4,5,6,7,8])  random choice from the passed list
random.shufle(list)   shuffle the list in place and return None.
"""

import random
import my_module
import math


# print(random.choice([2,3,4,34,54,74,84,5,62]))
# print(random.randint(1,100))
# print(my_module.my_favorite_number)

# print(math.floor(random.random() * 100))



# print(random.randint(0,1))

names_list = ['amit', 'jay', 'omkar', 'teena', 'sai', 'ram', 'krishna','om']

print(names_list[random.randint(0, len(names_list)-1)])

print(random.choice(names_list))