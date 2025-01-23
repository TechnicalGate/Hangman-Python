# Hangman-Python
## This is hangman in python.

## How to play
To start the game, run game.py

## What the other files do
wordgetter.py contains functions called by game.py when a word is chosen.

wordslistgetter.py uses webscraping to scrape Merriam Webster dictionary for words, then creates and adds the words to wordslist.txt

wordslist.txt is a list of all valid words without spaces, sourced from the Merriam Webster dictionary, and is used when choosing words offline.
If you want to add your own words, edit to wordslist.txt, with each line containing exactly 1 word.

themanhimself.txt contains the ASCII art displayed when letters are incorrectly guessed. 
If you wish to edit the ASCII art, do not remove the $ or the numbers (e.g $0), as that is how the program seperates each art.

## Why I made this
I wanted to learn and practice using Python for web scraping while also coding something fun and functional with the data. I chose hangman as I had previously tried to code the game and could reuse some code from my previous attempt. This allowed me to focus more on the webscraping aspect, the part I wanted to learn and do.
