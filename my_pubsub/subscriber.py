from google.cloud import pubsub_v1
from src.config import config as cfg
from src.mail import MailService
import json


class Subscriber:
    def __init__(self):
        self._subscriber = None
        self._subscription_path = None
        self.mail_service = MailService()

    def subscriber(self):
        if self._subscriber is None:
            self._subscriber = pubsub_v1.SubscriberClient()
            self._subscription_path = self._subscriber.subscription_path(cfg.get('pub-sub', 'PROJECT_ID'),
                                                                         cfg.get('pub-sub', 'SUBSCRIPTION_NAME'))
        return self._subscriber

    def callback(self, message):
        data = json.loads(message.data.decode())
        print(message.message_id, data)

        self.mail_service.send_mail(data)
        message.ack()

        print("Acknowledged message {}\n".format(message.message_id))

    def subscribe_message(self):
        # Limit the subscriber to only have ten outstanding messages at a time.
        flow_control = pubsub_v1.types.FlowControl(max_messages=1)
        streaming_pull_future = self.subscriber().subscribe(
            self._subscription_path, callback=self.callback, flow_control=flow_control
        )
        # Calling result() on StreamingPullFuture keeps the main thread from
        # exiting while messages get processed in the callbacks.
        try:
            streaming_pull_future.result()
        except Exception as err:
            streaming_pull_future.cancel()
            raise Exception(err)
