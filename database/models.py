from flask_login import UserMixin
from database.db import get_db

class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = str(id)   # MUST be string
        self.username = username
        self.role = role

    @staticmethod
    def get_by_username(username):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cur.fetchone()
        conn.close()
        return user

    @staticmethod
    def get_by_id(user_id):
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id=?", (user_id,))
        user = cur.fetchone()
        conn.close()
        if user:
            return User(user[0], user[1], user[3])
        return None
