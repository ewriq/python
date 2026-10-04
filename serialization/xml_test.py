import xml.etree.ElementTree as ET

data = """
<user>
    <name>ewriq</name>
    <age>10</age>
</user>
"""

user = ET.fromstring(data)

print(user.find("name").text)
print(user.find("age").text)