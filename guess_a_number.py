import random
secret_number = random.randint(1, 10)
guess = 5

while (guess > 0):
    print("You have " + str(guess) + " guesses left. ")
    user_guess = int(input("Guess the number between 1 and 10. What is your number?"))
    print()
    if user_guess == secret_number:
        print("You guessed right. You win!")
        play_again = input("Do you want to play again (y or n)?")
        if guess == 'y':
            guess = 5
        elif guess == 'n':
            guess = 0
            print('Bye.')   
    else:
        guess -= 1
        if guess == 0:
            print("Incorrect guess.")
            print("You have run out of guesses.")
        
        elif user_guess < secret_number:
            print("Incorrect guess. Try again.")
            print("Hint: " + str(user_guess) + " is too low.")
        elif user_guess > secret_number:
            print("Incorrect guess. Try again.")
            print("Hint: " + str(user_guess) + " is too high.") 
    
