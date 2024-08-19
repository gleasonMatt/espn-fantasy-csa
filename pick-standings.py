from espn_api.football import League
import numpy as np
import matplotlib.pyplot as plt

# Populates dict from draft position 1 - 12 and adds placement of the team to the array of values to the position
# After populating all years, graph the data based on final placement of team if place <= value specified.
# 2016 is the first year with 12 teams so we will start from there.

def graph_data(data):
    places = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x = np.arange(1, 13, 1)
    for pos in data:
        for place in data[pos]:
            if place <= 3:
                places[pos - 1] += 1
    plt.plot(labels, places, 'ro')
    plt.xticks(x)
    plt.show()


if __name__ == '__main__':
    years = range(2016, 2024)
    data = {1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : [], 10 : [], 11 : [], 12 : []}
    for year in years:
        if year == 2018:
            continue
        print("")
        print(str(year))
        league = League(league_id=1601564, year=year)
        for count, pick in enumerate(league.draft):
            if pick.round_num == 1:
                pick_team = pick.team.team_name
                for team in league.teams:
                    if team.team_name == pick_team:
                        standing = team.standing
                        if data[count + 1] is None:
                            data[count + 1] = [standing, 0]
                        else:
                            data[count + 1].append(standing)
            else:
                break

        print(data)
    graph_data(data)