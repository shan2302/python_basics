print("WELCOME TO ROLLER COASTER!")
height = float(input("Enter your height(in cm)"))

if(height>=120.00):
    print("You are eligible to go inside the roller coaster")
    age = int(input("What is your age?"))
    if 12<age<=18:
        bill=7
        print("Please pay $7")
    elif age<=12:
        bill=5
        print("Please pay $5")
    else:
        bill=12
        print("Please pay $12.")
    wants_photo=input("You want the photos Y or N")
    if wants_photo == "Y":
        bill =bill+3
        print(f"Your total bill is {bill}")
else:
    print("You are not eligible to go inside the roller coaster")