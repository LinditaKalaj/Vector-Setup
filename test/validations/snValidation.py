import unittest
import gui

'''
Testing sn which should be 8 alphanumeric characters long
'''


class NameValidationTest(unittest.TestCase):

    def setUp(self):
        self.test_gui = gui.Window()

    def test_lower_sn_alphanumeric(self):
        self.test_gui.snEntry.insert(0, "0dd83jff")
        self.assertEqual("0dd83jff", self.test_gui.validate_sn())

    def test_mixed_case_alphanumeric(self):
        self.test_gui.snEntry.insert(0, "0DfG19ek")
        self.assertEqual("0dfg19ek", self.test_gui.validate_sn())

    def test_all_caps_alphanumeric(self):
        self.test_gui.snEntry.insert(0, "GEG42FV3")
        self.assertEqual("geg42fv3", self.test_gui.validate_sn())

    def test_lower_alpha(self):
        self.test_gui.snEntry.insert(0, "giwlviwn")
        self.assertEqual("giwlviwn", self.test_gui.validate_sn())

    def test_caps_alpha(self):
        self.test_gui.snEntry.insert(0, "HRJSVUFS")
        self.assertEqual("hrjsvufs", self.test_gui.validate_sn())

    def test_mixed_alpha(self):
        self.test_gui.snEntry.insert(0, "HfWvHTwO")
        self.assertEqual("hfwvhtwo", self.test_gui.validate_sn())

    def test_numeric(self):
        self.test_gui.snEntry.insert(0, "57935028")
        self.assertEqual("57935028", self.test_gui.validate_sn())

    def test_non_alphanumeric(self):
        self.test_gui.snEntry.insert(0, "ff3-tj6v")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_non_alphanumeric_2(self):
        self.test_gui.snEntry.insert(0, "h05jhg7 ")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_non_alphanumeric_3(self):
        self.test_gui.snEntry.insert(0, " g2uc5s9")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_non_alphanumeric_4(self):
        self.test_gui.snEntry.insert(0, "        ")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_non_alphanumeric_5(self):
        self.test_gui.snEntry.insert(0, "\t8bsapb0")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_non_alphanumeric_6(self):
        self.test_gui.snEntry.insert(0, "niek652\n")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_none(self):
        self.test_gui.snEntry.insert(0, "")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_too_short_alphanumeric(self):
        self.test_gui.snEntry.insert(0, "g93kg0d")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_too_short_numeric(self):
        self.test_gui.snEntry.insert(0, "567930")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_too_short_alpha(self):
        self.test_gui.snEntry.insert(0, "pwkveqa")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_too_long_alphanumeric(self):
        self.test_gui.snEntry.insert(0, "rg92mgow0")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_too_long_alpha(self):
        self.test_gui.snEntry.insert(0, "pgiwlvjao")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_too_long_numeric(self):
        self.test_gui.snEntry.insert(0, "395068395")
        self.assertIsNone(self.test_gui.validate_sn())

    def test_upsidedown(self):
        self.test_gui.snEntry.insert(0, "sdᴉɯǝɹo˥")
        self.assertIsNone(self.test_gui.validate_sn())