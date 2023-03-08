'''
write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

'''
import random
print()
print("Welcome to virtual coin flip")
pick = input("Do you pick 'heads or 'tails'? : ")
print("computer is flipping......")
flip = random.randint(0, 1)
result = ''
if flip == 0:
    result = 'tails'
else:
    result = 'heads'

if pick == 'tails' and result == 'tails':
    print(f"Congratulations - you picked {pick} and the computer flipped {result}")
 
elif pick == 'heads' and result == 'heads':
    print(f"Congratulations - you picked {pick} and the computer flipped {result}")

else:
     print(f"Sorry, you picked {pick} but the computer flipped {result}")

