def get_named_network_id(client, name):
    """return the id for the named network

    arguments:
    client -- an authenticated neutron client
    name -- the name of the network to find

    returns:
    the id of the network or None if not found
    """
    nets = client.list_networks(name=name).get('networks', [])
    if len(nets) > 1:
        raise Exception('Oops, found multiple networks with that name.')
    if len(nets) == 0:
        return None
    return nets[0]['id']
