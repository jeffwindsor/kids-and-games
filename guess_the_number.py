import random

guessesTaken = 0
number = random.randint(1,20)

print('Hello! What is your name?')
name = input()
print('Welcome ' + name + '. I am thinking of a number between 1 and 20.')

for guessesTaken in range(4):
  print('Take a guess.')
  guess = int(input())
  if guess == number:
    print('Your guess is correct.')
    break
  if guess < number:
    print('Your guess is to cold.')
  if guess > number:
    print('Your guess is to hot.')

if(guess==number):
  print('Good job, you won ', name)
else:
  print('Better luck next time ', name)