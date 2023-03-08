print("Welcome to the ride!")
height = int(input("Are you tall enough? What is  your height in cm? "))



def age_cost (age):
    cost = 0
    if age < 12:
        cost = 5
    elif age <= 18:
        cost = 7
    else:
        cost = 12
    return cost

    
if height >= 120:
    print("You are tall enough to ride!")
    age = int(input("And how old are you? "))
    sub_total = age_cost(age)
    print(f"Your sub total is ${sub_total}.")
    picture = input("Would you like a photo taken with your ride?")
    if picture == 'yes' or picture == 'y':
        total = sub_total + 3
    else:
        total = sub_total
    print(f"Your total is ${total}.")
else:
    print("Sorry but you are too short to ride.") 