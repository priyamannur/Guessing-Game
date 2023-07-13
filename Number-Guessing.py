from random import Random, randint

start=int(input("Enter the range of the numbers\nfrom : "))
end=int(input("to: "))
val=randint(start,end)
flag=1
while flag!=0 :
    guess=int(input("Enter the value :"))
    if (guess - val) <= -15 :
        print("Try again !! The guess made is too low")
    elif (guess < val):
        print("CLose enough ,Try again!! The guess made is low")
    elif (guess - val) >= 15 :
        print("Try again !! The guess made is too high")
    elif (guess > val):
        print("CLose enough ,Try again!! The guess made is high")
    elif (guess - val)==0  :
        print("Woohoooo!! The guess made is correct! It matches the value chose by the system:",val)
        flag-=1
