# Introduction
Simple proof of concept using openstack oslo libraries and the wsgi.py server implementation used by 'glance-api' and the Falcon MicroFramework

# Branch service-proxy
This branch protoypes a simple proxy for glance requests, This is useful for the following reasons

* Network topology could create a throughput bottleneck (Having local access to glance images is faster)
* Glance images for use on cinder volumes must be converted from .ovf to raw before written to a cinder block device this proxy could cache the converted images so that future requests to glance images would return the pre-converted .ovf image saving conversion time.

# TODO
* db-oslo example
