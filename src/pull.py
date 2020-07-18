from my_pubsub.subscriber import Subscriber


while True:
    try:
        print('Starting a new subscriber')
        subscriber = Subscriber()
        subscriber.subscribe_message()
    except Exception as err:
        print(err)
