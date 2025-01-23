import wordgetter
import wordslistgetter

def num_val(text, mini, maxi):#input validation to make my life easier
    #input
    n = input(text)
    
    #type check
    try:
        n = int(n)
    except:
        print('ERROR: Not a number')
        return num_val(text, mini, maxi)

    #range checks
    if n > maxi or n < mini:
        print('ERROR: Not within range')
        return num_val(text, mini, maxi)

    return n

#=======ONE TIME THING==============================

def on_start():#basically settings
    wifi = num_val('Get words \n[0] Offline\n[1] Online\n',0,1)

    if wifi == 0:
        #check if txtfile exists
        try:
            with open('wordslist.txt','r') as file:
                pass
            
        except:
            #options in case txtfile does not exist
            print('ERROR: wordslist.txt does not exist')
            whatnow = num_val('[0] Generate new wordslist.txt (TAKES 4 MINUTES)\n[1] Get words online\n[2] Quit\n',0,2)

            if whatnow == 0:
                print('Please wait...')
                wordslistgetter.generate()
                
            elif whatnow == 1:
                wifi = 1
                
            else:
                quit()
                
    return wifi

#===================================================

def new_round(wifi):  
    #generate words
    if wifi == 0:
        word = wordgetter.get_word_offline()
    else:
        word = wordgetter.get_word_online()

    #important variables
    known = ['_' for _ in word]#start with the blanks

    return word, known

#===================================================

def draw():
    #draw guy
    #uses text file to draw
    with open('themanhimself.txt','r') as file:
        gallows = file.read()
        start = gallows.index(f'${7-hp}')+3
        end = gallows.index('\n$', start)

        he = gallows[start:end].splitlines()
        for i in he:
            print(i)
    #print known
    for i in known:
        print(i,end='')
    print('\n\n GUESSED: ')
    #print guessed
    for i in guessed:
        print(i, end=' ')
    print()

def guess_letter(letter, known, hp):
    #if letter is correct
    if letter in word:
        for n,i in enumerate(word):
            if i == letter:
                known[n] = i
    #if letter is wrong
    else:
        hp -= 1

    return known, hp
        

def letter_valid(guessed):
    #Get letter and validate it
    while True:
        what = input('Guess a letter: ')
        if len(what) == 1:#length check
            if what.isalpha():#type check
                what = what.upper()
                if what not in guessed:
                    break
                else:
                    print(f'You have already guessed {what}!')
                    
    guessed.append(what)
    return what, guessed

#===================================================

wifi = on_start()

while True:
    print('==============NEW ROUND==============')
    #per round
    hp = 7
    guessed = []
    word, known = new_round(0)

    while True:
        #per turn
        draw()
        letter, guessed = letter_valid(guessed)
        known, hp = guess_letter(letter, known, hp)
        #exit
        if hp == 0:
            print('YOU LOST!')
            #print word
            print('THE WORD WAS',end='')
            for i in word:
                print(i,end='')
            print('!')
            
            break
        if known == word:
            print('YOU WIN!')
            break
