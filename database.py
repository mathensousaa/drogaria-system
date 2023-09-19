import sqlite3

conn = sqlite3.connect('drogaria.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
''')
conn.commit()
conn.close()