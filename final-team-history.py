import math

from espn_api.football import League
import msgspec


class Player(msgspec.Struct):
    Name: str
    Team: str
    Position: str
    AverageDraftPositionPPR: float


if __name__ == '__main__':
    years = range(2018, 2024)
    for year in years:
        print("YEAR: " + str(year))
        if year == 2018:
            with open("teams_files/teams_" + str(year) + ".txt", "r") as f:
                for team in f.readlines():
                    print("TEAM: " + team.split(',')[0] + " | STANDING: " + team.split(',')[1])
                    continue
        else:
            with open("adp_files/adp_" + str(year) + ".json", "rb") as f:
                adp = msgspec.json.decode(f.read(), type=list[Player])

            league = League(league_id=1601564, year=year)
            draft_list = league.draft

            for team in league.teams:
                print("TEAM: " + team.team_name + " | STANDING: " + str(team.standing))
                for player in team.roster:
                    player_id = player.playerId
                    pos = 180
                    draft_pos = 180
                    round = 0
                    team_owner = ""
                    round_pick = 0
                    player_name = player.name
                    for position in adp:
                        if position.Name.upper() == player.name.upper():
                            pos = position.AverageDraftPositionPPR
                            break

                    for count, draftee in enumerate(draft_list):
                        if draftee.playerId == player_id:
                            round = draftee.round_num
                            team_owner = draftee.team.owners[0]['firstName'] + " " + draftee.team.owners[0]['lastName']
                            round_pick = draftee.round_pick
                            draft_pos = count

                    print(player_name + " | Draft: " + str(draft_pos) + " | " + str(round) + " | "
                          + str(round_pick) + " | " + team_owner + " | ADP: " + str(pos) + " - " + str(math.floor(pos / 12) + 1)
                          + " - " + str(math.floor(pos % 12)) + " Diff: " + str(draft_pos - pos))
                print("\n")
