# big-data-bbq

Example code to supplement the OpenStack summit presentation

The code contained in this project is designed to be used as snippets to
illustrate certain OpenStack interactions. My suggestion is to use this
code as prototyping and experiment material, especially in conjunction
with the Python REPL.

Begin by creating a local version of the `big-data-bbq.conf` file in your
`$HOME/.big-data-bbq/big-data-bbq.conf`. Replace the necessary values
with those of your stack (username, password, auth_url, etc).

After creating a configuration file, i recommend making a Python virtual
environment to begin experimenting. Install the contents of the
`requirements.txt` file into the new virtual environment using the
command `pip install -r requirements.txt`

Once installed and running in a virtual environment, simply start the
Python REPL in the root of this project, and begin your experiments!

Example:

    Python 2.7.11 (default, Mar 31 2016, 20:46:51) 
    [GCC 5.3.1 20151207 (Red Hat 5.3.1-2)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from clients import *
    >>> from config import *
    >>> from networking import *
    >>> conf = load_conf()
    >>> neutron_client = neutron(conf)
    >>> priv_id = get_named_network_id(neutron_client, 'private')
    >>> priv_id
    u'e13419d9-65ea-4815-85ba-7e04486ea3e1'
    >>> pub_id = get_named_network_id(neutron_client, 'public')
    >>> pub_id
    u'ab80c174-bd9e-4768-8720-5d525bd3c59a'
    >>> sahara_client = sahara(conf)
    >>> sahara_client.cluster_templates.list()
    []
    >>> from data_processing import *
    >>> spark_cluster_template = create_spark_cluster_template(sahara_client, 'spark160', pub_id, priv_id)
    >>> spark_cluster_template
    u'97ca2f78-952d-4a1e-bd59-9941b788d89c'
    >>> sahara_client.cluster_templates.find(id=spark_cluster_template)
    [<saharaclient.api.cluster_templates.ClusterTemplate object at 0x7f6d2d8db2d0>]
    >>> template = _[0]
    >>> template.id
    u'97ca2f78-952d-4a1e-bd59-9941b788d89c'
    >>> template.name
    u'spark160'
    >>> 

