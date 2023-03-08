''' 
write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Do not use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x

Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]

Example Output
The highest score in the class is: 91

Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?

'''
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# 🚨 Don't change the code above 👆
#Write your code below this row 👇

high_score = 0
for score in student_scores:
    if score > high_score:
        high_score = score
print(f"The high score in the class is: {high_score}")
