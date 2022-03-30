weight = float(input("Enter you weight in Kg : "))
height = float(input("Enter your weight in Cms : "))

bmi = weight / (height**2)
print("Computing...")
print("Your BMI is {} \n".format(bmi))
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.99:
    print("Perfect ! Normal Weight")
elif 25.00 <= bmi <= 30.00:
    print("Overweight")
else:
    print("Obese")
