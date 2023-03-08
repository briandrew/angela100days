# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#TODO It should take your current age as the input and output a message in this format:

# "You have 12410 days, 1768 weeks, and 408 months left."



print("Let's calculate weeks in your life until you are 90!")
age = int(input("Please enter your current age: "))
years_remaining = 90-age
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months remaining in your life")
