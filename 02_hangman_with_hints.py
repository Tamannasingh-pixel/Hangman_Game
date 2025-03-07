import random
from hangman_stages import stages
from hangman_word import hangman_words

lives = 6
chosen_word = random.choice(list(hangman_words.keys()))

placeholder = ""
for position in range (len(chosen_word)):
    placeholder += "_"
print(placeholder)
# print (chosen_word)
print(f"hint: {hangman_words[chosen_word]}")

game_over = False
correct_letter = []

while not game_over:
    guess = input("enter a letter here:").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"

    print (display)
    print (f"******************** you have {lives} / 6 lives left ********************")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print ("******************** you lose! ********************")
            print (f" correct word : {chosen_word}")

    if "_" not in display:
        game_over = True
        print("******************** you win! ********************")

    print(stages[lives])
