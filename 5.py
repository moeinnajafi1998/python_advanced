# The requests library in Python is a popular choice for making HTTP requests. 
# It simplifies the process of sending various types of HTTP requests to a server. 
# Here’s a breakdown of the most commonly used HTTP methods with examples for each.

# 1. GET
# The GET method is used to retrieve data from a server. It appends parameters to the URL.
import requests
response = requests.get('https://api.example.com/data')
print(response.status_code)  # Check status code
print(response.json())       # Print JSON response

# 2. POST
# The POST method is used to send data to the server, often resulting in a change in state or side effects on the server.
import requests
data = {'key': 'value'}
response = requests.post('https://api.example.com/data', json=data)
print(response.status_code)
print(response.json())

# 3. PUT
# The PUT method is used to update an existing resource or create a new resource if it does not exist.
import requests
data = {'key': 'new_value'}
response = requests.put('https://api.example.com/data/1', json=data)
print(response.status_code)
print(response.json())

# 4. PATCH
# The PATCH method is used to apply partial modifications to a resource.
import requests
data = {'key': 'updated_value'}
response = requests.patch('https://api.example.com/data/1', json=data)
print(response.status_code)
print(response.json())

# 5. DELETE
# The DELETE method is used to delete a specified resource.
import requests
response = requests.delete('https://api.example.com/data/1')
print(response.status_code)

# 6. HEAD
# The HEAD method is similar to GET, but it retrieves only the headers and not the body of the response.
import requests
response = requests.head('https://api.example.com/data')
print(response.status_code)
print(response.headers)  # Print headers

# 7. OPTIONS
# The OPTIONS method is used to describe the communication options for the target resource. It’s often used for CORS (Cross-Origin Resource Sharing) requests.
import requests
response = requests.options('https://api.example.com/data')
print(response.status_code)
print(response.headers)

# 8. Custom Headers
# You can also send custom headers with any request. Here’s an example using a GET request:
import requests
headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
response = requests.get('https://api.example.com/data', headers=headers)
print(response.status_code)
print(response.json())

# 9. Handling Timeouts
# You can set a timeout for your requests to prevent them from hanging indefinitely.
import requests
try:
    response = requests.get('https://api.example.com/data', timeout=5)  # 5 seconds timeout
    print(response.json())
except requests.exceptions.Timeout:
    print("The request timed out")

# Summary
# The requests library provides an easy-to-use interface for making HTTP requests in Python,
#    supporting all major HTTP methods and customizations like headers, timeouts, and response handling. 
# You can also handle exceptions and errors gracefully to ensure your application runs smoothly.