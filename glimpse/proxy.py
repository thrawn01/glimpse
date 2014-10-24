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
    """ Called when none of the other routes match """
    def __call__(self, req, resp, **kwargs):
        resp.status = falcon.HTTP_302
        resp.set_header('Location', CONF.glance_server + req.path
                        + '?' + req.query_string)


class ProxyResource(object):
    """ Called when a route is similar to the download images route, but should
    be proxied instead """
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_302
        resp.set_header('Location', CONF.glance_server + req.path
                        + '?' + req.query_string)

    def on_head(self, req, resp):
        resp.status = falcon.HTTP_302
        resp.set_header('Location', CONF.glance_server + req.path
                        + '?' + req.query_string)
