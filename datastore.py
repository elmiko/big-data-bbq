def get_datastore_id(client, name):
    """return the id of a datastore

    arguments:
    client -- an authenticated trove client
    name -- the name of the datastore to find

    returns:
    the id of the datastore or None if not found
    """
    try:
        store = client.datastores.find(name=name)
        return store.id
    except Exception:
        return None


def get_datastore_version_id(client, datastore, version):
    """return the id of a datastore version

    arguments:
    client -- an authenticated trove client
    datastore -- the id of a datastore
    version -- the version to find

    returns:
    """
    try:
        store = client.datastores.find(id=datastore)
        for vers in store.versions:
            if vers.get('name') == version:
                return vers.get('id')
    except Exception:
        return None
