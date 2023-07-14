from random import Random, randint
my_dict = {
    'tiger' : 'Striped animal, orange',
    'lion' : 'King',
    'Camel' : 'Dessert',
    'am' : 'My best friend',
    'Cow' : 'Sacared one',
    'goat' : 'bakara , another name of sam fyi',
    'ictoae' : 'I cannot think of anything else'
        }
end = len(my_dict)
i = randint(0,end-1)
keys = list(my_dict.keys())
chose_by_system = keys[i]
flag = 1
count = 0
hint = 0
print("These are the animals available in the system :")
print(keys)
print("The Animal Guessing Game starts here!!")
while flag!=0:
    if hint == 1:
        value= list(my_dict.values())
        print(value[i])
        hint = 0
    chose_by_user = input("Enter the animal: ")
    if chose_by_system==chose_by_user:
        print("Yay!! you got it right!")
        flag = 0
    else:
        print("Sorry!! try again")
    count = count + 1
    if count >= 3 and flag!=0:
        get= input("DO you want a hint? ,press y/n:")
        if get == 'y' or get == 'Y':
            hint = 1
        else :
            hint = 0
    

