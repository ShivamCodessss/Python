Weight = int(input("Enter Your Weight In (kg.) : "))
Height = float(input("Enter Your Height In (Cm.) : "))

BMI = Weight / (Height/100)**2

if BMI <= 18.5:
    print("Oops! you are Underweight")
elif BMI <= 24.9 and BMI >= 18.5:
    print("Awesome! You are Healthy")
elif BMI >= 24.9 and BMI <= 29.9:
    print("Oops! You are Overweight")
else:
    print("Sheesh! You are Obese")
