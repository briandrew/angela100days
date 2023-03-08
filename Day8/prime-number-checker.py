''' 
determine if any give number is a prime or not
'''
def prime_number(n):
    if n %2 == 0 or n % 3 == 0:
        return False
    
    else:
        return True

number = int(input("Please enter a whole number to check for primeness: "))

true_false = prime_number(n = number)

if not true_false:
    print("number not prime")
else:
    print("number is prime")