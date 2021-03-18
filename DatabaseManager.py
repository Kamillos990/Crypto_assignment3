import sqlite3
import logging
from Password import Password


class DatabaseManager:
    """
        Class managing passwords in database

        Methods
        -------
        def create_table(self):
            connects with database and checks if the table has been created. If not creates it

        def addPassword(self, password: Password):
            connects with database and inserts hashed password along with username and salt to database
        """

    logger = logging.getLogger('database')
    logging.basicConfig(level=logging.DEBUG)





    def create_table(self):
        conn = sqlite3.connect('passwords.db')

        cursor = conn.cursor()
        try:
            #
            cursor.execute('''SELECT count(*) FROM sqlite_master WHERE type='table' AND name='passwords' ''')

            if cursor.fetchone()[0] == 0:
                print("Passwords table doesn't exist, creating")
                cursor.execute("""CREATE TABLE passwords (username text, password text, salt text)""")
                conn.commit()
                self.logger.info('Table succesfully created')
            else:
                self.logger.info('Table already exists')

        except Exception as e:
            self.logger.info('Error ocurred while creating database table \nError: %s' % e)

        conn.close()

    def addPassword(self, password: Password):
        conn = sqlite3.connect('passwords.db')
        cursor = conn.cursor()

        print(password.password)
        query = ''' INSERT INTO passwords (username, password, salt) VALUES (?,?,?)'''
        cursor.execute(query, (password.username, password.password, password.salt))
        conn.commit()
