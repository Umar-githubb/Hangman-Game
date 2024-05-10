# Your Code

import random
word_list = ["prepinsta", "prime", "mohan"]
lives=6
chosen_word = random.choice(word_list)

#If we want access the word_list from other python file, we can use the below code instead of above
'''import word_file   #to import word_file python file
chosen_word = random.choice(word_file.words)  #words list present in word_file
print(chosen_word)'''
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
          '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
           '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
     '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
          '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
          '''
  +---+
  |   |
      |
      |
      |
      |
========='''
          ]
display = []
print("""
  _   _    _    _   _  ____ __  __    _    _   _
 | | | |  / \  | \ | |/ ___|  \/  |  / \  | \ | |
 | |_| | / _ \ |  \| | |  _| |\/| | / _ \ |  \| |
 |  _  |/ ___ \| |\  | |_| | |  | |/ ___ \| |\  |
 |_| |_/_/   \_\_| \_|\____|_|  |_/_/   \_\_| \_|

 """)


print("Hey! Let's play Hangman!")
print(stages[6])
for i in range(len(chosen_word)):
  display += '_'
print(display)

game_over = False
while not game_over:
  guess = input("Guess a letter: ").lower()
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = guess
      print("Good Job! "+ guess +" is in the word!")
  print(display)
  if guess not in chosen_word:
    lives -= 1
    print(stages[lives])
    print("You guessed "+ guess + " which is wrong")
    if lives == 0:
      game_over = True
      print("You lose!")
  if '_' not in display:
    game_over = True
    print("You Won!")




