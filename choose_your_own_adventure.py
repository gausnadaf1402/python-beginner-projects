name=input("type your name:")
print("welcome",name,"to this adventure!")

answer=input("you are on a dirt road,it has come to an end and you can go left or right. which way would you like to go? ").lower()

if answer == "left":
    answer=input("you came to a river,you can walk around it or swin accros? type walk to walk around and swim to swim accros: ")
   
    if answer == "swim":
        print("you swam accross and eaten by an alligator. ")
    elif answer == "walk":
        print("you walk for many miles, ran out of water and you lost the game.")
    else:
        print("not valid option. you lose.")

elif answer == "right":
    answer=input("you came to a bridge, it looks wobly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("you go back and lose. ")
    elif answer == "cross":
        answer=input("you cross the bridge and meet a stranger. do you talk to them (yes/no)? ")

        if answer == "yes":
            print("you talk to a stranger and they give you a gold. you WIN!")
        elif answer == "no":
            print("you ignore the stranger and they are affended and you LOSE!")
        else:
           print("not valid option. you lose.") 
    else:
        print("not valid option. you lose.")

else:
    print("not valid option. you lose.")

print("thank you for trying",name)