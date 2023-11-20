import requests

url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "1bd0a14833mshc18ed4be5953504p1236e8jsn709d3a0bc623"  # Replace with your RapidAPI key
    }
response = requests.get(url, headers=headers)
print(response.json())
  