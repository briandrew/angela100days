############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):  # was (1,20) at first which does not include 20 so increased to 21
#     print(i)
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]  # ofcourse list indexing starts at 0 and this one 
# goes to 5
# dice_num = randint(0,5)  # was (1,6) to start so changed to (0,5) as randint includes both 
# # endpoints
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")
# else:
#     print("You are old")

# # Fix the Errors
# age = int(input("How old are you?"))  # did not start as an int, I added that
# if age > 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# print(pages)
# print(word_per_page)

# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#         print(b_list)
#     print(b_list)
# mutate([1,2,3,5,8,13])

# number = int(input("Enter a number to check: "))
# if number % 2 == 0:
#     print("This is even.")
# else:
#     print("This is odd")

year = int(input("What year to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year!")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")