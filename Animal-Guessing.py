import random
chose_by_system = random.choice(open("animals.txt","r").read().split())
flag = 1
print("The Animal Guessing Game starts here!!")
while flag!=0:
    chose_by_user = input("Enter the animal: ")
    if chose_by_system==chose_by_user:
        print("Yay!! you got it right!")
        flag = 0
    else:
        with open("animals.txt","a") as file:
            file.write(chose_by_user)
        print("Sorry!! try again")

