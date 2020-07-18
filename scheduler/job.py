from src.push import driver
from rest_api.get_user_subscriptions import get_user_subscriptions
from rest_api.get_sub_content import get_content
from src.mail import MailService


def job_function():
    driver()


# cron testing function
def job_function1():
    subscription_data = get_user_subscriptions()
    for user_data in subscription_data:
        user_name = user_data[0]
        email_id = user_data[1]
        feed_data = user_data[2]
        newsletter_data = get_content(feed_data)
        pub_data = {"email_type": "subscribe_newsletter_child",
                    "user_name": user_name,
                    "email_id": email_id,
                    "newsletter_data": newsletter_data,
                    "subject": "Subscribe Newsletter"}

        mail_service = MailService()
        mail_service.send_mail(pub_data)
    print("mail sent")
