print("Welcome to the Love Calculator!")
name1 = input("What is your Name? \n")
name2 = input("What is his/her Name? \n")
first_Name = name1.lower()
second_Name = name2.lower()
#TRUE 
count_T1 = int(first_Name.count("t"))
count_T2 = int(second_Name.count("t"))
count_R1 = int(first_Name.count("r"))
count_R2 = int(second_Name.count("r"))
count_U1 = int(first_Name.count("u"))
count_U2 = int(second_Name.count("u"))
count_E1 = int(first_Name.count("e"))
count_E2 = int(second_Name.count("e"))

true = str(count_T1+count_T2+count_R1+count_R2+count_E1+count_E2+count_U1+count_U2)

#LOVE

count_L1 = int(first_Name.count("l"))
count_L2 =  int(second_Name.count("l"))
count_O1 = int(first_Name.count("o"))
count_O2 = int(second_Name.count("o"))
count_V1 = int(first_Name.count("v"))
count_V2 = int(second_Name.count("v"))

LOVE = str(count_L1+count_E1+count_E2+count_L2+count_O1+count_O2+count_V1+count_V2)

Love_score = int(LOVE+true)
if Love_score<10 or Love_score>90:
    print(f"Your score is {Love_score}, you go together like coke and mentos")
elif 40<=Love_score<=50:
    print(f"Your Score is {Love_score},you are alright together")
else:
    print(f"Your score is {Love_score}")