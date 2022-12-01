
def convert_number_to_string(phone_number):
    return str(phone_number)

def get_first_3_digits(phone_number):
    converted_number = convert_number_to_string(phone_number)
    area_code = converted_number[0:3]
    return area_code

def get_middle_digits(phone_number):
    converted_number = convert_number_to_string(phone_number)
    middle_numbers = converted_number[3:6]
    return middle_numbers

def get_last_4_digits(phone_number):
    converted_number = convert_number_to_string(phone_number)
    end_numbers = converted_number[6:]
    return end_numbers

def get_correct_format(phone_number):
    area_code = get_first_3_digits(phone_number)
    middle_digits = get_middle_digits(phone_number)
    end_numbers = get_last_4_digits(phone_number)
    return f"({area_code}) {middle_digits}-{end_numbers}"
