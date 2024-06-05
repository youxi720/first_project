import sqlite3

def init_db():
    connection = sqlite3.connect('compliments.db')
    with connection:
        connection.execute('''
            CREATE TABLE compliments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL
               )
         ''')
    print("Database initialized.")

if __name__ == "__main__":
    init_db()