#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 13:43:14 2022

@author: hujiujiu
"""

import random
import math
from gtts import gTTS

def addition (num,level):
    problem=[]

    while len(problem)<num :
        adder1=random.randint(1,level)
        adder2=random.randint(1,level)

        if adder1+adder2 > level:
            pass
        else:
            problem.append([str(adder1) + '+' + str (adder2) + '=' , adder1+adder2])

    return problem


def subtraction (num,level):
    problem=[]

    while len(problem)<num :
        sub=random.randint(2,level)
        subtractor=random.randint(0,level)

        if sub==subtractor:
            continue
        if subtractor > sub :

            sub,subtractor=subtractor,sub


        problem.append([str(sub) + '-' + str (subtractor) + '=' , sub-subtractor])

    return problem

def multiplication (num,level):
    problem=[]

    while len(problem)<num :
        mul1=random.randint(2,level)
        mul2=random.randint(2,level)


        problem.append([str(mul1) + 'x' + str (mul2) + '=' , mul1*mul2])

    return problem


def division (num,level):
    problem=[]

    while len(problem)<num :
        mul1=random.randint(2,level/2)
        mul2=random.randint(2,level/2)

        if mul1 * mul2 > level:
            pass
        else:

            problem.append([str(mul1*mul2) + chr(247) + str (mul1) + '=' , mul2])

    return problem

def GCD (num,level):
    problem=[]
    if level<50:
        level=50
    while len(problem) < num:
        num1=random.randint(10,level)
        num2=random.randint(10,level)


        problem.append([f'the greatest common divisor of {num1} and {num2} =',math.gcd(num1,num2)])

    return problem

def LCM (num,level):
    problem=[]

    while len(problem) < num:
        num1=random.randint(10,level)
        num2=random.randint(10,level)


        problem.append([f'the least common multiple of {num1} and {num2} =',abs(num1*num2) // math.gcd(num1, num2)])

    return problem

def CRP (num,level):
    problem=[]

    while len(problem) < num:
        num1=random.randint(2,level)
        num2=random.randint(2,level)


        problem.append([f'There are {num1+num2} chicken and rabbit in the cage, in total they have {num1*2+num2*4} legs, rabbit=', num2])

    return problem


def Sequence (num,level):
    problem=[]
    rules=['cd','cm','cd','dcd','cd','cm','cd','cd','mcd','cd','fn',]
    
    while len(problem) < num:
        seq=[]
        seq.append(random.randint(1,10))
        
        rule=random.choice(rules)
        
        if rule=='cd':
            diff=random.randint(1,5)*random.choice([1,-1])
            for i in range(5):
                seq.append(seq[-1]+diff)

        elif rule=='cm':
            diff=random.randint(1,5)
            for i in range(5):
                seq.append(seq[-1]*diff)
     
        elif rule=='dcd':
            diff=random.randint(1,5)*random.choice([1,-1])
            diff2=random.randint(1,2)*random.choice([1,-1])
            for i in range(5):
                seq.append(seq[-1]+diff)
                diff+=diff2

        elif rule=='mcd':
            diff=random.randint(1,3)
            diff2=random.randint(0,2)
            for i in range(5):
                seq.append(seq[-1]*diff)
                diff+=diff2
            
        elif rule=='fn':
            diff=random.randint(-5,5)*random.choice([1,-1])
            seq.append(diff)
            for i in range(5):
                seq.append(seq[-1]+seq[-2])
        
        
        i=random.randint(0,4)
        ans=seq[i]
        seq[i]='( )'
        seq.append(' , ... =')
        problem.append([' , '.join(map(str, seq)),ans])    

    return problem

def spelling(num,level):
    
    problem=[]
    
    with open ('static/words.txt','r') as f:
        words=f.read().splitlines()
    
    test_words=random.sample(words,num)
    
    for i in range(len(test_words)):
        problem.append([test_words[i]+'=',test_words[i]])
        gTTS(test_words[i]).save(f"static/{test_words[i]}.mp3")
    
    
    return problem
    
    
    
    
