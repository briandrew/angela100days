'''
automatic pizza order program - Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1

'''

bill = 0

pizza_size = input("Would you like a small, medium, or large? S, M, L: ").capitalize()
if pizza_size == 'S':
    bill += 15
elif pizza_size == 'M':
    bill += 20
elif pizza_size == 'L':
    bill += 25
else:
    print("Please select small, medium, or large - S, M, L: ")

extra_pepperoni = input("Would you like extra pepperoni on that? Y/N: ").capitalize()
if extra_pepperoni == 'Y':
    if pizza_size == 'S':
        bill += 2
    else:
        bill += 3

extra_cheese = input("Would you like extra cheese? Y/N: ").capitalize()
if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is ${bill}.")
