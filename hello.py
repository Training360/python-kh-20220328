import requests

print("Hello Docker")

response = requests.get("https://api.github.com/users/vicziani")
print(response.json())

# mod1