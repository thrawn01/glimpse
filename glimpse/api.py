from glimpse import images
from glimpse import proxy
import falcon


# falcon.API instances are callable WSGI apps
app = falcon.API()

# Handle all requests that would return an image
#app.add_route('/v2/images/{image_id}/file', images.ImageDataResource())
app.add_route('/v1/images/{image_id}', images.ImageDataResource())

# Useful for ensuring all glimpse-api servers have the same images cached
app.add_route('/cached/images', images.ImageListResource())

# Proxy requests for detail image listings
app.add_route('/v1/images/detail', proxy.ProxyResource())

# Handle all other requests
app.add_sink(proxy.ProxySink(), '/')
