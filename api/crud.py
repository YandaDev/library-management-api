from .database import conn

cursor = conn.cursor(dictionary=True)

def get_all_members():
    cursor.execute("SELECT * FROM members")
    return cursor.fetchall()

def create_member(name, email):
    cursor.execute("INSERT INTO members (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    return {"id": cursor.lastrowid, "name": name, "email": email}