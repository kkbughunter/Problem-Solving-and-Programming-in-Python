#Write a program to generate a list with 5 random numbers between 100 and 200 inclusive

import random
list1=[random.randint(100,201) for a in range(0,5)]
print(list1)