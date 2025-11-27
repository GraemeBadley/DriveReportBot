import requests
from datetime import date
    
def get_todays_games():
    today = date.today()
    strdate = f"{today.year}{today.month:02}{today.day:02}"
    url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates=" + strdate
    
    response = requests.get(url)
    if response.status_code == 200:
        games = []
        data = response.json()
        for event in data["events"]:
            games.append(event["id"])
            print(f"{event["shortName"]}, id: {event["id"]}")
        return games
    else:
        raise Exception(f"{response.text}")

    
def main():
    games = get_todays_games()
    print(games)
    
if __name__ == "__main__":
    main()
