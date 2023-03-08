# from turtle import Turtle, Screen
#
#
# bob = Turtle()
#
# my_screen = Screen()
# print(my_screen.canvheight, my_screen.canvwidth)
# bob.shape("turtle")
# bob.color("green")
#
# turns = 4
# while turns > 0:
#     bob.forward(100)
#     bob.left(90)
#     turns -= 1
# my_screen.exitonclick()

from prettytable import PrettyTable  # import the PrettyTable Class


table = PrettyTable(['Pokemon', 'Type'])
table.add_row(["Pikachu", "Electric"])
table.add_row(['Squirtle', 'Water'])
table.add_row(['Charmander', 'Fire'])
table.align['Pokemon'] = "l"  # to align a single column
table.align = "l"  # to align all columns in the table


print(table)









