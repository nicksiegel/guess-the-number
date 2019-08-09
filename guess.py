from random import randint

# keeps track of the number of guesses the user has taken
guesses_taken = 0

# asks the user for their name
print('hello, what is your name?')
my_name = input()

# generates a random number for the user to guess
number = randint(1, 50)
print('well, ' + my_name + ', im thinking of a number between 1 and 50')

# gives the user 6 tries to guess the number
while guesses_taken < 6:
    print('take a guess')
    guess = input()

    # converts string input to an integer
    guess = int(guess)

    # increment the number of guesses by 1 with each loop
    guesses_taken = guesses_taken + 1

    # tells the user if their guess is too low
    if guess < number:
        print('your guess is too low')

    # tells the user if their guess is too high
    if guess > number:
        print('your number is too high')

    # if the user guesses correctly, the game is over
    if guess == number:
        break

# tells user that they won if they guess number correctly
if guess == number:
    guesses_taken = str(guesses_taken)
    print('good job, ' + my_name + ' you guessed my number in ' + guesses_taken + ' guesses!')

# tells user that they lost if they run out of guesses
if guess != number:
    number = str(number)
    print('nope! the number i was thinking of was ' + number + '!')
