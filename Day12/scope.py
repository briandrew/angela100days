

enemies = 1
# global scope
player_health = 10


def increase_enemies():
    global enemies  # added after the fact to access the 'enemies' in the global scope
    # avoid global calls like this, don't modify within a function, use return statements
    enemies = 2  # local scope variable within the function only
    print(f"enemies inside functions: {enemies}")
    return enemies + 1  # which now is able to change the globaly 'enemies'

increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope exists within functions
def drink_potion():
    potion_strength = 2
    print(potion_strength)
    print(player_health)

drink_potion()
print(potion_strength) # can't print because potion_strength locally scoped within the function

# Global Constants - where it's ok to use globally scoped variables - use variable names in UPPER
# examples
PI = 3.14159
URL = thedrews.com