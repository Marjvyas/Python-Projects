import random
objects=('*','$','@')
total_amount=100
print(f"You have {total_amount} rupees.")
print(f"In this game you have to pay 5 rupees per spin and then you will earn 10 rupees on each win")
while True:
    a=int(input("Enter 1 to spin and 0 to quit."))
    if a:
        total_amount-=5
        b,c,d=random.choice(objects),random.choice(objects),random.choice(objects)
        print(b,c,d)
        if b==c==d:
            print("Congratulations!!!   You won 10 rupees")
            total_amount+=10
        else:
            print("You Lose the game...")
        print(f"Your total amount:{total_amount}")
    elif a==0:
        break
    else:
        print("Enter valid choice...")
print("Your Status:")
if(total_amount>100):
    print("You are in profit...")
    print(f"You have earned {total_amount-100} rupees")
else:
    print(f"You lose {100-total_amount} rupees out of 100")