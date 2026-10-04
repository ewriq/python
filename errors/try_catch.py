file_handle = None

try:
    file_handle = open("data.txt")
    print(file_handle.read())
    
except FileNotFoundError:
    print("404")

finally:
    if file_handle:
        file_handle.close()