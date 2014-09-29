# program written by Sue Sentance and edited by robert fox
import random
import time

def main():
    turns_left = random.randint(1,10) # selects a random number of turns before the end is reached
    turns_to_do = turns_left
    print("You are trying to find your way through a maze to the centre where ")
    print("there is a pot of gold!")
    print("What you don't know is that this is a dangerous maze with traps and hazards.")
    print()
    print("Starting maze game ...")
    print()
    print("You enter the maze...")
    time.sleep(1) # time.sleep is just used to build up the suspense!
    print("You reach a opening in the wall and go through it...")
    print()
    while turns_left > 0:
        time.sleep(1)
        print("You can go left or right")
        answer = input("Make your choice ... ")
        if answer == "r" or "R" or "Right" or "right" or "starboard" or "not left":
            answers = "R"
        else:
            answers = "L"
        print("You chose",answer,"... what will happen? ...")
        time.sleep(1)
        print("You turn the corner...")
        time.sleep(1)
        print("You walk forward a few steps...")
        time.sleep(1)
        right_way = random.choice(["R","L"]) 
        if right_way == answers:
            turns_left = (turns_left-1)
            print("You find yourself at another turn...")
            print(turns_left) # debug code to see turns left to do
        else:
            turns_comp = (turns_to_do-turns_left) 
            turns_left = 0
            print("...and fall down a trap door and are never seen again....")
            print("You survived {0} turns".format(turns_comp,))
    print("You found the gold pot! well done!")
    print("It took you {0} turns to get there!".format(turns_left,))

    # end of program
    
    
    
    
    
