import random
inp =input("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100\nPlease choose a difficulty level:easy or hard\n")
number =random.randint(1,100)
if inp =="easy":
    chances =10
else:
    chances=5
print(f"You have {chances} chances")
while chances>0:
    user_number =int(input("Guess a number: "))
    if user_number==number:
        print("You WIN")
        break
    elif user_number>number:
        print("Too HIGH")
        print(f"You have {chances-1} chances left\n")
    elif user_number<number:
        print("Too Low")
        print(f"You have {chances-1} chances left!\n")
    chances-=1
print(f"The number was {number}")            

