import smtplib
from email.mime.text import MIMEText
from src.config import config as cfg
from jinja2 import Environment, FileSystemLoader


class MailService:
    def __init__(self):
        self.server = cfg.get('email', 'MAIL_SERVER')
        self.port = cfg.get('email', 'MAIL_PORT')
        self.username = cfg.get('email', 'MAIL_USERNAME')
        self.password = cfg.get('email', 'MAIL_PASSWORD')
        self.sender = cfg.get('email', 'MAIL_SENDER')
        self.env = Environment(loader=FileSystemLoader(cfg.get('email', 'TEMPlATE_PATH')))
        self._mail = None

    def mail(self):
        if self._mail is None:
            self._mail = smtplib.SMTP_SSL(self.server)
            self._mail.connect(self.server, self.port)
            self._mail.login(self.username, self.password)
        return self._mail

    def get_msg(self, email_type, to, subject, user_name=None, link=None, newsletter_data=None):
        try:

            template_name = '{}.html'.format(email_type)
            template = self.env.get_template(template_name)
            output = template.render(user_name=user_name, link=link, newsletter_data=newsletter_data)
            message = MIMEText(output, "html")
            message['Subject'] = subject
            message['From'] = self.sender
            message['To'] = to
            return message
        except Exception as e:
            return str(e)

    def send_mail(self, data):
        try:
            email_type, email_id, user_name, subject = data['email_type'], data['email_id'], data['user_name'], \
                                                       data['subject']
            link = data["link"] if 'link' in data else None
            newsletter_data = data["newsletter_data"] if 'newsletter_data' in data else None
            msg = self.get_msg(email_type, email_id, subject, user_name, link, newsletter_data)
            self.mail().sendmail(self.sender, email_id, msg.as_string())
        except Exception as err:
            print(err)
            raise Exception(err)
