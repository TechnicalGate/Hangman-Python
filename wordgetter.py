import random

import wordslistgetter as getter

def get_word_online():
    #set up link to pick random from
    letter = chr(random.randint(ord('a'), ord('z')))#random lowercase letter for link
    num = getter.get_page_nums(f"https://www.merriam-webster.com/browse/thesaurus/{letter}/1")
    link = f"https://www.merriam-webster.com/browse/thesaurus/{letter}/{num}"

    #get random word
    wordslist = getter.get_words(link)
    word = random.choice(wordslist)

    #make it a list
    word = list(word)

    return word

def get_word_offline():
    #read wordslist.txt and take word from there
    with open(r'wordslist.txt') as file:
        f = file.readlines()
        word = random.choice(f)
        word = word.replace('\n','')

    #make it a list
    word = list(word)
  
    return word

