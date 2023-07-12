#CODE HERE
from random import Random, randint


start=int(input("Enter the range of the numbers\nfrom : "))
end=int(input("to: "))
val=randint(start,end)
flag=1
while flag!=0 :
    guess=int(input("Enter the value :"))
    if guess < val :
        print("Try again !! The guess made is too low")
    elif guess > val :
        print("Try again !! The guess made is too high")
    else :
        print("The guess made is correct to the system selected random val",val)
        flag-=1
