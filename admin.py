import sqlite3

DATABASE = 'database.db'

def get_admin_users():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email FROM users WHERE is_admin = 1")
    admins = cursor.fetchall()

    if not admins:
        print("No admin users found.")
    else:
        for admin in admins:
            print(f"ID: {admin['id']}, Name: {admin['name']}, Email: {admin['email']}")

    conn.close()

if __name__ == '__main__':
    get_admin_users()
