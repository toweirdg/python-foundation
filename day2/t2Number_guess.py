#pick a random number
#user guesses
#program responds:
#too high
#too low
#correct
import random
target=random.randint(1,100)

print('Guess a Number :')
num=int(input())

while target!=num:
  if num<target:
    print('Too Low')
  elif num>target:
    print('Too High')

  num=int(input("Try Again :"))
print("Correct!")