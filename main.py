import random
from collections import Counter


def Checker(guess,answer):
  checker=[0,0,0,0,0]
  for i in range(5):
    if guess[i]==answer[i]:
      checker[i]=20
    elif guess[i] in answer:
      checker[i]=1
  return(checker)


attempts=0
guesses=0

checker=[0,0,0,0,0]
green={}
yellow=[]
red=[]


f=open("words.txt","r")
file=f.readlines()
words=[]

for word in file:
  words.append(word.strip())

#answer=random.choice(words)
answer=input("answer: ")
guess=input("Enter a word: ")
attempts+=1
guesses=1
while checker!=[20,20,20,20,20]:
  print("Guess", guess)
  
  #print(checker)
  checker=[]
  #for i in range(5):
    #checker.append(int(input("Enter number: ")))

  checker=Checker(guess,answer)

  for i in range(len(checker)):
    if checker[i]==20:
      green.update({i:guess[i]})
    if checker[i]==1:
      yellow.append(guess[i])
    if checker[i]==0:
      red.append(guess[i])

  
  valid_words=[]
  
  for word in words:
    valid=True
    for placement in green:
      if word[placement]!=(green[placement]):
        valid=False

    for letter in yellow:
      if letter not in word:
        valid=False
          
    for letter in red:
      if letter in word:
        if word in words:
          valid=False
    if valid:
      valid_words.append(word)

  words=valid_words
  guess=random.choice(words)
  
  if checker==[20,20,20,20,20]:
    print(guesses, answer)
    break
  guesses+=1
