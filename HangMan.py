from random_word import RandomWords

game_done = False
live = 5

while True:
     lvl = input("Enter a number to set hardness 6-15: ")
     if lvl.isdigit() and 6 <= int(lvl) <= 15:
        break;
     print('not valid input')

print(f'you have {live} lives')

# decorator 
def word_checker(lvl):
    def decorator(func):
        def wrapper(*args, **kwargs):
            while True:
                word = func(*args, **kwargs)
                if len(word) == lvl:
                    return word
        return wrapper
    return decorator

# get word and check it with the
@word_checker(int(lvl))
def getWords():
    random_words = RandomWords()
    return random_words.get_random_word()

def check_letter_in_word(imp):
    global live
    if imp in word:
        pos = [i for i in range(len(word)) if word[i] == imp]
        return pos
    else:
        print('the letter is not in the word -1 life')
        live -= 1
        print(f'your lives are: {live}')
        print(f'your word is : {hidden_word}')
        return None

def replacer(s, newstring, index, nofail=False):
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")
    if index < 0:
        return newstring + s
    if index > len(s):
        return s + newstring
    return s[:index] + newstring + s[index + 1:]

def check_is_alpha():
    global game_done
    if hidden_word.isalpha() == False:
        game_done = False
    else:
        game_done = True

word = getWords()
# print(word)
hidden_word = '*' * len(word)

print(f'your word is : {hidden_word}')

while game_done == False:
    if live == 0:
        print('you lost')
        print(f'the word was: {word}')
        break
    
    imp = input("Enter a letter a-z: ")
    if len(imp) == 1 and imp.isalpha():
        if imp not in hidden_word:
            positions = check_letter_in_word(imp)
            if positions != None:
                for pos in positions:
                    hidden_word = replacer(hidden_word, imp, pos)
                    print(f'Updated hidden word: {hidden_word}')
                check_is_alpha()
        else:
            print('you already tried this letter')

if game_done == True:
    print('you won')
    print(f'the word was: {word}')
