import psycopg2

conn = psycopg2.connect(
    dbname="snake",
    user="postgres",
    password="erten2007",  
    port="5432"
)
cur = conn.cursor()

# Таблица пользователей
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    level INTEGER DEFAULT 1
)
""")

# Таблица результатов
cur.execute("""
CREATE TABLE IF NOT EXISTS user_scores (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    score INTEGER,
    level INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Таблица сохранённых состояний игры
cur.execute("""
CREATE TABLE IF NOT EXISTS saved_state (
    user_id INTEGER PRIMARY KEY REFERENCES users(id) ON DELETE CASCADE,
    snake TEXT,
    direction TEXT,
    score INTEGER,
    level INTEGER
)
""")

conn.commit()
cur.close()
conn.close()

print("Все таблицы успешно созданы!")
