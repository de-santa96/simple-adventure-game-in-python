# a print statement in python 
print("Welcome to my first game!!")

# taking input from standard input
name = input("What is your name? ")

# converts the input string to an integer   
age = int(input("What is your age? "))

# initial health of the player
health = 10

# main logic of the program starts from here
# simple if-elses to decide the fate of the player
if age >= 18:
    print("You are old enough to play!!")
    
    wants_to_play = input("Do you want to play? ").lower()
    
    if(wants_to_play == "yes"):
        print("You are starting with", health, "health")
        print("Let's play!!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        
        if left_or_right == "left":
            ans = input("Nice... You follow the path and reach a lake... Do you swim across or go around (across/around)? ").lower()

            if ans == "across":
                print("You managed to get across but were bit by a fish and lost 5 health.")
                health -= 5
            elif ans == "around":
                print("You went around and reached the other side of the lake.")

            ans = input("You notice a house and river. Which do you go to? (river/house) ")

            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lost 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lose the game...")
                else:
                    print("You have survived... You win!!")
            else:
                print("You fell in the river and lost...")
        
        else:
            print("You fell down and lost...")


    else:
        print("Cya...")

elif age >= 14:
    print("You can play with supervision")

else:
    print("You are not old enough to play...")
