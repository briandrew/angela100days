''' 
test the compatibility between two people

To work out the love score between two people:

1. Take both people's names and check for the number of times the letters in the word TRUE occurs. 

2. Then check for the number of times the letters in the word LOVE occurs. 

3. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is **z**."
'''

# after the fact learned from Angela that a better approach is to combine the names into 1 string " to simplify the checking
print()
print("Welceom to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

true_count = 0
love_count = 0

true_count += name1.count('t')
true_count += name1.count('r')
true_count += name1.count('u')
true_count += name1.count('e')

true_count += name2.count('t')
true_count += name2.count('r')
true_count += name2.count('u')
true_count += name2.count('e')

love_count += name1.count('l')
love_count += name1.count('o')
love_count += name1.count('v')
love_count += name1.count('e')

love_count += name2.count('l')
love_count += name2.count('o')
love_count += name2.count('v')
love_count += name2.count('e')

love_calculation = str(true_count) + str(love_count)

love_calculation = int(love_calculation)

if love_calculation <10 or love_calculation > 90:
    print(f"Your score is {love_calculation}, you go together like coke and mentos.")
elif love_calculation >=40 and love_calculation <= 50:
    print(f"Your score is {love_calculation}, you are alright together.")
else:
    print(f"Your score is {love_calculation}")
