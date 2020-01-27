'''
This a Game of rolling two dices.
Input:None
Output:A number between 1 and 6
Created By:Dhritiman Mukherjee
Date of Creation: 27-JAN-2020
'''

import random
#importing random for getting a random number between 1 and 6
Roll_Dice='Y'
print("Do You Want To Roll The Dices : ")
Roll_Dice=input("Press Y or N : ")
while Roll_Dice=="Y":
    print("Rolling the Dice: ",end="")
    print(random.randint(1,6))
    print(random.randint(1,6))
    Roll_Dice=input("Do You Want To Roll Again: ")    
