import random

secret_number = random.randint(1,20)

attempts = 5

name= input("Enter your nickname befor entering into the game:")

print(f"Are you ready to dive into the Guessing world {name} !!!!")

print(f"You may have 5 attempts to win this game .")

print(f"Now! Let's dive into this world {name}")

print(f"You can choose any number ranges between 1 to 20")

while attempts > 0:
    guess = int(input("Enter your guess value :"))
    
    if guess == secret_number :
        print("Congratulations your guess is correct!!! ")
        break
    elif guess < secret_number:
        print("your guess value is too low !!.")
    else:
        print("Your guess value is too high")
        
   
        
    attempts = attempts-1

    if attempts ==0:
        print(f"Your chance limit has reached.The secret number was {secret_number}.")
        print("Better luck next time!!!")
    else:
        print(f"you have {attempts} chance(s) left.\n")
