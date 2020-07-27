import unittest
from Reader import Reader

PATH = "/home/fir3destr0yer/PycharmProjects/pythonReader/"

#Class designed for testing the Reader
class TestReader(unittest.TestCase):

    #Test correctness
    def test_path(self):
        obj = Reader()
        self.assertIsInstance(obj.readFile(PATH + "test_reader.csv"),str)

    #Test if it catches the wrong emails
    def test_email(self):
        obj = Reader()
        self.assertRaises(Exception, lambda: obj.readFile(PATH + "test_reader_email.csv"))

    #Test if it catches the wrong genders
    def test_gender(self):
        obj = Reader()
        self.assertRaises(Exception, lambda: obj.readFile(PATH + "test_reader_gender.csv"))

    #Test if it catches the wrong birthdays
    def test_date(self):
        obj = Reader()
        self.assertRaises(Exception, lambda: obj.readFile(PATH + "test_reader_date.csv"))


if __name__ == '__main__':
    unittest.main()
