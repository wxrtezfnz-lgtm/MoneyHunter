import sqlite3

conn = sqlite3.connect("moneyhunter.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER,
    name TEXT,
    age TEXT,
    activity TEXT,
    goal TEXT,
    income TEXT,
    experience TEXT,
    day INTEGER DEFAULT 1
)
""")

conn.commit()


def save_user(
    telegram_id,
    name,
    age,
    activity,
    goal,
    income,
    experience
):

    cursor.execute("""
    INSERT INTO users
    (
        telegram_id,
        name,
        age,
        activity,
        goal,
        income,
        experience,
        day
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        telegram_id,
        name,
        age,
        activity,
        goal,
        income,
        experience,
        1
    ))

    conn.commit()


def get_user(telegram_id):

    cursor.execute("""
    SELECT *
    FROM users
    WHERE telegram_id = ?
    """, (telegram_id,))

    return cursor.fetchone()


def get_day(telegram_id):

    cursor.execute("""
    SELECT day
    FROM users
    WHERE telegram_id = ?
    """, (telegram_id,))

    row = cursor.fetchone()

    if row:
        return row[0]

    return 1


def next_day(telegram_id):

    cursor.execute("""
    UPDATE users
    SET day = day + 1
    WHERE telegram_id = ?
    """, (telegram_id,))

    conn.commit()