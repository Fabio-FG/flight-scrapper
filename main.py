import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

print("making request to API...")
print (f"URL: {url}\n")

# make the http get request
response = requests.get(url)

print(f"Status Code: {response.status_code}")

# check json data
data = response.json()
print("data", data)