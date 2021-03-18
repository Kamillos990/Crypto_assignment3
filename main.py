from Password import Password
from DatabaseManager import DatabaseManager
import sqlite3

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()
db = DatabaseManager()
db.create_table()


if __name__ == '__main__':
    username = input("Type in your username:")
    password1 = input("Type in password:")


    while True:
        if input('Repeat password ') == password1:
            print("Passwords match")
            break
        else:
            print('Passwords do not match. Please retry')


    p1 = Password(username, password1)
    db.addPassword(p1)
    p1.verifyPassword()
