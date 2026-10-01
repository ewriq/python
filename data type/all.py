number = 100

decimal = 3.14

text = "Python"

is_active = True

character = "A"


numbers = [1, 2, 3, 4]

user = {
    "name": "Ali",
    "age": 20
}

unique_numbers = {1, 2, 3, 3, 3}

coordinates = (10, 20)

data = None

print("TYPE CHECKING")

print(type(number))
print(type(decimal))
print(type(text))
print(type(is_active))
print(type(character))
print(type(numbers))
print(type(user))
print(type(unique_numbers))
print(type(coordinates))
print(type(data))

print("\nISINSTANCE")

print(isinstance(number, int))
print(isinstance(decimal, float))
print(isinstance(text, str))
print(isinstance(is_active, bool))
print(isinstance(numbers, list))
print(isinstance(user, dict))

print("\nTYPE CONVERSION")

string_number = "50"
integer_number = int(string_number)

print(integer_number)
print(type(integer_number))

float_number = float(number)

print(float_number)
print(type(float_number))

string_value = str(number)

print(string_value)
print(type(string_value))

boolean_value = bool(number)

print(boolean_value)
print(type(boolean_value))

tuple_value = tuple(numbers)

print(tuple_value)
print(type(tuple_value))

list_value = list(coordinates)

print(list_value)
print(type(list_value))

set_value = set(numbers)

print(set_value)
print(type(set_value))

print("\nVALUES")

print(number)
print(decimal)
print(text)
print(is_active)
print(character)
print(numbers)
print(user)
print(unique_numbers)
print(coordinates)
print(data)