#important random library to utilize to select to secret_words
import random
words= ["hangman", "bergen", "python", "library"]
#I use random.choice(words) because I want to random words from my words list
secret_word = random.choice(words)
#I want to my letters should be lower and one letter from my words list
dashes = "-" * len(secret_word)
number_of_guesses= 5
#this function will ask the user to input a guess letter
def get_guess():
#to repeadtly ask the user for guesses we are constracting while loop
#the loop will end when the condition is met
    while True:
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print "Please enter one letter at the time! "
        elif not guess.islower():
            print "Please enter lowercase! "
        else:
            return guess
#this function is to find each letter
def update_dashes(words, dashes, guess):
#the for loop will be executed based on the words length
    for i in range(len(words)):
#we use i to check each index in the word by assigning words [i] because I want to check each index of the word and identifed if the my guess was found in that specific index
        if words [i] == guess:
#since my conditions was met I am updating the value of dashes by replacing the dash with the guess letter
            dashes = dashes[:i] + guess + dashes[i+1:]
#when the conditions is not met I return the same values of dashes
    return dashes

while number_of_guesses>0 and dashes != secret_word:
# we created the guess variable to store the out of the return function
    print dashes
    print number_of_guesses

    guess = get_guess()
    dashes=update_dashes(secret_word, dashes, guess)

#my condition is guess in secret_word we use the if/else statements because we want to check the letter to see if it is found in my secter word
    if guess in secret_word:
        print "That letter is in the secret word"
    else:
        print "That letter is not in the secret word"
        number_of_guesses = number_of_guesses - 1

#I use if/else statements because I want to check if my number_of_guesses == 0 I want to print "You lost!"
if number_of_guesses == 0:
    print "You lost! That word was:  " +  secret_word
#else check my number_of_guesses != 0
else:
    print "You won! That word was:  " + secret_word
