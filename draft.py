import msgspec


class Player(msgspec.Struct):
    adp: float
    name: str
    high: float
    low: float
    stdev: float
    position: str


if __name__ == '__main__':
    with open("adp_files/adp.json", "rb") as f:
        adp = msgspec.json.decode(f.read(), type=list[Player])

    for player in adp:

        print(player)