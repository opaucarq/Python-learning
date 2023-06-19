'''
Created on 18 jun. 2023

@author: opaucarq

Guessing a number from 1 to 100000
'''

from random import randint
from pickle import NONE

start = 1
end = 1000

value = randint(start, end)

print("The computer choose a number between", start, "and", end)

guess = None 

while guess != value:
    text = input("Guess the number: ")
    guess = int(text)
    if guess == value: break
    print(("The number is Higher", "The number is Lower")[guess > value])
    
print("Congratulations!!! You guessed the number. You Won.")
