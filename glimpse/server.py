from __future__ import print_function

import eventlet
import sys

# Monkey patch socket, time, select, threads
eventlet.patcher.monkey_patch(all=False, socket=True, time=True,
                              select=True, thread=True, os=True)

from glimpse import exception
from oslo.config import cfg
from glimpse import config
from oslo.log import log
from glimpse import wsgi
from api import app
import logging


def main():
    try:
        CONF = cfg.CONF
        # Register config options for the logging system
        log.register_options(CONF)
        # Init the config object
        CONF(project='glimpse', version='0.1')
        # Set some reasonable defaults
        config.set_defaults(CONF)
        # Load the logging options from config
        log.setup(CONF, 'glimpse')

        # Get our Logging instance
        LOG = log.getLogger(__name__)
        LOG.debug("Loading glimpse from %s" % CONF.config_file)
        # Spit our config out to stderr
        CONF.log_opt_values(LOG, logging.INFO)
        # Register eventlet poll, or select
        wsgi.set_eventlet_hub()
        # Init and start the WSGI server
        server = wsgi.Server()
        server.start(app, default_port=9292)
        server.wait()
    except (exception.WorkerCreationFailure, RuntimeError) as e:
        print("ERROR: %s\n" % exception.exception_to_str(e), file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
