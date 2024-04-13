#Number guessing game
import random  # This module is used to generate random numbers
import math  # This module provides mathematical functions

# Taking input from the user for the lower and upper bounds of the range
lower, upper = map(int, input("enter lower and upper:").split())
x = random.randint(lower, upper)  # Generating a random number within the specified range

# Calculating the maximum number of chances based on the range
print("\t You have only ", round(math.log(upper - lower + 1, 2)), "chances to guess.")

count = 0  # Counter to keep track of the number of attempts
wrong = 0  # Counter to keep track of out-of-range guesses

# Loop to continue until the user guesses correctly or runs out of chances
while count < round(math.log(upper - lower + 1, 2)):
   num = int(input("Guess the number:"))  # Taking input from the user

   # Checking if the guess is out of range
   if num < lower or num > upper:
       print("Number is out of range!")
       wrong += 1  # Incrementing the out-of-range counter
       if wrong == 5:  # If the user has made 5 out-of-range guesses, the game ends
           print("Better luck next time!")
           break

   # Checking if the guess is correct
   elif x == num:
       print("congratulations you have guessed in", count, "try.")
       break

   # Checking if the guess is too large
   elif num > x:
       print("You guessed too large")
       count += 1  # Incrementing the attempt counter

   # Checking if the guess is too small
   elif num < x:
       print("You guessed too small")
       count += 1  # Incrementing the attempt counter

# If the user runs out of chances, the correct number is revealed
if count >= round(math.log(upper - lower + 1, 2)):
   print("The number is :", x)
   print("Better luck next time")