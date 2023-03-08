''' 
Write a program that converts student scores to grades. The final version of the student_grades dictionary will be checked.

This is the scoring criteria:

Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail
'''
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
#TODO By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. 
student_grades = {}

for name, score in student_scores.items():
    if score > 90:
        student_grades[name] = 'outstanding'
    elif score > 80:
        student_grades[name] = 'exceeds expectations'
    elif score >= 70:
        student_grades[name] = 'acceptable'
    else:
        student_grades[name] = 'needs work'

print(student_grades)
