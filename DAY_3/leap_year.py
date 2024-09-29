year = int(input("Which year do you want to chcek?"))

if year%4==0 and (year %100 !=0 or year %400 ==0):
    print(f"your year {year} is a leap year")
else:
    print(f"your year {year} is a not a leap")