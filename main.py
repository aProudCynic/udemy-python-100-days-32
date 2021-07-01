import smtplib
from secrets import (
    TEST_EMAIL_ACCOUNT_USERNAME,
    TEST_EMAIL_ACCOUNT_PASSWORD,
    TARGET_EMAIL_ADDRESS,
)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=TEST_EMAIL_ACCOUNT_USERNAME, password=TEST_EMAIL_ACCOUNT_PASSWORD)
    connection.sendmail(
        from_addr=TEST_EMAIL_ACCOUNT_USERNAME,
        to_addrs=TARGET_EMAIL_ADDRESS,
        msg="Subject:Hello\n\nHello",
    )
