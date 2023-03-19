import unittest
import gui

'''
Only testing if ip matches format of XXX.XXX.XXX.XXX
where x can appear 1 to 3 times per section and x is a number between 0-9
function does not care if an ip is valid, as long as it follows the same format
'''


class IpValidationTest(unittest.TestCase):

    def setUp(self):
        self.test_gui = gui.Window()

    def test_common_ip(self):
        self.test_gui.ipEntry.insert(0, "192.168.1.1")
        self.assertEqual("192.168.1.1", self.test_gui.validate_ip())

    def test_common_ip_all_filled(self):
        self.test_gui.ipEntry.insert(0, "192.168.001.001")
        self.assertEqual("192.168.001.001", self.test_gui.validate_ip())

    def test_common_ip_with_one_per_section(self):
        self.test_gui.ipEntry.insert(0, "2.8.1.1")
        self.assertEqual("2.8.1.1", self.test_gui.validate_ip())

    def test_ip6(self):
        self.test_gui.ipEntry.insert(0, "FE80:CD00:0000:0CDE:1257:0000:211E:729C")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_ip_alpha(self):
        self.test_gui.ipEntry.insert(0, "afv.bjt.hsc.dgd")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_ip_alpha_mixed(self):
        self.test_gui.ipEntry.insert(0, "a11.b35.c64.d24")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_ip_alpha_at_least_1(self):
        self.test_gui.ipEntry.insert(0, "192.168.531.24d")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_extra_nums(self):
        self.test_gui.ipEntry.insert(0, "192.168.5341.245")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_extra_nums_2(self):
        self.test_gui.ipEntry.insert(0, "1522.1922.5361.2745")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_extra_decimal_nums(self):
        self.test_gui.ipEntry.insert(0, "192.168.531.245.424")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_extra_decimal_nums_2(self):
        self.test_gui.ipEntry.insert(0, "192.168.531.245.124.38")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_not_enough_decimal_nums(self):
        self.test_gui.ipEntry.insert(0, "192.168.531")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_not_enough_decimal_nums_2(self):
        self.test_gui.ipEntry.insert(0, "192.168")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_not_enough_decimal_nums_3(self):
        self.test_gui.ipEntry.insert(0, "192")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_not_enough_decimal_nums_4(self):
        self.test_gui.ipEntry.insert(0, "")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_no_decimal(self):
        self.test_gui.ipEntry.insert(0, "19216811")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_decimal_wrong_place(self):
        self.test_gui.ipEntry.insert(0, "19216811....")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_non_decimal(self):
        self.test_gui.ipEntry.insert(0, "192,168,1,1")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_non_decimal_2(self):
        self.test_gui.ipEntry.insert(0, "192:168:1:1")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_not_enough_decimal(self):
        self.test_gui.ipEntry.insert(0, "192.168.001001")
        self.assertIsNone(self.test_gui.validate_ip())

    def test_no_numbers(self):
        self.test_gui.ipEntry.insert(0, "....")
        self.assertIsNone(self.test_gui.validate_ip())
