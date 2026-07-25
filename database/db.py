import os
import psycopg
from psycopg.rows import dict_row


DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg.connect(
    DATABASE_URL,
    row_factory=dict_row
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

    id SERIAL PRIMARY KEY,

    telegram_id BIGINT UNIQUE,

    name TEXT,
    age TEXT,
    activity TEXT,
    goal TEXT,
    income TEXT,
    experience TEXT,

    day INTEGER DEFAULT 1,

    level INTEGER DEFAULT 1,
    xp INTEGER DEFAULT 0,
    streak INTEGER DEFAULT 1,
    achievements TEXT DEFAULT ''

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
        experience
    )

    VALUES
    (%s,%s,%s,%s,%s,%s,%s)

    ON CONFLICT (telegram_id)

    DO UPDATE SET

        name=EXCLUDED.name,
        age=EXCLUDED.age,
        activity=EXCLUDED.activity,
        goal=EXCLUDED.goal,
        income=EXCLUDED.income,
        experience=EXCLUDED.experience

    """,

    (
        telegram_id,
        name,
        age,
        activity,
        goal,
        income,
        experience
    ))

    conn.commit()


def get_user(telegram_id):

    cursor.execute(
        "SELECT * FROM users WHERE telegram_id=%s",
        (telegram_id,)
    )

    return cursor.fetchone()


def get_day(telegram_id):

    cursor.execute(
        "SELECT day FROM users WHERE telegram_id=%s",
        (telegram_id,)
    )

    row = cursor.fetchone()

    if row:
        return row["day"]

    return 1


def next_day(telegram_id):

    cursor.execute(

        """
        UPDATE users

        SET day = day + 1

        WHERE telegram_id=%s
        """,

        (telegram_id,)
    )

    conn.commit()

def get_profile(telegram_id):

    cursor.execute(
        """
        SELECT
            name,
            goal,
            income,
            experience,
            day,
            level,
            xp,
            streak,
            achievements

        FROM users

        WHERE telegram_id=%s
        """,

        (telegram_id,)
    )

    return cursor.fetchone()

def add_xp(telegram_id, xp):

    cursor.execute(
        """
        UPDATE users

        SET xp = xp + %s

        WHERE telegram_id = %s
        """,

        (xp, telegram_id)
    )

    conn.commit()


def update_level(telegram_id):

    cursor.execute(
        """
        SELECT xp

        FROM users

        WHERE telegram_id=%s
        """,

        (telegram_id,)
    )

    row = cursor.fetchone()

    if not row:
        return

    xp = row["xp"]

    level = (xp // 100) + 1

    cursor.execute(

        """
        UPDATE users

        SET level=%s

        WHERE telegram_id=%s
        """,

        (level, telegram_id)
    )

    conn.commit()

def unlock_achievement(telegram_id, achievement):

    cursor.execute(
        """
        SELECT achievements

        FROM users

        WHERE telegram_id=%s
        """,

        (telegram_id,)
    )

    row = cursor.fetchone()

    if not row:
        return False

    current = row["achievements"] or ""

    items = [x for x in current.split(",") if x]

    if achievement in items:
        return False

    items.append(achievement)

    new_value = ",".join(items)

    cursor.execute(

        """
        UPDATE users

        SET achievements=%s

        WHERE telegram_id=%s
        """,

        (new_value, telegram_id)
    )

    conn.commit()

    return True

def get_achievements(telegram_id):

    cursor.execute(
        """
        SELECT achievements

        FROM users

        WHERE telegram_id=%s
        """,

        (telegram_id,)
    )

    row = cursor.fetchone()

    if not row:
        return []

    achievements = row["achievements"] or ""

    return [x for x in achievements.split(",") if x]