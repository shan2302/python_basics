print("Welcome to Python Pizza Deliveries!")
print("SMALL PIZZA:  $15")
print("MEDIUM PIZZA: $20")
print("LARGE PIZZA:  $25")
size = input("What size pizza do you want? S,M or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size == "S":
    if add_pepperoni=="Y":
        if extra_cheese == "Y":
            print("Your Bill is $18")
        else:
            print("Your Bill is $17")
    elif extra_cheese =="Y":
        print("Your bill is $16")
    else:
        print("Your Bill is $15")
elif size == "M":
    if add_pepperoni=="Y":
        if extra_cheese == "Y":
            print("Your Bill is $24")
        else:
            print("Your Bill is $22")
    elif extra_cheese == "Y":
        print("Your bill is $21")
    else:
        print("Your Bill is $20")
elif size=="L":
    if add_pepperoni=="Y":
        if extra_cheese == "Y":
            print("Your Bill is $29")
        else:
            print("Your Bill is $28")
    elif extra_cheese == "Y":
        print("Your Bill is $26")
    else:
        print("Your bill is $25")
else:
    print("You can only select S,M,L")