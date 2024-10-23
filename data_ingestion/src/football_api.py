import requests
from typing import List
from models import Team, Competition, Area, CurrentSeason
import os

class FootballApi:
    def __init__(self):
        self._base_url = "https://api.football-data.org/v4/"
        self._headers = {
            "X-Auth-Token": os.environ["FOOTBALL_API_TOKEN"],
            "Accept-Encoding": "",
        }
        
        self._global_params = {"limit": "10000"}
        
    def get_teams(self) -> List[Team]:
        response = requests.get(f"{self._base_url}/teams", headers=self._headers, params=self._global_params)
        teams_data = response.json()["teams"]
        
        return [Team(**team_data) for team_data in teams_data]

    def get_competitions(self) -> List[Competition]:
        response = requests.get(f"{self._base_url}/competitions", headers=self._headers, params=self._global_params)
        competitions_data = response.json()["competitions"]
        
        competitions = []
        for competition_data in competitions_data:
            area_data = competition_data.pop("area", {})
            area = Area(**area_data)
            
            current_season_data = competition_data.pop("currentSeason", {})
            winner_data = current_season_data.pop("winner", {})
            winner = Team(**winner_data) if winner_data else None
            current_season = CurrentSeason(**current_season_data, winner=winner)
            
            competition = Competition(**competition_data, area=area, currentSeason=current_season)
            competitions.append(competition)
        
        return competitions

# Example usage
if __name__ == "__main__":
    api = FootballApi()

    print("Teams:")
    teams = api.get_teams()
    for team in teams:
        print(f"Team: {team.name}, Crest: {team.crest}")

    print("\nCompetitions:")
    competitions = api.get_competitions()
    for competition in competitions:
        print(competition)
        print(f"Competition: {competition.name}")
        print(f"Area: {competition.area.name}")
        print(f"Current Season: {competition.currentSeason.startDate} - {competition.currentSeason.endDate}")
        if competition.currentSeason.winner:
            print(f"Winner: {competition.currentSeason.winner.name}")
        else:
            print("No winner yet")
        print()