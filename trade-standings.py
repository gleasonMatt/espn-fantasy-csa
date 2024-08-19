from espn_api.football import League
import matplotlib.pyplot as plt

# This shows teams who placed in the top x amount and the amount of trades they made throughout the year.

def graph_trades(data):
    labels = []
    top_4 = []
    for aqui in data:
        labels.append(aqui)
        top_4.append(data[aqui])
    plt.bar(labels, top_4)
    plt.xlabel("Trades Number")
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
                trades = team.trades
                if trades in data:
                    data[trades] += 1
                else:
                    data[trades] = 1
        print(data)
    graph_trades(data)


