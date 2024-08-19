from espn_api.football import League
import matplotlib.pyplot as plt

# Number of acquisitions plotted against the amount of times reached top x amount of standings.

def graph_aqui(data):
    labels = []
    top_4 = []
    for aqui in data:
        labels.append(aqui)
        top_4.append(data[aqui])
    plt.bar(labels, top_4)
    plt.xlabel("Aquired Number")
    plt.ylabel("Top 4 Count")
    plt.show()


if __name__ == '__main__':
    years = range(2016, 2023)
    data = {}
    for year in years:
        if year == 2018:
            continue
        print("")
        print(str(year))
        league = League(league_id=1601564, year=year)

        for team in league.teams:
            standing = team.standing
            if standing <= 4:
                aqui = team.acquisitions
                if aqui in data:
                    data[aqui] += 1
                else:
                    data[aqui] = 1
        print(data)
    graph_aqui(data)