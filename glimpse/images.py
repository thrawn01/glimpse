import falcon

class ImagesResource:
    def on_get(self, req, resp, image_id):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ('\nThis is an images request for image %s\n' % image_id)
