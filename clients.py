from keystoneclient.auth.identity.v3 import password
from keystoneclient import session
from neutronclient.v2_0 import client as neutron_client
from novaclient import client as nova_client
from saharaclient.api import client as sahara_client
from troveclient.v1 import client as trove_client
from zaqarclient.queues import client as zaqar_client


def neutron(conf):
    return neutron_client.Client(session=session_from_conf(conf))


def nova(conf):
    return nova_client.Client(2, session=session_from_conf(conf))


def sahara(conf):
    return sahara_client.Client(session=session_from_conf(conf))


def trove(conf):
    return trove_client.Client(conf.keystone.username,
                               conf.keystone.password,
                               conf.keystone.project_name,
                               conf.keystone.auth_url)


def zaqar(conf):
    zconf = {
            'auth_opts': {
                'backend': 'keystone',
                'options': {
                    'os_username': conf.keystone.username,
                    'os_password': conf.keystone.password,
                    'os_project_name': conf.keystone.project_name,
                    'os_auth_url': conf.keystone.auth_url,
                    'insecure': ''
                    }
                }
            }

    # this is a workaround for an unevenness in the zaqar client
    zmap = {'1': 1, '1.1': 1.1, '2': 2}
    vers = zmap.get(conf.zaqar_version)
    return zaqar_client.Client(conf.zaqar_url, vers, conf=zconf)


def session_from_conf(conf):
    auth = password.Password.load_from_conf_options(
        conf, group='keystone')
    return session.Session(auth=auth)
