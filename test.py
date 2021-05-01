import requests
#import json

teams = {
    "ATL": {
        "id": 1,
        "abbreviation": "ATL",
        "city": "Atlanta",
        "conference": "East",
        "division": "Southeast",
        "full_name": "Atlanta Hawks",
        "name": "Hawks"
    },
    "BOS": {
        "id": 2,
        "abbreviation": "BOS",
        "city": "Boston",
        "conference": "East",
        "division": "Atlantic",
        "full_name": "Boston Celtics",
        "name": "Celtics"
    },
    "BKN": {
        "id": 3,
        "abbreviation": "BKN",
        "city": "Brooklyn",
        "conference": "East",
        "division": "Atlantic",
        "full_name": "Brooklyn Nets",
        "name": "Nets"
    },
    "CHA": {
        "id": 4,
        "abbreviation": "CHA",
        "city": "Charlotte",
        "conference": "East",
        "division": "Southeast",
        "full_name": "Charlotte Hornets",
        "name": "Hornets"
    },
    "CHI": {
        "id": 5,
        "abbreviation": "CHI",
        "city": "Chicago",
        "conference": "East",
        "division": "Central",
        "full_name": "Chicago Bulls",
        "name": "Bulls"
    },
    "CLE": {
        "id": 6,
        "abbreviation": "CLE",
        "city": "Cleveland",
        "conference": "East",
        "division": "Central",
        "full_name": "Cleveland Cavaliers",
        "name": "Cavaliers"
    },
    "DAL": {
        "id": 7,
        "abbreviation": "DAL",
        "city": "Dallas",
        "conference": "West",
        "division": "Southwest",
        "full_name": "Dallas Mavericks",
        "name": "Mavericks"
    },
    "DEN": {
        "id": 8,
        "abbreviation": "DEN",
        "city": "Denver",
        "conference": "West",
        "division": "Northwest",
        "full_name": "Denver Nuggets",
        "name": "Nuggets"
    },
    "DET": {
        "id": 9,
        "abbreviation": "DET",
        "city": "Detroit",
        "conference": "East",
        "division": "Central",
        "full_name": "Detroit Pistons",
        "name": "Pistons"
    },
    "GSW": {
        "id": 10,
        "abbreviation": "GSW",
        "city": "Golden State",
        "conference": "West",
        "division": "Pacific",
        "full_name": "Golden State Warriors",
        "name": "Warriors"
    },
    "HOU": {
        "id": 11,
        "abbreviation": "HOU",
        "city": "Houston",
        "conference": "West",
        "division": "Southwest",
        "full_name": "Houston Rockets",
        "name": "Rockets"
    },
    "IND": {
        "id": 12,
        "abbreviation": "IND",
        "city": "Indiana",
        "conference": "East",
        "division": "Central",
        "full_name": "Indiana Pacers",
        "name": "Pacers"
    },
    "LAC": {
        "id": 13,
        "abbreviation": "LAC",
        "city": "LA",
        "conference": "West",
        "division": "Pacific",
        "full_name": "LA Clippers",
        "name": "Clippers"
    },
    "LAL": 
        "id": 14,
        "abbreviation": "LAL",
        "city": "Los Angeles",
        "conference": "West",
        "division": "Pacific",
        "full_name": "Los Angeles Lakers",
        "name": "Lakers"
    },
    "MEM": {
        "id": 15,
        "abbreviation": "MEM",
        "city": "Memphis",
        "conference": "West",
        "division": "Southwest",
        "full_name": "Memphis Grizzlies",
        "name": "Grizzlies"
    },
    "MIA": {
        "id": 16,
        "abbreviation": "MIA",
        "city": "Miami",
        "conference": "East",
        "division": "Southeast",
        "full_name": "Miami Heat",
        "name": "Heat"
    },
    "MIL": {
        "id": 17,
        "abbreviation": "MIL",
        "city": "Milwaukee",
        "conference": "East",
        "division": "Central",
        "full_name": "Milwaukee Bucks",
        "name": "Bucks"
    },
    "MIN": {
        "id": 18,
        "abbreviation": "MIN",
        "city": "Minnesota",
        "conference": "West",
        "division": "Northwest",
        "full_name": "Minnesota Timberwolves",
        "name": "Timberwolves"
    },
    "NOP": {
        "id": 19,
        "abbreviation": "NOP",
        "city": "New Orleans",
        "conference": "West",
        "division": "Southwest",
        "full_name": "New Orleans Pelicans",
        "name": "Pelicans"
    },
    "NYK": {
        "id": 20,
        "abbreviation": "NYK",
        "city": "New York",
        "conference": "East",
        "division": "Atlantic",
        "full_name": "New York Knicks",
        "name": "Knicks"
    },
    "OKC": {
        "id": 21,
        "abbreviation": "OKC",
        "city": "Oklahoma City",
        "conference": "West",
        "division": "Northwest",
        "full_name": "Oklahoma City Thunder",
        "name": "Thunder"
    },
    "ORL": {
        "id": 22,
        "abbreviation": "ORL",
        "city": "Orlando",
        "conference": "East",
        "division": "Southeast",
        "full_name": "Orlando Magic",
        "name": "Magic"
    },
    "PHI": {
        "id": 23,
        "abbreviation": "PHI",
        "city": "Philadelphia",
        "conference": "East",
        "division": "Atlantic",
        "full_name": "Philadelphia 76ers",
        "name": "76ers"
    },
    "PHX": {
        "id": 24,
        "abbreviation": "PHX",
        "city": "Phoenix",
        "conference": "West",
        "division": "Pacific",
        "full_name": "Phoenix Suns",
        "name": "Suns"
    },
    "POR": {
        "id": 25,
        "abbreviation": "POR",
        "city": "Portland",
        "conference": "West",
        "division": "Northwest",
        "full_name": "Portland Trail Blazers",
        "name": "Trail Blazers"
    },
    "SAC": {
        "id": 26,
        "abbreviation": "SAC",
        "city": "Sacramento",
        "conference": "West",
        "division": "Pacific",
        "full_name": "Sacramento Kings",
        "name": "Kings"
    },
    "SAS": {
        "id": 27,
        "abbreviation": "SAS",
        "city": "San Antonio",
        "conference": "West",
        "division": "Southwest",
        "full_name": "San Antonio Spurs",
        "name": "Spurs"
    },
    "TOR": {
        "id": 28,
        "abbreviation": "TOR",
        "city": "Toronto",
        "conference": "East",
        "division": "Atlantic",
        "full_name": "Toronto Raptors",
        "name": "Raptors"
    },
    "UTA": {
        "id": 29,
        "abbreviation": "UTA",
        "city": "Utah",
        "conference": "West",
        "division": "Northwest",
        "full_name": "Utah Jazz",
        "name": "Jazz"
    },
    "WAS": {
        "id": 30,
        "abbreviation": "WAS",
        "city": "Washington",
        "conference": "East",
        "division": "Southeast",
        "full_name": "Washington Wizards",
        "name": "Wizards"
    }
}

user_team = input("Enter team code:")

if user_team in teams:
    teamId = {teams[user_team]}
    print(f"\n\n{user_team} -- {teamId}\n\n")
    #url = f"https://stats.nba.com/stats/commonteamroster/?Season={season}&TeamID={teams[user_team]}"
    url = "https://free-nba.p.rapidapi.com/teams"
    querystring = {"page":"0"}
    headers = {
        'x-rapidapi-host': "free-nba.p.rapidapi.com",
        'x-rapidapi-key': "42a39ab4a1mshbd35872590c3224p1993edjsn16da697457e9"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # Print the status code of the response.
    print(response.content)
else:
    print(f"{user_team} is not a valid team name")