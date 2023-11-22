from flask import Flask, render_template
import requests
import json
from tabulate import tabulate
import os


app = Flask(__name__)

def fetch_cricket_scores():
    url = "https://cricbuzz-cricket.p.rapidapi.com/matches/v1/recent"

    headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "Replace with your RapidAPI key"  
    }
    response = requests.get(url, headers=headers)
    data = response.json()

    matches_data = []

    for match in data['typeMatches'][0]['seriesMatches'][0]['seriesAdWrapper']['matches']:
        table = [
            [f" {match['matchInfo']['matchDesc']} , {match['matchInfo']['team1']['teamName']} vs {match['matchInfo']['team2']['teamName']}"],
            ["Series Name", match['matchInfo']['seriesName']],
            ["Match Format", match['matchInfo']['matchFormat']],
            ["Result", match['matchInfo']['status']],
            [f"{match['matchInfo']['team1']['teamName']} Score", f"{match['matchScore']['team1Score']['inngs1']['runs']}/{match['matchScore']['team1Score']['inngs1']['wickets']} in {match['matchScore']['team1Score']['inngs1']['overs']} overs"],
            [f"{match['matchInfo']['team2']['teamName']} Score", f"{match['matchScore']['team2Score']['inngs1']['runs']}/{match['matchScore']['team2Score']['inngs1']['wickets']} in {match['matchScore']['team2Score']['inngs1']['overs']} overs"]
        ]
        matches_data.append(tabulate(table, tablefmt="html"))

    return matches_data

def fetch_upcoming_matches():
    url = "https://cricbuzz-cricket.p.rapidapi.com/schedule/v1/international"

    headers = {
        "X-RapidAPI-Host": "cricbuzz-cricket.p.rapidapi.com",
        "X-RapidAPI-Key": "1bd0a14833mshc18ed4be5953504p1236e8jsn709d3a0bc623"  # Replace with your RapidAPI key
    }
    #
    response = requests.get(url, headers=headers)
    upcoming_matches = []

    if response.status_code == 200:
        try:
            data = response.json()
            match_schedules = data.get('matchScheduleMap', [])

            for schedule in match_schedules:
                if 'scheduleAdWrapper' in schedule:
                    date = schedule['scheduleAdWrapper']['date']
                    matches = schedule['scheduleAdWrapper']['matchScheduleList']

                    for match_info in matches:
                        for match in match_info['matchInfo']:
                            description = match['matchDesc']
                            team1 = match['team1']['teamName']
                            team2 = match['team2']['teamName']
                            match_data = {
                                'Date': date,
                                'Description': description,
                                'Teams': f"{team1} vs {team2}"
                            }
                            upcoming_matches.append(match_data)
                else:
                    print("No match schedule found for this entry.")

        except json.JSONDecodeError as e:
            print("Error parsing JSON:", e)
        except KeyError as e:
            print("Key error:", e)
    else:
        print("Failed to fetch cricket scores. Status code:", response.status_code)

    return upcoming_matches

@app.route('/')
def index():
    cricket_scores = fetch_cricket_scores()
    upcoming_matches = fetch_upcoming_matches()
    return render_template('index.html', cricket_scores=cricket_scores, upcoming_matches=upcoming_matches)

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)
