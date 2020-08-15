#!/usr/bin/env python3
import os
from sendgrid.helpers.mail import Mail
from sendgrid import sendgrid

FROM_EMAIL = 'laknitti@gmail.com'
TEMPLATE_ID = 'd-1d636ed6725a4e4580be9410faa2e5b8'
TO_EMAILS = [('assignment@meyvan.com', 'Meyvan')]


def SendDynamic():
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAILS)
    message.template_id = TEMPLATE_ID
    try:
        sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        code, body, headers = response.status_code, response.body, response.headers
        print(f"Response code: {code}")
        print(f"Response headers: {headers}")
        print(f"Response body: {body}")
        print("Dynamic Messages Sent!")
    except Exception as e:
        print("Error: {0}".format(e))


if __name__ == "__main__":
    SendDynamic()
