from espn_api.football import League
import matplotlib.pyplot as plt


def graph_data(data):
    labels = []
    top_4 = []
    for aqui in data:
        labels.append(aqui)
        top_4.append(data[aqui])
    plt.bar(labels, top_4)
    plt.show()


if __name__ == '__main__':
    years = range(2023, 2024)
    data = {}
    for year in years:
        if year == 2018:
            continue
        print("")
        print(str(year))
        league = League(league_id=1601564, year=year)
        draft_list = league.draft

        for team in league.teams:
            standing = team.standing
            if standing <= 3:
                for player in team.roster:
                    if player.position == 'WR':
                        player_id = player.playerId
                        for count, draftee in enumerate(draft_list):
                            if draftee.playerId == player_id and draftee.round_num <= 3:
                                if standing in data:
                                    data[standing] += 1
                                else:
                                    data[standing] = 1
        print(data)
    graph_data(data)