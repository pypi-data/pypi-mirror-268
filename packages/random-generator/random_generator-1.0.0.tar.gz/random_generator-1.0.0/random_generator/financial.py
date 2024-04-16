import random as random_libs


def credit_card(issuer):
    def calculate_luhn(number):
        def digits_of(n):
            return [int(d) for d in str(n)]

        processed_digits = []
        for i, digit in enumerate(reversed(number)):
            if i % 2 == 0:
                processed_digits.extend(digits_of(digit * 2))
            else:
                processed_digits.append(digit)

        total_sum = sum(processed_digits)
        control_digit = (10 - total_sum % 10) % 10
        return control_digit

    if issuer.lower() == 'visa':
        prefix = random_libs.choice([4])
        length = 16
    elif issuer.lower() == 'mastercard':
        prefix = random_libs.choice([51, 52, 53, 54, 55])
        length = 16
    elif issuer.lower() == 'american express':
        prefix = random_libs.choice([34, 37])
        length = 15
    else:
        return None

    partial_number = [int(x) for x in str(prefix)]
    while len(partial_number) < (length - 1):
        partial_number.append(random_libs.randint(0, 9))
    control_digit = calculate_luhn(partial_number)
    return ''.join(map(str, partial_number)) + str(control_digit)


def iban(country_code='PL'):
    def generate_national_bank_account_number():
        return ''.join(str(random_libs.randint(0, 9)) for _ in range(24))

    def calculate_iban_check_digits(country_code, national_bank_account_number):
        country_code_numbers = ''.join(str(ord(char) - 55) for char in country_code)
        check_string = national_bank_account_number + country_code_numbers + '00'
        check_digits = 98 - (int(check_string) % 97)
        return f"{check_digits:02d}"

    national_number = generate_national_bank_account_number()
    check_digits = calculate_iban_check_digits(country_code, national_number)
    return f"{country_code}{check_digits}{national_number}"
