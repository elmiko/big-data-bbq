def create_spark_cluster(client, name, template, image, keypair):
    """launch a spark cluster

    arguments:
    name -- the name to assign the cluster
    template -- the cluster template id
    image -- the image id for the cluster nodes
    keypair -- a keypair id to configure with the cluster nodes

    returns:
    the id of the cluster
    """
    cluster = sahara_client.clusters.create(name=name,
                                            plugin_name='spark',
                                            hadoop_version='1.6.0',
                                            cluster_template_id=template,
                                            default_image_id=image,
                                            user_keypair_id=keypair)
    return cluster.id


def create_spark_cluster_template(client, name, float_pool, mgmt_net):
    """create a cluster template for spark

    this will update the sahara server with the requested cluster
    template.

    arguments:
    client -- an authenticated sahara client
    name -- the name for the cluster template
    float_pool -- id of the floating point ip network
    mgmt_net -- id of the management network

    returns:
    the id of the cluster template
    """
    kwargs = {
        'name': name,
        'plugin_name': 'spark',
        'hadoop_version': '1.6.0',
        'net_id': mgmt_net,
        'cluster_configs': {'general': {'Enable NTP service': False}},
        'node_groups': [
            {
                'count': 1,
                'name': 'spark160-master',
                'flavor_id': '2',
                'node_processes': ['namenode',
                                   'master'],
                'floating_ip_pool': float_pool
            },
            {
                'count': 1,
                'name': 'spark160-worker',
                'flavor_id': '2',
                'node_processes': ['datanode',
                                   'slave'],
                'floating_ip_pool': float_pool
            }
        ]
    }
    return client.cluster_templates.create(**kwargs).id


def get_named_image_id(client, name):
    """return the id of a named image registerd with sahara

    arguments:
    client -- an authenticated sahara client
    name -- the name of the image to find

    returns:
    the id of the image or None if not found
    """
    images = client.images.find(name=name)
    if len(images) > 1:
        raise Exception('Oops, found multiple images with that name.')
    if len(images) == 0:
        return None
    return images[0].id

