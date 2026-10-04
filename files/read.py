file_handle = open("data.txt", "r")
content = file_handle.read()
print(content)
file_handle.close()