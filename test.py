import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "Replace with your RapidAPI key"  # Replace with your RapidAPI key
    }
response = requests.get(url, headers=headers)
print(response.json())
  
