import unittest
import random_generator
import random_generator.poland
import random_generator.germany


class Test(unittest.TestCase):
    def test_number_generator(self):
        generator = random_generator.number(15)
        self.assertEqual(len(generator), 15)

    def test_string_generator(self):
        generator = random_generator.string(15)
        self.assertEqual(len(generator), 15)
        self.assertTrue(all(s.isalpha() for s in generator))

    def test_poland_pesel(self):
        self.assertTrue(self._validate_pesel(random_generator.poland.pesel()))
        self.assertTrue(self._validate_pesel(random_generator.poland.pesel()))
        self.assertTrue(self._validate_pesel(random_generator.poland.pesel()))
        self.assertTrue(self._validate_pesel(random_generator.poland.pesel()))
        self.assertTrue(self._validate_pesel(random_generator.poland.pesel()))

    def test_germany_vat(self):
        self.assertTrue(self._validate_german_vat(random_generator.germany.vat()))
        self.assertTrue(self._validate_german_vat(random_generator.germany.vat()))
        self.assertTrue(self._validate_german_vat(random_generator.germany.vat()))
        self.assertTrue(self._validate_german_vat(random_generator.germany.vat()))
        self.assertTrue(self._validate_german_vat(random_generator.germany.vat()))

    @staticmethod
    def _validate_german_vat(vat_number):
        if not vat_number.startswith("DE") or len(vat_number) != 11:
            return False
        return vat_number[2:].isdigit()

    @staticmethod
    def _validate_pesel(pesel):
        if len(pesel) != 11 or not pesel.isdigit():
            return False  # Sprawdza czy PESEL ma 11 cyfr i składa się tylko z cyfr

        # Dekomponowanie PESEL
        year = int(pesel[0:2])
        month = int(pesel[2:4])
        day = int(pesel[4:6])
        series = pesel[6:10]  # Seria i płeć
        control_digit = int(pesel[10])

        # Korygowanie roku i miesiąca w zależności od wieku
        if 81 <= month <= 92:
            year += 1800
            month -= 80
        elif 1 <= month <= 12:
            year += 1900
        elif 21 <= month <= 32:
            year += 2000
            month -= 20
        elif 41 <= month <= 52:
            year += 2100
            month -= 40
        elif 61 <= month <= 72:
            year += 2200
            month -= 60
        else:
            return False  # Miesiąc poza zakresem oznacza niepoprawny PESEL

        # Sprawdzanie poprawności daty
        from datetime import datetime
        try:
            datetime(year, month, day)
        except ValueError:
            return False

        # Obliczenie cyfry kontrolnej
        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        expected_control_digit = sum(w * int(num) for w, num in zip(weights, pesel[:10])) % 10
        expected_control_digit = (10 - expected_control_digit) % 10

        return expected_control_digit == control_digit