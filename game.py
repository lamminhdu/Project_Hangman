import random
import string

from words import words

alphabet = set(string.ascii_letters)


def is_not_in_alphabet(word):
    # Check whether word contain special characters
    for letter in word:
        if letter not in alphabet:
            return True
    return False


def get_valid_word(words):
    # Get valid word from words list
    word = random.choice(words)
    while is_not_in_alphabet(word):
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letter = set(word)
    used_letter = set()  # keep track user input word
    lives = 7
    print(word)
    while len(word_letter) > 0 and lives > 0:
        print("")
        # show lives
        print(f"You have {lives} live(s) remain, be careful !!!")

        # show used letter
        print("You have used these letters: ", ' '.join(used_letter))

        # show word
        word_list = ['-' if letter not in used_letter else letter for letter in word]
        print("You need to guess the word: ", ' '.join(word_list))

        # Get user input
        user_input = input("Please enter guess letter: ").upper()

        if user_input in alphabet:
            if user_input not in used_letter:
                used_letter.add(user_input)
                if user_input in word:
                    word_letter.remove(user_input)
                else:
                    print("Sorry the letter you guess not in word")
                    lives -= 1
            else:
                print("You have used this letter !!")
        else:
            print("Invalid letter")

    # Get here when guess true or lives = 0
    if lives > 0:
        print(f"Congratulations !! The word is: {word}")
    else:
        print(f"You died !!! The word was: {word}")


# Use index to check word
def hangman_ver2():
    word = get_valid_word(words)
    used_letter = set()
    word_letter = ['-' for letter in word]
    lives = 7
    print(word)

    while '-' in word_letter and lives > 0:
        # show lives
        print(f"\nYou have {lives} live(s) remain, be careful")

        # show used letters
        print("You have used these letters: ", ' '.join(used_letter))

        # show word need to guess
        print("You need to guess the word: ", ' '.join(word_letter))

        # get user input
        user_input = input("Please input your guess letter: ").upper()

        if user_input not in alphabet:
            print("Invalid letter")
        else:
            if user_input not in used_letter:
                used_letter.add(user_input)
                is_in_word = False
                for i in range(len(word)):
                    if user_input == word[i]:
                        word_letter[i] = user_input
                        is_in_word = True
                if is_in_word == False:
                    print(f"Sorry, the word not contain this {user_input} letter!")
                    lives -= 1
            else:
                print("You have used this letter !")

    # Get here when guess true or lives = 0
    if lives > 0:
        print(f"Congratulations !! The word is: {word}")
    else:
        print(f"You died !!! The word was: {word}")

if __name__ == '__main__':
    hangman()
    hangman_ver2()