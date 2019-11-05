import random


print("This is an interactive guessing game!")
print("You have to find a secret number between 1 and 99.")
print("Type 'exit' to end the game.")
print("Good luck!")
num = random.randint(1, 99)
attempt = 1
while 1:
    choice = input("What's your guess between 1 and 99?\n>> ")
    if choice == 'exit':
        print("Bye!")
        break
    try:
        choice = int(choice)
    except ValueError:
        print("That's not a number.")
        attempt += 1
        continue
    if choice < 1 or choice > 99:
        print("Number is out of range.")
    elif choice < num:
        print("Too low!")
    elif choice > num:
        print("Too high!")
    elif choice == num and attempt == 1:
        print("Congratulations, you got it first try!!!")
        break
    elif choice == num and attempt > 1:
        print("You got it!")
        print("You won in {} attempts!".format(attempt))
        break
    attempt += 1
