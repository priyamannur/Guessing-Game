import random
import string
animal_list = ["lion" ,"tiger" ,"hippopotomus"]
chose_by_system = random.choice(animal_list)
flag = 1
while flag!=0:
    print("The Animal Guessing Game starts here!!")
    chose_by_user = input("Enter the animal: ")
    if chose_by_system==chose_by_user:
        print("Yay!! you got it right!")
        flag = 0
    else:
        print("Sorry!! try again")
