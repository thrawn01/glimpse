from oslo.utils import encodeutils
from oslo.log._i18n import _
import six


class GlimpseException(Exception):
    message = _("An unknown exception occurred")

    def __init__(self, message=None, *args, **kwargs):
        if not message:
            message = self.message
        if kwargs:
            message = message % kwargs
        self.msg = message
        super(GlimpseException, self).__init__(message)

    def __unicode__(self):
        return six.text_type(self.msg)


def exception_to_str(exc):
    try:
        error = six.text_type(exc)
    except UnicodeError:
        try:
            error = str(exc)
        except UnicodeError:
            error = ("Caught '%(exception)s' exception." %
                     {"exception": exc.__class__.__name__})
    return encodeutils.safe_encode(error, errors='ignore')


class WorkerCreationFailure(GlimpseException):
    message = _("Server worker creation failed: %(reason)s.")


class InvalidContentType(GlimpseException):
    message = _("Invalid content type %(content_type)s")
