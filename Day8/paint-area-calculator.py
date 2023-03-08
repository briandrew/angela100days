''' 
You are painting a wall. 
1 can of paint can cover 5 square meters of wall. 
Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.
e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 * 4) / 5 = 1.6

But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

'''
import math # in order to use math ceiling to round number of cans need up

def paint_needed(height,width,coverage):
    area = height * width
    return math.ceil(area/coverage)

print()
print("How much paint do you need? ")

height = float(input("Enter height of the wall: "))
width = float(input("Enter width of the wall: "))
paint_coverage = 5


print(f"You need {paint_needed(height,width,coverage=paint_coverage)} cans of paint")

