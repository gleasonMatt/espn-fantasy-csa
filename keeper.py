import math

from espn_api.football import League
import msgspec

# Lists your players at end of season specified, and shows when they were drafted that year and by whom.
# Then it compares that player to the adp.json file that should be this years current adp for all players,
# and shows where they are being drafted now, High Low and average with STDEV.

class Player(msgspec.Struct):
    adp: float
    name: str
    high: float
    low: float
    stdev: float


if __name__ == '__main__':
    with open("adp_files/adp.json", "rb") as f:
        adp = msgspec.json.decode(f.read(), type=list[Player])

    league = League(league_id=1601564, year=2023)
    draft_list = league.draft
    print("\nKeeper List:")
    print("")
    for team in league.teams:
        if team.team_id != 12:
            continue
        print("TEAM: " + team.team_name + " | STANDING: " + str(team.standing))
        for player in team.roster:
            player_id = player.playerId
            pos = 180
            draft_pos = 180
            high = 0
            low = 0
            stdev = 0
            round = 0
            team_owner = ""
            round_pick = 0
            player_name = player.name
            for position in adp:
                if position.name.upper() == player.name.upper():
                    pos = position.adp
                    high = position.high
                    low = position.low
                    stdev = position.stdev
                    break

            for count, draftee in enumerate(draft_list):
                if draftee.playerId == player_id:
                    round = draftee.round_num
                    team_owner = draftee.team.owners[0]
                    round_pick = draftee.round_pick
                    draft_pos = count

            print(player_name + " | Draft: " + str(draft_pos) + " | " + str(round) + " | "
                  + str(round_pick) + " | " + ("NONE" if not team_owner else str(team_owner['firstName'])) + " | ADP: " + str(pos) + " - " + str(math.floor(pos / 12) + 1)
                  + " - " + str(math.floor(pos % 12)) + " Diff: " + str(draft_pos - pos) + " | HIGH: " + str(high) +
                  " | LOW: " + str(low) + " | STDEV: " + str(stdev))
        print("\n")
