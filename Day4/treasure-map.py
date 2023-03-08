''' 
write a program that will mark a spot with an X. In the starting code, you will find a variable called map. This map contains a nested list. When map is printed this is what the nested list looks like:

[['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

Your job is to write a program that allows you to mark a square on the map using a two-digit system. 

The first digit in the input will specify the column (the position on the horizontal axis).

The second digit in the input will specify the row number (the position on the vertical axis). 

So an input of 23 should place an X at the position shown below:

'''

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# put my code here
# can print out map to see the lists side by side
# print(map)
row = int(position[0]) # index the input string postion 0
column = int(position[1])

map[int(position[0])-1][int(position[1])-1] = ' x'



# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")