print("****** Welcome to the BMI calculator!! ******")


first_name = input("Please enter your first name and press ENTER: ") # input for first name, last name, and age
last_name = input("Please enter your last name and press ENTER: ")
age = input("Please enter current age and press ENTER: ")
print("*****Welcome,",first_name, last_name, "*******!","\nAge",age)

height = int(input("Please enter height in inches: "))# input for height and weight
current_weight = int(input("Please enter your current weight in lbs: "))

current_bmi = float(current_weight/(height**2) * 703) # formula for BMI with print statement
print("Your current BMI is:", current_bmi)

if current_bmi>30: # if, elif, else statement for BMI classifications
    print("Your BMI classification is obese.")
elif current_bmi<18.5:
    print("Your BMI classification is underweight.")
elif current_bmi>18.5 and current_bmi<24.9:
    print("Normal")
else:
    print("Your BMI classification is overweight.")

# *** BMI classifications
# Underweight: Less than 18.5
# Normal weight: 18.5 to 24.9
# Overweight: 25 to 29.9
# Obesity: 30 or higher

print("Would you like to recalculate your BMI?")