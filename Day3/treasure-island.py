print(''' 
************************* Welcome to Treasure Island **************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************

''')

def left (swim):
    
    if swim_walk == 'swim':
        print('Sorry, you were attacked by trout, game over')
        
    

print("You just landed on the island. There is a path going left and a path going right.")
path = input("Which do you take - 'left' or 'right'? ").lower()
if path == 'left':
    swim_walk = input("You come to a lake, do you swim across or walk around? - swim or walk: ").lower()
    if swim_walk == 'swim':
        left(swim)
    elif swim_walk == 'walk':
        print("Good choice, you continue on and come to a house with 3 doors.")
        
   
elif path == 'right':
    print("You come to a fork in the path, one way goes left, the other right.")
    left_right = input("Which way do you go - left or right: ")
    if left_right == 'left':
        swim_walk = input("You come to a lake, do you swim across or walk around? - swim or walk: ").lower()
        if swim_walk == 'swim':
            left(swim_walk)
        elif swim_walk == 'walk':
            print("Good choice, you continue on")
    elif left_right == 'right':
        print("You continue on and come to a house with 3 doors.")

print("You enter the cave")



    
        
