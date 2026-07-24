import sqlite3

conn = sqlite3.connect("moneyhunter.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    name TEXT,
    age TEXT,
    activity TEXT,
    goal TEXT,
    income TEXT
)
""")

conn.commit()


def save_user(telegram_id, name, age, activity, goal, income):
    cursor.execute("""
    INSERT INTO users
    (telegram_id, name, age, activity, goal, income)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        telegram_id,
        name,
        age,
        activity,
        goal,
        income
    ))

    conn.commit()