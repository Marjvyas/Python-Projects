import random
print("Welcome to number guessing game...")
print("In this game you have to guess any number and if you will get success in finding the number then output will display the number of guesses...")
start=int(input("Enter the lower bound number:"))
end=int(input("Enter the upper bound number:"))
key=random.randint(start,end)
passes=0
while True:
    guess=int(input("Enter your guess:"))
    if(guess<start or guess>end):
        print("Invalid number!!!")
    elif(guess<key):
        print("Too low!!!")
        passes+=1
    elif(guess>key):
        print("Too high!!!")
        passes+=1
    else:
        print("You got the number!!!")
        break
print(f"Your no. of guesses is:{passes}")