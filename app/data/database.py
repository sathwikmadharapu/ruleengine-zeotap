import sqlite3

def initialize_db():
    conn = sqlite3.connect('rules.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rules (id INTEGER PRIMARY KEY, rule_string TEXT)''')
    conn.commit()
    conn.close()
