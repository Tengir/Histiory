def generate_top_players(players: dict):
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse=True)
    result = ""
    for player in sorted_players:
        result += f"{player[1]} {player[0]}\n"
    return result.strip()