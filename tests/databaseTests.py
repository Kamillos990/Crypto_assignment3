import unittest
import sqlite3
from DatabaseManager import DatabaseManager
from Password import Password

conn = sqlite3.connect('passwords.db')
cursor = conn.cursor()

class MyTestCase(unittest.TestCase):



    def testPasswordTableCreation(self):
        db = DatabaseManager()
        db.create_table()

        cursor.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')
        assert cursor.fetchone()[0] == 1

    def testPasswordInsert(self):
        db = DatabaseManager()
        passwd = Password("Kamil", "Dumbass")
        db.addPassword(passwd)
        cursor.execute("SELECT password FROM passwords WHERE username = ?", [passwd.username])
        passwordcheck = cursor.fetchone()[0]
        assert passwordcheck != 0