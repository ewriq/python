file = None

try:
    file = open("data.txt")
    print(file.read())
    
except FileNotFoundError:
    print("404")

finally:
    if file:
        file.close()