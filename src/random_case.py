from random import random

def random_case(x):
    new_str = ""
    for c in x:
         roll = random()
         if roll >= 0.5:
             new_str += c.upper()
         else:
             new_str += c.lower()
    return new_str
