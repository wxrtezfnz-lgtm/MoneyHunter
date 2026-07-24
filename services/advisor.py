def get_strategy(age, activity, goal, income, experience):

    # Новичок
    if "новичок" in experience.lower():
        return {
            "skill": "ChatGPT + Telegram-боты",
            "first_step": "Освой ChatGPT, затем создай своего первого Telegram-бота.",
            "money": "Через 2–4 недели попробуй взять первый заказ на Kwork или Freelance."
        }

    # Уже пробовал
    if "пробовал" in experience.lower():
        return {
            "skill": "Автоматизация и AI",
            "first_step": "Собери 2–3 проекта в портфолио.",
            "money": "Начинай искать клиентов и продавать свои услуги."
        }

    # Уже зарабатывает
    if "зарабатываю" in experience.lower():
        return {
            "skill": "Масштабирование",
            "first_step": "Автоматизируй свою работу с помощью AI.",
            "money": "Повышай средний чек и создавай собственный продукт."
        }

    return {
        "skill": "Востребованный онлайн-навык",
        "first_step": "Начни обучение уже сегодня.",
        "money": "Через месяц попробуй заработать первые деньги."
    }


def generate_plan(data):

    age = int(data["age"])
    activity = data["activity"]
    goal = data["goal"]
    income = data["income"]
    experience = data["experience"]
    name = data["name"]

    strategy = get_strategy(
        age,
        activity,
        goal,
        income,
        experience
    )

    text = (
        f"🧠 <b>Персональный разбор для {name}</b>\n\n"

        f"👤 <b>Возраст:</b> {age}\n"
        f"💼 <b>Деятельность:</b> {activity}\n"
        f"🎯 <b>Цель:</b> {goal}\n"
        f"💰 <b>Доход:</b> {income}\n"
        f"⭐ <b>Опыт:</b> {experience}\n\n"

        "━━━━━━━━━━━━━━━━━━\n"
        "📊 <b>Мой вывод</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"
    )

    if age <= 25:
        text += "🚀 Сейчас у тебя лучший период для быстрого роста.\n\n"
    else:
        text += "💼 Твой опыт поможет быстрее выйти на высокий доход.\n\n"

    text += (
        "━━━━━━━━━━━━━━━━━━\n"
        "🧭 <b>Твоя стратегия</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"

        f"🛠 <b>Главный навык:</b>\n{strategy['skill']}\n\n"

        f"🚀 <b>Первый шаг:</b>\n{strategy['first_step']}\n\n"

        f"💸 <b>Как заработать:</b>\n{strategy['money']}\n\n"

        "━━━━━━━━━━━━━━━━━━\n"
        "📅 <b>План на неделю</b>\n"
        "━━━━━━━━━━━━━━━━━━\n\n"

        "✅ День 1 — изучить тему.\n"
        "✅ День 2 — посмотреть практику.\n"
        "✅ День 3 — сделать мини-проект.\n"
        "✅ День 4 — улучшить проект.\n"
        "✅ День 5 — оформить портфолио.\n"
        "✅ День 6 — начать искать клиентов.\n"
        "✅ День 7 — получить первый отклик.\n\n"

        "🔥 Каждый следующий день бот сможет выдавать тебе новое персональное задание."
    )

    return text