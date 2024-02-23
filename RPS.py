# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 00:19:41 2022

@author: ALFASTREK
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 23:18:50 2022

@author: ALFASTREK
"""
import random
print('Welcome to the Rock Paper scissor App!')
req1=int(input('How many round would you like to play:')) 
#total number of attempts
game=['rock','scissor','paper'] 
#giving 3 choices to user
userscore=0 #to maintain user's score
compscore=0 #to maintain computer's score
sr=0 #to denite a serial no. to every round of the game
def real1(a,b): 
    #case1 where user is supposed to win over computer
    print ('Player:',a)
    print('Computer:',b)
    print(a,'wins over', b)
    global userscore
    global compscore
    
    userscore+=1
    
    print('PLAYER:',userscore,
              'COMPUTER:',compscore,
              '\nUser wins the round!\n')
def real2(c,d): 
    #case1 where comp is supposed to win over user
    print ('Player:',c)
    print('Computer:',d)
    print(d,'wins over', c)
    global userscore
    global compscore
    compscore+=1
    print('PLAYER:',userscore,
              'COMPUTER:',compscore,
              '\nComputer wins the round!\n')
    
     
def draw(a): 
    #case 3 where its a draw
    print ('Player:',a)
    print('Computer:',a)
    print("It's a Draw, how boring!, better luck next time tho.")
    print('PLAYER:',userscore,
              'COMPUTER:',compscore,'\n')
    
        
for i in range(req1):
    comp= random.choice(game)
    sr+=1
    print(sr,')''The computer has choosen its pick!')
    user=input('Time to pick:')
    #now to write code for different cases possible
    if (user=='rock' and comp=='scissor'): 
        real1('rock','scissor')
    elif(user=='scissor' and comp=='rock'):
        real2('scissor','rock')
    elif (user=='paper' and comp=='rock'):
        real1('paper','rock')
    elif(user=='rock' and comp=='paper'):
        real2('rock','paper')
    elif (user=='scissor' and comp=='paper'):
        real1('scissor','paper')
    elif(user=='paper' and comp=='scissor'):
        real2('paper','scissor')
    elif(user==comp):
        draw(user)
    else:
        print('wrong input')
        break

def winner (a,b): #to declare the final winner
    if (a>b):
        print('User wins!')
    elif (b>a):
        print('Computer wins!')
    elif (a==b):
        print("IT'S A DRAW !")
    else:
        pass
    return ('GAME OVER')
    
    
print("Final Game results:" #to display final result
      "\t\tRounds Played:",req1,
      '\t\tPlayer Score:',userscore,
      '\t\tComputer Score:',compscore,
       winner('userscore','compscore'))

      
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
