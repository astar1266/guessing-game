import random
import time
print("Hello! Welcome to the number guessing game!!")

the_first_random_number = random.randint(1, 100)
the_first_seccend_number = random.randint(1, 100)

# Swap the numbers if necessary
if the_first_random_number > the_first_seccend_number:
    the_first_random_number, the_first_seccend_number = the_first_seccend_number, the_first_random_number

input_str = "What do you think the number is between " + str(the_first_random_number) + " and " + str(the_first_seccend_number) + ": "
user_guess = int(input(input_str))
the_number = random.randint(the_first_random_number, the_first_seccend_number)

if user_guess == the_number:
    print("You're a top G 😎😊😎😍")
else:
    print("L + ratio. The answer was: " + str(the_number))

time.sleep(60)
