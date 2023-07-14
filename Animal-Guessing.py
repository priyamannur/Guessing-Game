import random
chose_by_system = random.choice(open("animals.txt","r").read().split())
flag = 1
print("These are the animals available in the system :")
print([line.strip() for line in open("animals.txt")])
print("The Animal Guessing Game starts here!!")
while flag!=0:
    chose_by_user = input("Enter the animal: ")
    if chose_by_system==chose_by_user:
        print("Yay!! you got it right!")
        flag = 0
    else:
        print("Sorry!! try again")

