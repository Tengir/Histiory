def generate_top(top: dict):
    sorted_top = sorted(top.items(), key=lambda x: x[1], reverse=True)
    top_str = "Топ игроков\n"
    for item in sorted_top:
        top_str += str(item[1]) + " - " + str(item[0]) + "\n"
    return top_str + "\n"


def generate_winner(top: dict):
    sorted_top = sorted(top.items(), key=lambda x: x[1], reverse=True)
    names = [x[0] for x in sorted_top if x[1] == sorted_top[0][1]]
    res = f"Поздравляем {', '.join(names)} с победой в исторической викторине!\n"
    if len(names) == 1:
        res += "Ты настоящий исторический гений! 🎉🎉🎉"
    else:
        res += "Вы настоящие исторические гении! 🎉🎉🎉"
    return res
