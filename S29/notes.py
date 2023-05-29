import sqlite3
from pathlib import Path

ROOT = Path(__file__).parent
DB_FILE = ROOT/"db1.sqlite"

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute("SELECT * FROM users")

print(cursor.fetchall())
