from keystoneclient.auth.identity.v3 import password
from oslo_config import cfg

zaqar_opts = [
    cfg.StrOpt('zaqar_url', default='http://127.0.0.1:8888/',
               help='The URL for the zaqar api server'),
    cfg.StrOpt('zaqar_version', default='1.1',
               help='The zaqar api version to use'),
    ]


def load_conf():
    """get a configured ConfigOpts object

    this will attempt to load the configuration file for the
    big-data-bbq project. the only configuration options are those to
    configure keystone.
    """
    conf = cfg.ConfigOpts()
    conf.register_opts(zaqar_opts)
    conf.register_opts(password.Password.get_options(), group='keystone')
    conf(args=[], project='big-data-bbq')
    return conf
