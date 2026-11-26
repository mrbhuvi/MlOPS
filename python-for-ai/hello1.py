import requests

response = requests.get('https://api.github.com')
if response.status_code == 200: 
    print("Successfully connected to GitHub API!")  
