from espn_api.football import League

# Show all the teams for year specified.

if __name__ == '__main__':
    league = League(league_id=1601564, year=2023)
    for team in league.teams:
        print(team.owners[0]['firstName'] + " " + team.owners[0]['lastName'])