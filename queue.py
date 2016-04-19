def create_named_queue(client, name):
    """return a queue object for the given name

    arguments:
    client -- an authenticated zaqar client
    name -- the name for the queue
    """
    return client.queue(name)
    

def send_message(queue, message, ttl=60):
    pass

