''' 

'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print()
choice = input("Which do you choose? 'rock', 'paper', or 'scissors'? ").lower()

if choice == 'rock':
    print(f"You chose {choice}:\n {rock}")
    choice = 0
elif choice == 'paper':
    print(f"You chose {choice}:\n {paper}")
    choice = 1       
elif choice == 'scissors':
    print(f"You chose {choice}:\n {scissors}")
    choice = 2    
else:
    print("you did not enter rock, paper or scissors")

computer_pick = random.randint(0,2)
if computer_pick == 0:
    print(f"The computer picked rock:\n {rock}")
elif computer_pick == 1:
    print(f"The computer picked paper:\n {paper}")
else:
    print(f"The computer picked scissors:\n {scissors}")

if choice == 0 and computer_pick == 1:
    print("Paper covers rock - you win!")
elif choice == 0 and computer_pick == 2:
    print("Scissors cuts paper - you  lose!")
elif choice == 1 and computer_pick == 0:
    print("Paper covers rock - you lose!")
elif choice == 1 and computer_pick == 2:
    print("Rock smashes scissors - you win!")
elif choice == 2 and computer_pick == 0:
    print("Scissors cuts paper - you win!")
elif choice == 2 and computer_pick == 1:
    print("Rock smashes scissors - you lose!")
else:
    print("Tie! Play again")









