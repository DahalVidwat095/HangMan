def main():

    hangman_array = hangman_array_maker()
    guess_word(hangman_array)


def hangman_array_maker():

    # Multiline comment explaining the hangman list creation
    r"""
    While making this list, I learned these things:
        1. Multiline strings can be enclosed in triple quotes (''' Your multi-line string ''').
        2. The 'r' prefix indicates a raw string, which solves issues with backslashes (\).
        3. To align the figure perfectly, separate the content from the line containing quotes:
           r''' 
           Your content goes here.
           '''
    """

    # list that contains different stages of hangman
    hang_array  = [ r'''
                     +------++      
                     |      ||
                            ||
                            ||
                            ||
                            ||
                  ==============
                     ''',
              
                    r'''
                     +------++      
                     |      ||
                     O      ||
                            ||
                            ||
                            ||
                  ==============
                     ''', 
              
                    r'''
                     +------++      
                     |      ||
                     O      ||
                     |      ||
                            ||
                            ||
                  ==============
                     ''',  

                    r'''
                     +------++      
                     |      ||
                     O      ||
                    /|      ||
                            ||
                            ||
                  ==============
                     ''',   

                    r'''
                     +------++      
                     |      ||
                     O      ||
                    /|\     ||
                            ||
                            ||
                  ==============
                     ''',  
                              
                    r'''
                     +------++      
                     |      ||
                     O      ||
                    /|\     ||
                    /       ||
                            ||
                  ==============
                     ''', 

                    r'''
                     +------++      
                     |      ||
                     O      ||
                    /|\     ||
                    / \     ||
                            ||
                  ==============
                     ''' ]

    return hang_array


def guess_word(hangman_array):
    wrong_guess_number = 0
    chances_left = len(hangman_array)
    word_to_be_guessed = "elephant"
    display_word = list("_" * len(word_to_be_guessed))
    print("".join(display_word))
    print("")

   
    while wrong_guess_number < len(hangman_array):
        # ask to guess a letter from the user 
        print("Guess a letter?")
        print("")
        letter_guessed_by_user = input(">> ").lower()

        if letter_guessed_by_user in word_to_be_guessed:
            for index, char in enumerate(word_to_be_guessed):
                if letter_guessed_by_user == char:
                    display_word[index] = letter_guessed_by_user
            print("".join(display_word))
            if "_" not in display_word:
                print("Congratulations! You've guessed the word:", "".join(display_word))
                print("")
                return
        else:
            print(hangman_array[wrong_guess_number])
            wrong_guess_number += 1
            chances_left -= 1
            print("Number of chance left:", chances_left)
            print("")
    print("Sorry, you've run out of chances. The word was:", word_to_be_guessed)
    print("")


if __name__ == "__main__":
    main()
    