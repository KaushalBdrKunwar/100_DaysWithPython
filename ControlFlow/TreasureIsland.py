print(r'''
   ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`

''')

print("Welcome to Treasure Island.")
print("Your Mission is to find treasure.")

direction = input("type left or right?").lower()

if direction == 'left':
    choice = input("You have come to the lake. Type wait to wait for boat or type swim? ").lower()

    if choice == 'wait':
        choice1 = input("You have red, blue and yellow door select one: ").lower()

        if choice1 == 'yellow':
            print("You won")
        elif choice1 == 'red':
            print("You lose")
        elif choice1 == 'blue':
            print('You lose!')
        else:
            print("Door don't exist wrong!")
    else:
        print("You drowned.Game Over")
else:
    print("You fall into the hole. Game Over")
