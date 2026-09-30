print("===FITNESS & BMI TRACKER===")

name = input("enter your name:")
height = float(input("enter your height in meters:"))
weight = float(input("enter your weight in kg:"))

bmi = weight/(height**2)

print("\n---result---")
print("name:",name)
print("BMI:",bmi)

if bmi < 18.5:
    category = "underweight"
    advise = "focus on balanced and nutritous meals"
elif bmi < 25:
    category = "normal range"
    advise = "maintain a balanced diet and regular activity"
elif bmi <30:
    category ="overweight"
    advise = "focus on regular phycal activity and balanced meal"
else:
    category = "obesity range"
    advise = "consider discussing healthy lifestyle goals with a qualified proffessional"

print("category:",category)
print("suggestion:", advise)
print("\nthank you for using the fitness & BMI tracker!")