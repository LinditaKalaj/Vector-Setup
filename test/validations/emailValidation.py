import unittest
import gui

'''
simple email validation, not the most robust
'''


class EmailValidation(unittest.TestCase):

    def setUp(self):
        self.test_gui = gui.Window()

    def test_common_email(self):
        self.test_gui.emailEntry.insert(0, "hello@gmail.com")
        self.assertEqual("hello@gmail.com", self.test_gui.validate_email())

    def test_invalid_domain(self):
        self.test_gui.emailEntry.insert(0, "someemail@.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_domain_2(self):
        self.test_gui.emailEntry.insert(0, "someemail@..com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_domain_3(self):
        self.test_gui.emailEntry.insert(0, "nodomain@.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_domain_4(self):
        self.test_gui.emailEntry.insert(0, "space@na sa.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_domain_5(self):
        self.test_gui.emailEntry.insert(0, "newline@new\nsunday.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_top_lvl_domain(self):
        self.test_gui.emailEntry.insert(0, "anotheremail@google.")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_top_lvl_domain_2(self):
        self.test_gui.emailEntry.insert(0, "email3@yahoo.c")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_top_lvl_domain_3(self):
        self.test_gui.emailEntry.insert(0, "eww@ghotmail")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_top_lvl_domain_4(self):
        self.test_gui.emailEntry.insert(0, "equals@lake.==")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_top_lvl_domain_5(self):
        self.test_gui.emailEntry.insert(0, "kevin@spacey.c o")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_top_lvl_domain_6(self):
        self.test_gui.emailEntry.insert(0, "nonewline@gmail.c\n")
        self.assertIsNone(self.test_gui.validate_email())

    def test_top_lvl_domain(self):
        self.test_gui.emailEntry.insert(0, "amail@country.co.uk")
        self.assertEqual("amail@country.co.uk", self.test_gui.validate_email())

    def test_top_lvl_domain_2(self):
        self.test_gui.emailEntry.insert(0, "ooo.ahhh@acha.co")
        self.assertEqual("ooo.ahhh@acha.co", self.test_gui.validate_email())

    def test_invalid_local_name(self):
        self.test_gui.emailEntry.insert(0, "acha.@gmail.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_local_name_2(self):
        self.test_gui.emailEntry.insert(0, ".acha@gmail.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_local_name_3(self):
        self.test_gui.emailEntry.insert(0, "hehe~acha@gmail.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_local_name_4(self):
        self.test_gui.emailEntry.insert(0, "lalala\n@gmail.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_local_name_5(self):
        self.test_gui.emailEntry.insert(0, "spacing @nasa.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_invalid_local_name_6(self):
        self.test_gui.emailEntry.insert(0, "wherego.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_at_sign(self):
        self.test_gui.emailEntry.insert(0, "imampedup.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_at_sign_2(self):
        self.test_gui.emailEntry.insert(0, "imamped&up.com")
        self.assertIsNone(self.test_gui.validate_email())

    def test_no_special_chars(self):
        self.test_gui.emailEntry.insert(0, "wowowewagmailcom")
        self.assertIsNone(self.test_gui.validate_email())

    def test_blank(self):
        self.test_gui.emailEntry.insert(0, "")
        self.assertIsNone(self.test_gui.validate_email())



