	# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random as rd
file = open('word.txt','r')
r=rd.randrange(0,100,1)
word = None
for x in range(100):
    if x == r:
        word=file.readline()
    else:
        file.readline()
        
#print(word)
#print(len(word))
word = word.lower()
attempt=2*(len(word)-1) 
for i in range(len(word)-1):
    print(f"_ ",end='')
print()
temp = []
flag = False
while attempt!=0:
    print(f"You have {attempt} attempts to guess the word")
    ch = input("Enter a character: ")
    print(ch)
    if ch in temp:
        print(f"You have already guessed {ch}")
        continue
    temp.append(ch)
    print (temp)
    count=0
    f=False
    for i in range(len(word)-1):
        if word[i] in temp:
            print(f"{word[i]} ",end='')
            f=True
        else:
            count =count+1
            print("_ ",end='')

        
    print()
    
    if count==0 and f==True:
        print(f"You guessed in {len(temp)} attempts")
        flag = True
        break
    
    attempt=attempt-1

if flag == False:
    print(f"You Lost the game,Better Luck next time Word: {word}")
else:
    print("Congrats !!! You Win")

file.close()

