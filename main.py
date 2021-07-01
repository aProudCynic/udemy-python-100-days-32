import smtplib
from datetime import datetime
import random

from secrets import (
    TEST_EMAIL_ACCOUNT_USERNAME,
    TEST_EMAIL_ACCOUNT_PASSWORD,
    TARGET_EMAIL_ADDRESS,
)


def today_is_thursday():
    return datetime.now().weekday() == 4


def send_mail(content):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=TEST_EMAIL_ACCOUNT_USERNAME, password=TEST_EMAIL_ACCOUNT_PASSWORD)
        connection.sendmail(
            from_addr=TEST_EMAIL_ACCOUNT_USERNAME,
            to_addrs=TARGET_EMAIL_ADDRESS,
            msg=content,
        )


def select_quote():
    with open('quotes.txt') as quote_file:
        lines = quote_file.read().splitlines()
        return random.choice(lines)


if today_is_thursday():
    quote = select_quote()
    send_mail(f"Subject:Quote for Thursday\n\n{quote}")
