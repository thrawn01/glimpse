from glimpse import images
from glimpse import proxy
import falcon


# falcon.API instances are callable WSGI apps
app = falcon.API()
# Handle all requests to the '/images/{}/file' URL path
app.add_route('/images/{image_id}/file', images.ImagesResource())
# Handle all other requests
app.add_sink(proxy.ProxySink(), '/')
