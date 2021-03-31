age = 30
group = "control"
BMI = 20

condition = ((BMI >= 15) | (age > 40)) & (group == "treatment")
print(condition)
