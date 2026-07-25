from services.days import DAYS


def build_day(day: int):

    info = DAYS.get(day)

    if info is None:
        return (
            "🏆 Все задания выполнены!\n\n"
            "🚀 Скоро появятся новые уровни."
        )

    text = (
        f"🔥 <b>День {day}</b>\n\n"

        f"📚 <b>{info['title']}</b>\n\n"
    )

    for task in info["tasks"]:
        text += f"✅ {task}\n"

    text += (
        "\n"
        f"🎯 <b>Цель дня:</b>\n"
        f"{info['goal']}"
    )

    return text