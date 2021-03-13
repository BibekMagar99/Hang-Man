# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:54:33 2021

@author: bibek
"""
import random
import string
#tala alphabets load garna lai use vako
from words import words
#print(word_list)
    
def word_selection(words):
    word = random.choice(words) 
    #esle chai word_list bata random words select garcha
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.upper()
#so yo function le chai paila word vanne variable ma random word assign garcha and if tyo word ma - or space cha vane chai feri naya word khojera halcha.

def Five():
    print("+--------+")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print(" =========")
    print("")
    
    
def Four():
    print("+-------+")
    print("|       |")
    print("|      ( )")
    print("|      ")
    print("|       ")
    print("|      ")
    print("|")
    print(" =========")
    
def Three():
    print("+-------+")
    print("|       |")
    print("|      ( )")
    print("|       |")
    print("|       |")
    print("|      ")
    print("|")
    print(" =========")
    
def Two():
    print("+-------+")
    print("|       |")
    print("|      ( )")
    print("|      /|\  ")
    print("|       |")
    print("|      ")
    print("|")
    print(" =========")
    
def One():
    print("+-------+")
    print("|       |")
    print("|      ( )")
    print("|      /|\     last Chance")
    print("|       |")
    print("|      / ")
    print("|")
    print(" =========")
    
def Dead():
    print("+-------+")
    print("|       |")
    print("|      ( )")
    print("|      /|\      D E A D !!!!")
    print("|       |")
    print("|      / \  ")
    print("|")
    print(" =========")
      
def hangman():
    word = word_selection(words)
    #randomly select words from the list 
    word_ko_letters = set(word)
    #converts the word into set...."bibek" cha vane {b,e,i,k} bancha
    #saves the word inn word letters as a set
    uppercase_alphabets = set(string.ascii_uppercase)
    #uppercase_alphabets vanne ma all upper case ko character haru set banayera rakhcha
    used_letters = set()
    #used letters ma empty set rakhako
    lives = 6
    
    #aaba user sanga input line:
    while len(word_ko_letters) > 0 and lives > 0:
        print("you have :", lives, "lives left. choose the letters wisely!")
        if lives == 5:
            Five()
        elif lives == 4:
            Four()
        elif lives == 3:
            Three()
        elif lives == 2:
            Two()
        elif lives == 1:
            One()
       
        #print(current_lives)
        print("you have already used : " ," ".join(used_letters))
        word_to_show_in_the_screen = [letter if letter in used_letters else "_" for letter in word]
        #it replaces the letter in the word if it is in used and replaces with _ if not used
        print("current Word : ", " ".join(word_to_show_in_the_screen))
        user_letter = input("Guess a letter : ").upper()
        if user_letter in uppercase_alphabets - used_letters :
            #yo chai used letters lai alphabet bata minus/remove gareko,   i.e if a use vaisakeko cha vane a is removed from alphabets
            used_letters.add(user_letter)
            if user_letter in word_ko_letters :
                word_ko_letters.remove(user_letter)
            else :
                lives = lives -1 
                print("The input letter", user_letter, "is not in the word")
                if lives == 0:
                    Dead()
                
                
        elif user_letter in used_letters:
            print("Already Used")
            
        else :
            print("please input a valid character, i.e String!")
            
    if lives == 0:
        print("sorry you failed, Please try again")
        print("The Word was :", word )
    else :
        print("Congratulations !! you've guessed the word, ", word)
        
hangman()