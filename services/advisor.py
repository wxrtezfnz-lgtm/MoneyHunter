def generate_plan(data):
    return (
        f"👋 {data['name']}, я проанализировал твою анкету.\n\n"
        f"🎯 Цель: {data['goal']}\n"
        f"💰 Доход: {data['income']}\n\n"
        "🚀 Скоро здесь будет персональный AI-план."
    )