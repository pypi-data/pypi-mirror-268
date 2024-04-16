import random as random_libs


def vat():
    numbers = [random_libs.randint(0, 9) for _ in range(9)]
    vat_number = "DE" + ''.join(str(num) for num in numbers)
    return vat_number
