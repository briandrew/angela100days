''' 
write a program that calculates the average student height from a List of heights.

e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g.

180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights so 1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Do not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

Example Input
156 178 165 171 187

'''
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(',') #depending if entry separated by comma or space

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

height_total = 0
number_of_heights = 0
for height in student_heights:
    height_total += height
    number_of_heights += 1

avg_height = round(height_total / number_of_heights)

print(avg_height)





