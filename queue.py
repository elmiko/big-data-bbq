def create_named_queue(client, name):
    """return a queue object for the given name

    arguments:
    client -- an authenticated zaqar client
    name -- the name for the queue
    """
    return client.queue(name)


def send_message(queue, message, ttl=60):
    """send a message on the queue

    arguments:
    queue -- a queue object to use for sending
    message -- the message payload to send
    ttl -- the time to live for the message (default 60 seconds)
    """
    body = {'body': message, 'ttl': ttl}
    queue.post(body)
