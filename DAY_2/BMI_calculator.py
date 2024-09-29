height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

height_for_BMI_Calculator = height*height

BMI =  weight/height_for_BMI_Calculator

if(BMI< 18.5):
    print("You are underweight")
elif(18.5 <= BMI <25):
    print("You are NormalWeight")
elif(25<=BMI<30):
    print("You are overweight")
else:
    print("You are Obese")