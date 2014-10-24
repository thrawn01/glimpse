import exception


def running(image_id):
    """ Returns True if a conversion job for image_id is currently running """
    # Query the database for a currently running job
    return False


def start(image_id, auth_token):
    """ Attempts to start a conversion job using celery """
    if running(image_id):
        raise exception.JobAlreadyRunning(image_id=image_id)

    # TODO: Start a celery job
