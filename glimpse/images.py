from oslo.log._i18n import _
from oslo.config import cfg
from os import path, listdir
import statistics
import exception
import falcon
import errno
import json
import job

images_opts = [
    cfg.StrOpt('image_cache_dir', default='/var/cache/glimpse',
               help=_('Directory where the cached glance images are stored'))
]

CONF = cfg.CONF
CONF.register_opts(images_opts)


class ImageDataResource():
    def on_get(self, req, resp, image_id):
        """Handles Image download requests"""
        try:
            image_path = path.join(CONF.image_cache_dir, image_id)
            # Attempt to open our local cached version of the image
            with open(image_path + '.ddi') as fd:
                # Record this download in the census log
                statistics.downloaded(image_id)
                # TODO: Make this a chunked response
                resp.body = fd.read()

        except IOError, e:
            # No such file or directory
            if e.errno != errno.ENOENT:
                raise

        try:
            # Start the conversion job
            job.start(image_id, req.get_header('X-Auth-Token', required=True))
        except exception.JobAlreadyRunning, e:
            # If conversion job is already running We have 2 options, make the
            # request hang here until the convert is done or return 202
            # (Request accepted process pending) and have our glance client try
            # again in a few seconds
            resp.status = falcon.HTTP_202


class ImageListResource():
    def on_get(self, req, resp):
        """ Returns a list of cached images """
        resp.body = json.dumps(listdir(CONF.image_cache_dir))
