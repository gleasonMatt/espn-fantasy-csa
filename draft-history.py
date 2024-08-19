from espn_api.football import League


def get_position(teams, player_id):
    for team in teams:
        for player in team.roster:
            if player_id == player.playerId:
                return player.position
    return ''


if __name__ == '__main__':
    # 2018 first year with 12
    years = range(2023, 2024)
    for year in years:
        if year == 2018:
            continue
        print("")
        print(str(year))
        league = League(league_id=1601564, year=year)
        draft_list = league.draft
        for count, draftee in enumerate(draft_list):
            round = draftee.round_num
            team_owner = draftee.team.owners
            round_pick = draftee.round_pick
            name = draftee.playerName
            pos = get_position(league.teams, draftee.playerId)
            print(str(count + 1) + " | " + str(round) + " | " + str(round_pick) + " | " + name + " | " + pos + " | " +
                  str(team_owner[0]['firstName'] + " " + team_owner[0]['lastName']))
