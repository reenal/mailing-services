from my_pubsub.publisher import Publisher


def driver():
    publisher = Publisher()
    pub_data = {"email_type": "password_reset",
                "user_name": "prasanth93",
                "email_id": "reenalboddul@gmail.com",
                "link": "https://www.w3schools.com/",
                "subject": "Testing reset password"}
    publisher.publish_message(pub_data)

    '''pub_data = {"email_type": "account_activation",  
                "user_name": "prasanth93",
                "email_id": "rsunny1993@gmail.com",
                "link": "https://www.w3schools.com/",
                "subject": "Testing account activation"}
     publisher.publish_message(pub_data)'''


driver()
