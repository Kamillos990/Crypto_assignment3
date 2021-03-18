import unittest
from Password import Password


class MyTestCase(unittest.TestCase):
    def test_init(self):
        username = "Kamil"
        password = "Dumbass"
        pswd = Password(username, password)

        self.assertIsInstance(pswd, Password)

    def test_hashPassword(self):
        username = "Kamil"
        password = "Dumbass"
        pswd = Password(username, password)

        assert pswd.password != "Dumbass"



