age = 30
group = "control"
BMI = 20

condition = (group == "treatment") & (BMI >= 15)
print(condition)
