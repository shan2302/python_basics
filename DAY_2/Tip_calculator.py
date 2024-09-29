print("Welcome to the tip calculator. ")
bill = float(input("What was the total bill?  ₹"))
person= float(input("How many people to split the bill? "))
tip= float(input("What percentage tip would lie to give ? 10, 12,or 15? "))

total_bill = bill + (tip/100)*bill
split_bill = round(total_bill/person,2)

print("Each person should pay: ₹",split_bill)