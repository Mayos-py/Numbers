import random

x=int(input("How many games you want to play: "))

num= random.randint(1,25)
count=0
for i in range(x):
    y = int(input("Select random number between 1-25: "))
    count += 1
    if y == num:
        print("Congrats!! You guessed it correctly")
        print("You guessed it in {} attempts".format(count))
        break
    elif y > num:
        print("The number is less than this")
    elif y < num:
        print("The number is greater than this")
    
if(x==count):
    print("You have played {} games ".format(x))


    

        
