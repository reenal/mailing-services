from google.cloud import pubsub_v1
from src.config import config as cfg
import time
import json


class Publisher:
    def __init__(self):
        self._publisher = None
        self._topic_path = None
        self.futures = dict()

    def publisher(self):
        if self._publisher is None:
            self._publisher = pubsub_v1.PublisherClient()
            self._topic_path = self._publisher.topic_path(cfg.get('pub-sub', 'PROJECT_ID'),
                                                          cfg.get('pub-sub', 'TOPIC_NAME'))
        return self._publisher

    def get_callback(self, future, data):
        def callback(future):
            try:
                from datetime import datetime
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print("Current Time =", current_time)

                print(future.result())
                self.futures.pop(data)
            except Exception as err:
                print("Please handle {} for {}.".format(err, data))
                raise Exception(err)
        return callback

    def publish_message(self, data):
        try:
            data = json.dumps(data).encode()  # publisher needs the data in bytes
            self.futures.update({data: None})
            future = self.publisher().publish(
                self._topic_path, data=data
            )
            self.futures[data] = future
            future.add_done_callback(self.get_callback(future, data))

            # Wait for all the publish futures to resolve before exiting.
            while self.futures:
                time.sleep(5)
        except Exception as err:
            print(err)
            raise Exception(err)
