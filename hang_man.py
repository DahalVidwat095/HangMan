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
    word_to_be_guessed = "cat"

    while wrong_guess_number < len(hangman_array):
        # ask the word from user 
        print("Guess the word?")
        display_word_place = "_ " * len(word_to_be_guessed)
        print(display_word_place)
        print("")
        word_guessed_by_user = input(">> ").lower()

        if word_guessed_by_user == word_to_be_guessed:
            print("You got it !!!")
            return
        else:
            print(hangman_array[wrong_guess_number])
            wrong_guess_number += 1
            chances_left -= 1
            print("Number of chance left:", chances_left)
            print("")























if __name__ == "__main__":
    main()