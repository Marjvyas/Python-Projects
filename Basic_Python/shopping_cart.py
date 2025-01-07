Menu={'Apple':60,
        'Banana':50,
        'Orange':80,
        'Grapes':40,
        'Pineapple':60}
total=0
cart=[]
for key,value in Menu.items():
    print(f"{key:10}:{value} rupees/kg")
while True:
    choice=input("Enter your item(q to quit):")
    if choice.lower()=='q':
        break
    elif choice.capitalize() not in Menu.keys():
        print("Item not found!!!")
    else:
        cart.append(choice)
        total+=Menu.get(choice.capitalize())
print("-----Your Cart-----")
for i in cart:
    print(i)
print(f"Total rupees is:{total}")