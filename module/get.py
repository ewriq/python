import http.client

conn = http.client.HTTPSConnection("github.com")

conn.request("GET", "/ewriq")

response = conn.getresponse()

print(response.status)

data = response.read().decode("utf-8")

print(data)

conn.close()