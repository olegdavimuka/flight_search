import smtplib
from twilio.rest import Client

TWILIO_SID = "ACb499837ac7d6f445bfadce6805236697"
TWILIO_AUTH_TOKEN = "7e06f8b54c629da0c1394f6d8af0a9ff"
TWILIO_VIRTUAL_NUMBER = "+18456713421"
TWILIO_VERIFIED_NUMBER = "+3805051936522"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "olegdavimuka0@gmail.com"
MY_PASSWORD = "vkNyrNd6#Y^b5ChW9l4N&&gPKaJV%hot@JNbAm4KbSowN3^fZS"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    @staticmethod
    def send_emails(emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS, port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
