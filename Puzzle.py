#! /usr/bin/env python3 # coding: UTF-8 
# this is a shitty code 

import os, sys  
import numpy as np 
# Crypto 
from cryptography.fernet import Fernet 
# Sound 
from playsound import playsound
# key 
#key = Ferent.generate_key() 


# opening the responsible files, I think i do need a better method! 
prompts_count1 =  sum(len(files) for _, _, files in os.walk(r'Prompts/challenge1/'))
prompts_count2 =  sum(len(files) for _, _, files in os.walk(r'Prompts/challenge2/'))
answers_count1 = sum(len(files) for _, _, files in os.walk(r'Prompts/answer1/')) 
answer_count2 =  sum(len(files) for _, _, files in os.walk(r'Prompts/answer2/'))  

answers1 = ["a", "b", "c","45"] 
e = len(answers) 
# Puzz1 
def puzz1(): 

    i = 1 
    l = 1 
    c = 0 
    score = 0 
    for j in range(prompts_count) : 
          pp = open ("Prompts/challenge1/p"+ str(i) +".txt","r") 
          # opening answers was here   
          i = i + 1 
          answer = input(pp.read() )
          aa = open ("Prompts/answer1/a" + str(i) +".txt", "r") 
          for k in range (e): 
                if answer == answers1[c]: 
            
                    score += 1 
                    c = c + 1 
                elif answer != answers1[c]: 
                     pass
                 elif answers1[c] > len(answers): 
                      break
                else: 
                    pass
    print('Your score is =',score)     

# Puzz2 
def puzz2():

    i = 1 
    l = 1 
    c = 0 
    score = 0 
    for j in range(prompts_count) : 
          pp = open ("Prompts/challenge2/p"+ str(i) +".txt","r") 
          # opening answers was here   
          i = i + 1 
          answer = input(pp.read() )
          aa = open ("Prompts/answer2/a" + str(i) +".txt", "r") 
          for k in range (e): 
                if answer == answers[c]: 
                    score += 1 
                    c = c + 1 
                elif answer != answers[c]: 
                    pass
                elif answers[c] > len(answers): 
                    break
                else: 
                    pass
    print('Your score is =',score)    
    

def main(): 
    try:
        puzz1() 
        letter = "test"
        print(letter, end='')  
        playsound('noahark.mp3') 
    except: 
        print("What are you doing?") 
    # i need an errors handler over here 

import glob
import errno
prompts_count1 =  sum(len(files) for _, _, files in os.walk(r'Prompts/'))
fc = 0 
for i in range(prompts_count1): 
    path ='/home/mohamed/Desktop/projects/NoahArk/Prompts/challenge[i]/*.txt' #note C:

    files = glob.glob(path)
    for name in files:
        try:
            with open(name) as f:
                for line in f:
                    print(line.split())
                fc+=1
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise






) 
