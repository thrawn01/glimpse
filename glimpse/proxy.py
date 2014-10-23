from oslo.log._i18n import _
from oslo.config import cfg
import falcon

proxy_opts = [
    cfg.StrOpt('glance_server', default='http://glance:9292',
               help=_('The glance server we are a proxy for. '
                      'All requests that are not matched by our'
                      ' routes are proxied to this server'))
]

CONF = cfg.CONF
CONF.register_opts(proxy_opts)


class ProxySink(object):
    def __call__(self, req, resp, **kwargs):
        resp.status = falcon.HTTP_302
        resp.set_header('Location', CONF.glance_server + req.path
                        + '?' + req.query_string)
