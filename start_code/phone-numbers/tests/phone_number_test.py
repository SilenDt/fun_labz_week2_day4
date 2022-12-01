import unittest
from src.phone_number import *

class TestPhoneNumber(unittest.TestCase):

    def setUp(self):
        self.phone_number = 1234567890

    def test_convert_phone_number_to_string(self):
        self.assertEqual("1234567890", str(self.phone_number))

    def test_get_first_3_digits(self):
        convert_number_to_string(self.phone_number)
        area_code = get_first_3_digits(self.phone_number)
        self.assertEqual("123", area_code)
    
    def test_get_middle_digits(self):
        convert_number_to_string(self.phone_number)
        middle_digits = get_middle_digits(self.phone_number)
        self.assertEqual("456", middle_digits)
    
    def test_get_last_4_digits(self):
        convert_number_to_string(self.phone_number)
        last_4_digits = get_last_4_digits(self.phone_number)
        self.assertEqual("7890", last_4_digits)

    def test_get_correct_format(self):
        get_first_3_digits(self.phone_number)
        get_middle_digits(self.phone_number)
        get_last_4_digits(self.phone_number)
        formatted_phone_number = get_correct_format(self.phone_number)
        self.assertEqual("(123) 456-7890", formatted_phone_number)





    # def get_formated_phone_number(self):
    #     formatted_number = format_number(self.phone_number)
    #     self.assertEqual("(123) 456-7890", formatted_number)