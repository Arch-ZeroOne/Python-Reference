import random

# i = 0
# while i <= 5:
#  i += 1
#
#  if i == 3:
#      continue
#     #breaks the loop
#     # if i == 3:
#     #     break
#  print(i)
#  #continuation if a loop stops
# else :
#  print("Loop Stopped")

# i = 0
#
# while i != 5:
#     i += 1
#     print(i)



# # Number guessing game
# rand = random.randint(1,10)
# guess = 0
#
# while guess != rand:
#     guess = int(input("Guess the number 1 - 10:"))
#     if guess == rand:
#         print(f"Correct {guess} is the right number")
#     elif guess < rand:
#         print(f"{guess} is too low try a higher number")
#     elif guess > rand:
#         print(f"{guess} is too high try a lower number")

# Echo Bot

terminate = "bye"
user = ""

while user != terminate:
    user = input("User:")

    if user != terminate:
        print(f"Bot:{user}")
    else:
        print("Goodbye beep! boop! beep! boop!")





