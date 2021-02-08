"""
This online tool helps to test HMAC values:
https://www.freeformatter.com/hmac-generator.html#ad-output
"""


import datetime
import hashlib
import hmac
import pytz


def today_in_uk():
    utc = pytz.timezone('Etc/UTC')
    uk = pytz.timezone('Europe/London')

    return uk.localize(datetime.datetime.now()).astimezone(utc).date()


def date_to_digits(date, secret_key, num_digits):
    """
    date_to_digits calculates a daily access code e.g. 123456 from a date and a secret key.
    It's can generate an "emergency" code for a door entry system that changes every day and
    that cannot be predicted without the secret.

    it generates a SHA-256 HMAC of the date in iso format (e.g. `2021-02-08`) using the provided
    secret_key and converts the output bytes to decimal digits.
    """

    hmac_bytes = calculate_date_hmac(date, secret_key)

    return bytes_to_digits(hmac_bytes, num_digits)


def calculate_date_hmac(d, secret_key):
    date_string = d.isoformat().encode('UTF-8')
    digest_maker = hmac.new(secret_key.encode('UTF-8'), date_string, hashlib.sha256)
    return digest_maker.digest()


def bytes_to_digits(bs, num_digits):
    digits = []
    bs = [b for b in bs]

    for i in range(0, num_digits):
        while True:
            try:
                next_byte = bs.pop(0)
            except IndexError:
                raise RanOutOfBytesError()

            if next_byte > 249:
                continue
            break

        digits.append(next_byte % 10)

    return digits


class RanOutOfBytesError(Exception):
    pass
