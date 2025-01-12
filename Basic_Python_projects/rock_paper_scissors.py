import random
options=('Stone','Paper','Scissors')
your_choice=None
key=random.choice(options)
while your_choice not in options:
    your_choice=input("Enter your choice(stone,paper,scissors) and q to quit:")
    print(f"Result:\nyour choice  :  {your_choice}\ncomputer choice  :  {key}")
    if(your_choice.lower()=='q'):
        break
    elif(your_choice.capitalize()==key.capitalize()):
        print("It's Tie!!!")
    elif((your_choice.capitalize()=='Stone' and key.capitalize()=='Scissors') or (your_choice.capitalize()=='Paper' and key.capitalize()=='Stone') or (your_choice.capitalize()=='Scissors' and key.capitalize()=='Paper')):
        print("You won!!!")
    else:
        print("You lose the game")