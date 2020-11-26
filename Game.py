import random
print('Welcome to my guessing game, your task is to guess a number between 1 and a 100, you have 10 guesses, good luck!')
guesses = []
num = random.randint(1,100)
previousguesses = guesses

while True:
    guess = int(input('I am thinking of a number between 1 and a hundred. \n what is your guess? '))
    guesses.append(guess)
    print(previousguesses)
    if guess < 1 or guess > 100:
        print('Invalid guess, guess a number between 1 and 100. ')
        continue
    if guess == num and abs(len(guesses)) == 1:
        print('Congratulations! On your first try aswell.')
        break
    if guess == num and abs(len(guesses)) < 10:
        print(f'Congratulations! You guessed it in {len(guesses)} guesses.')
        break
    if abs(len(guesses)) == 10:
        print('You lose. Goodday.')
        print('The number was ' + str(num))
        break
    if abs(len(guesses)) == 1:
        if abs(num - guesses[-1]) > 10:
            print('COLD')
        if abs(num - guesses[-1]) <= 10:
            print('WARM')
        continue
    if abs(len(guesses)) > 1:
        if abs(num - guesses[-2]) < abs(num - guesses[-1]):
            print('COLDER')
        if abs(num - guesses[-2]) > abs(num - guesses[-1]):
            print('WARMER')
        continue