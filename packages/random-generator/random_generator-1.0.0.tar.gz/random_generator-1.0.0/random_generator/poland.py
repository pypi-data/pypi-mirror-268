import random as random_libs
import datetime as datetime_libs


def pesel():
    start_date = datetime_libs.datetime(1900, 1, 1)
    end_date = datetime_libs.datetime(1999, 12, 31)
    random_date = start_date + datetime_libs.timedelta(days=random_libs.randint(0, (end_date - start_date).days))
    year = random_date.year % 100
    month = random_date.month
    day = random_date.day

    if 1800 <= random_date.year <= 1899:
        month += 80
    elif 2000 <= random_date.year <= 2099:
        month += 20
    elif 2100 <= random_date.year <= 2199:
        month += 40
    elif 2200 <= random_date.year <= 2299:
        month += 60

    series_and_sex = random_libs.randint(1000, 9999)
    pesel_without_control = f"{year:02d}{month:02d}{day:02d}{series_and_sex}"
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    control_number = sum(w * int(num) for w, num in zip(weights, pesel_without_control)) % 10
    control_digit = (10 - control_number) % 10
    return f"{pesel_without_control}{control_digit}"


def nip():
    nip_number = [random_libs.randint(0, 9) for _ in range(9)]

    weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
    control_sum = sum(w * n for w, n in zip(weights, nip_number))
    control_digit = control_sum % 11

    if control_digit == 10:
        return nip()

    nip_number.append(control_digit)

    return ''.join(str(num) for num in nip_number)