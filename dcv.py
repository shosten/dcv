import sqlite3

def get_user(user_name):
  conn = sqlite3.connect("users.db")
  cursor = conn.cursor()

  query = f"SELECT * FROM users WHERE username = '{user_name}'"
  cursor.execute(query);

  return cursor.fetchAll()
