import random

# Intro
print("Welcome to Soumya's number guessing game!\n")

number = 8
guess = int(input("guess a number between 1-10: "))
print(number)
if (guess==number):
    print("hurray you won!!")
elif(guess==number-5):
    print("very close")
elif(guess==number+5):    
    print("very close")
else:
    print("better luck next time")