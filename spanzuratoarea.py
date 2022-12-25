import random
import sys

# a quit function
def quit_function():
    sys.exit("\n" + "See ya!")

# a menu for selecting the game's difficulty
def gamemode():
    print('''alege dificultatea: \n 
    1 - EASY 6 vieti , cuvinte pana in 5 litere \n 
    2 - HARD 3 vieti cuvinte cu peste 6 litere \n 
    "quit" 
    ''')
    difficulty = input('enter the difficulty = ')
    if difficulty == '1' or difficulty == '2':
        return difficulty
    elif difficulty == 'quit':
        print("Goodbye")
        return quit_function()

# sets the players lifes depending on the difficulty chosen
def game_stats(difficulty):
    if difficulty == '1':
        return 6
    elif difficulty == '2':
        return 3

# takes words from a txt file
def word_list():
    defoult_words = []
    word_list = []
    f = open("words.txt", "r")
    lines = f.readlines()
    for words in lines:
        word_set = words.split(',')
        defoult_words.append(word_set)
    for i in defoult_words:
        word_list.append(i[0])
    return word_list

# devides the words in 2 lists depending on the difficulty
def list_difficulty(words, difficulty):
    easy_words = []
    hard_words = []
    for i in words:
        if len(i) <= 5:
            easy_words.append(i.lower())
        elif len(i) > 5:
            hard_words.append(i.lower())
    if difficulty == '1':
        return easy_words
    elif difficulty == '2':
        return hard_words

# displays a drawing depending on many lifes the player currently has
def status_display(difficulty):
    easy_list = ['''
    -------------
    |           |
    |           |
    |
    |
    |
    |
    /|\  
    -----
    ''', '''
    -------------
    |           |
    |           |
    |           O
    |
    |
    |
    /|\  
    -----
    ''', '''
    -------------
    |           |
    |           |
    |           O
    |           |
    |           |
    |
    /|\  
    -----
    ''', '''
    -------------
    |           |
    |           |
    |           O
    |          /|
    |         / |
    |
    /|\  
    -----
    ''', '''
    -------------
    |           |
    |           |
    |           O   
    |          /|\  
    |         / | \ 
    |
    /|\  
    -----
    ''', '''
    -------------
    |           |
    |           |
    |           O
    |          /|\  
    |         / | \ 
    |          /
    /|\       /
    -----
    ''', '''
    -------------
    |           |
    |           |
    |           O
    |          /|\  
    |         / | \ 
    |          / \  
    /|\       /   \ 
    -----
    ''']
    hard_list = [easy_list[0], easy_list[2], easy_list[4], easy_list[6]]
    if difficulty == '1':
        return easy_list
    elif difficulty == '2':
        return hard_list

# allows the possibilty of a replay
def replay():
    print("do you wish to play again? yes- replay , no - exit")
    user_input2 = input()
    if user_input2 == 'yes':
        main()
    elif user_input2 == 'no':
        quit_function()
    else:
        print("not a valid input")


def main():
    difficulty = gamemode()
    life = game_stats(difficulty)
    words = word_list()
    word_difficulty = list_difficulty(words, difficulty)
    life_status = status_display(difficulty)
    # the main algorithm that useses the words extracted from the txt file
    random_word = random.choice(word_difficulty)
    hidden_word = ["_" for i in range(len(random_word))]
    lifes = life
    used_letters = []
    drawings = 0
    print(life_status[0])
    while lifes > 0:
        print(''.join(hidden_word),
                f"life={lifes}", f"\t used letters={used_letters}")
        user_input = input()
        if user_input in used_letters:
            print("you already used that letter")
            pass
        if (user_input not in random_word) and (user_input.isalpha() == True) and (user_input not in used_letters):
            lifes -= 1
            drawings += 1
            if user_input not in used_letters:
                used_letters.append(user_input)
            print(life_status[drawings])
        elif user_input in random_word:
            for i, z in enumerate(random_word):
                if (user_input in random_word) and (user_input == z) and (user_input not in used_letters):
                    used_letters.append(user_input)
                    hidden_word[i] = z
        elif user_input.isalpha() == False:
            print('this is not a valid input , try again:')
            user_input = input()
        if ''.join(hidden_word) == random_word:
            print("you win")
            lifes = 0
            random_word = ''
        elif lifes == 0:
            print(f"hidden word = {random_word}")
            print("Try again")
    replay()


if __name__ == "__main__":
    main()
