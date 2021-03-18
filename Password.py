import hashlib
import logging
import os
import sqlite3



class Password:
    """
    Class that will be saved in database


    ...

    Attributes
    ----------
    username : str
        username to which we assign password and salt, let's us verify passwords using this attribute
    salt : str
        salt generated while creating Password class instance used to "salt" the password
    password: str
        password provided by the user ,later salted , hashed and added to database

    Methods
    -------
    __init__(self, username: str, password: str):
        Constructor of Password class instance

    get_salt(self):
        getter of salt attribute value, returns salt value

    get_username(self):
        getter of username attribute value, returns username value

    get_password(self):
        getter of password attribute value, returns password value

    hashPassword(self, password: str, salt: str):
        returns hashed password

    verifyPassword(self):
        verifies password of provided username

    """

    def __init__(self, username: str, password: str):
        self.username = username
        self.salt = os.urandom(16)
        self.password = self.hashPassword(password, self.salt)
    

    def get_salt(self):
        return self.salt

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def hashPassword(self, password: str, salt: str):
        hashedpassword = hashlib.pbkdf2_hmac(
            'sha256',
            str.encode(password),
            salt,
            100000  # It is recommended to use at least 100,000 iterations of SHA-256
        )
        return hashedpassword.hex()

    def verifyPassword(self):
         logging.info("Verifying password.")
         login = input("Type in your login: ")
         password = input("Type in your password: ")
         conn = sqlite3.connect('passwords.db')
         cursor = conn.cursor()
         cursor.execute("SELECT password FROM passwords WHERE username = ?", [login])
         passwordcheck = cursor.fetchone()[0]
         cursor.execute("SELECT salt FROM passwords WHERE username = ?", [login])
         saltcheck = cursor.fetchone()[0]
         new_hash = self.hashPassword(password, saltcheck)

         if passwordcheck == new_hash:
             print("Password is correct.")
         else:
             logging.error("Password is not correct")


