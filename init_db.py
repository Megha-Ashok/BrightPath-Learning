import sqlite3
from werkzeug.security import generate_password_hash

def initialize_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Drop and recreate the users table
    c.execute("DROP TABLE IF EXISTS users")

    c.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            is_admin INTEGER DEFAULT 0
        )
    ''')

    # Insert default admin user
    c.execute('''
        INSERT INTO users (name, email, password, is_admin)
        VALUES (?, ?, ?, ?)
    ''', (
        "Admin User",
        "megharashokashok@gmail.com",
        generate_password_hash("Megha@591970"),
        1
    ))

    conn.commit()
    conn.close()
    print("✅ Database initialized with admin user.")

if __name__ == '__main__':
    initialize_db()
