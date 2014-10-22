import falcon


class ProxySink(object):
    def __call__(self, req, resp, **kwargs):
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nThis is a proxy request for %s\n' % kwargs)
