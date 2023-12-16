def generate_top(top: dict):
    sorted_top = sorted(top.items(), key=lambda x: x[1], reverse=True)
    top_str = "Топ игроков\n"
    for item in sorted_top:
        top_str += str(item[1]) + " - " + str(item[0]) + "\n"
    return top_str + "\n"
