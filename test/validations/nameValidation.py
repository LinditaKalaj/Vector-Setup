import unittest
import gui


class NameValidationTest(unittest.TestCase):

    def setUp(self):
        self.test_gui = gui.Window()

    def test_common_name(self):
        self.test_gui.nameEntry.insert(0, "Vector-C4W1")
        self.assertEqual("Vector-C4W1", self.test_gui.validate_name())  # Vector-XXXX == Vector-XXXX

    def test_lower_case_vector(self):
        self.test_gui.nameEntry.insert(0, "vector-C4W1")
        self.assertEqual("Vector-C4W1", self.test_gui.validate_name())  # vector-XXXX == Vector-XXXX

    def test_upper_case_vector(self):
        self.test_gui.nameEntry.insert(0, "VECTOR-C4W1")
        self.assertEqual("Vector-C4W1", self.test_gui.validate_name())  # VECTOR-XXXX == Vector-XXXX

    def test_no_vector(self):
        self.test_gui.nameEntry.insert(0, "C4W1")
        self.assertEqual("Vector-C4W1", self.test_gui.validate_name())  # XXXX == Vector-XXXX

    def test_no_vector_lower_case(self):
        self.test_gui.nameEntry.insert(0, "t4jh")
        self.assertEqual("Vector-T4JH", self.test_gui.validate_name())  # xxxx == Vector-XXXX

    def test_misspelling(self):
        self.test_gui.nameEntry.insert(0, "Victor-53rf")
        self.assertIsNone(self.test_gui.validate_name())  # "Victor-XXXX" == None

    def test_misspelling_2(self):
        self.test_gui.nameEntry.insert(0, "V-53rf")
        self.assertIsNone(self.test_gui.validate_name())  # "V-XXXX" == None

    def test_mixed_case(self):
        self.test_gui.nameEntry.insert(0, "VeCtor-kb4f")
        self.assertIsNone(self.test_gui.validate_name())  # "VeCtor-XXXX" == None

    def test_mixed_case_2(self):
        self.test_gui.nameEntry.insert(0, "5gS3")
        self.assertEqual("Vector-5GS3", self.test_gui.validate_name())  # "5gS3" == "Vector-5GS3"

    def test_lowercase_no_vector(self):
        self.test_gui.nameEntry.insert(0, "ffff")
        self.assertEqual("Vector-FFFF", self.test_gui.validate_name())  # "xxxx" == "Vector-XXXX"

    def test_no_chars(self):
        self.test_gui.nameEntry.insert(0, "")
        self.assertIsNone(self.test_gui.validate_name())  # "" == None

    def test_too_many_chars(self):
        self.test_gui.nameEntry.insert(0, "5rv2d")
        self.assertIsNone(self.test_gui.validate_name())  # "xxxxx" == None"

    def test_too_many_chars_with_vector(self):
        self.test_gui.nameEntry.insert(0, "Vector-hgt4h")
        self.assertIsNone(self.test_gui.validate_name())  # "Vector-xxxxx" == None

    def test_no_dash(self):
        self.test_gui.nameEntry.insert(0, "Vector ge47")
        self.assertEqual("Vector-GE47", self.test_gui.validate_name())  # "Vector ge47" == "Vector-GE47"

    def test_no_dash_2(self):
        self.test_gui.nameEntry.insert(0, "Vector_wowo")
        self.assertEqual("Vector-WOWO", self.test_gui.validate_name())  # "Vector_wowo" == "Vector-WOWO"

    def test_no_dash_3(self):
        self.test_gui.nameEntry.insert(0, "Vector~4pW7")
        self.assertEqual("Vector-4PW7", self.test_gui.validate_name())  # "Vector~4pW7" == "Vector-4PW7"

    def test_no_space(self):
        self.test_gui.nameEntry.insert(0, "Vectorfrw3")
        self.assertIsNone(self.test_gui.validate_name())  # "Vectorfrw3" == "None"

    def test_no_space_2(self):
        self.test_gui.nameEntry.insert(0, "Vector\tfrw3")
        self.assertEqual("Vector-FRW3", self.test_gui.validate_name())  # "Vector   frw3" == "Vector-FRW3"

    def test_alpha_char(self):
        self.test_gui.nameEntry.insert(0, "goes")
        self.assertEqual("Vector-GOES", self.test_gui.validate_name())  # "goes" == "Vector-GOES"

    def test_numeric(self):
        self.test_gui.nameEntry.insert(0, "4626")
        self.assertEqual("Vector-4626", self.test_gui.validate_name())  # "4626" == "Vector-4626"

    def test_non_alnum(self):
        self.test_gui.nameEntry.insert(0, "-34rd")
        self.assertIsNone(self.test_gui.validate_name())   # "-3rd" == None

    def test_non_alnum_2(self):
        self.test_gui.nameEntry.insert(0, "~=+@")
        self.assertIsNone(self.test_gui.validate_name())   # "~=+@" == None

    def test_non_alnum_3(self):
        self.test_gui.nameEntry.insert(0, "-546")
        self.assertIsNone(self.test_gui.validate_name())   # "-546" == None


if __name__ == '__main__':
    unittest.main()
