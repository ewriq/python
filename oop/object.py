class User:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User("ewriq", 111)

print(user.name)
print(user.age)