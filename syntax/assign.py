import random

age = random.randint(0, 100)
print("Your age is:", age)

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
elif age == 0  :
    print("You are a baby.")
else :
    print("You are a child.")
    