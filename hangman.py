import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


words = ['problem', 'console', 'terminal', 'package', 'version', 'control']
random_word = random.choice(words)
print(random_word)
dash=[]
for i in random_word:
    dash+="_"
print(dash)
end_of_game = False
lives=6
previous_guesses = ""
while not end_of_game:
    guess=(input('Guess the word : ')).lower()

    if guess in previous_guesses:
        print('You already guessed this word')
    else:
        previous_guesses += guess
        for position in range(len(random_word)):
            letter = random_word[position]
            if letter == guess:
                dash[position] = letter
        if guess not in random_word:
            if lives == 0:
                print("you lose")
                end_of_game = True
            print(stages[lives])
            lives -= 1
        print(' ' .join(dash))
        if "_" not in dash:
             end_of_game = True
             print("You won")
