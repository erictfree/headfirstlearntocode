color = 'blue'
guess = ''
guesses = 0

while guess != color:
    guess = input('What color am I thinking of? ')
    guesses = guesses + 1
print('You got it! It took you', guesses, 'guesses')
