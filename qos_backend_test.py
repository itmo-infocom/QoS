import json
import logging
import drv_list

from ryu.app import simple_switch#will be frontend
from webob import Response
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER
from ryu.controller.handler import set_ev_cls
from ryu.app.wsgi import ControllerBase, WSGIApplication, route
from ryu.lib import dpid as dpid_lib

simple_switch_instance_name = 'simple_switch_api_app'
url = '/qos/queue/status/{dpid}'

class SimpleSwitchRest13(simple_switch.SimpleSwitch):

    _CONTEXTS = { 'wsgi': WSGIApplication }

    def __init__(self, *args, **kwargs):
        super(SimpleSwitchRest13, self).__init__(*args, **kwargs)
        self.switches = {}
        wsgi = kwargs['wsgi']
        wsgi.register(SimpleSwitchController, {simple_switch_instance_name : self})

class SimpleSwitchController(ControllerBase):

    def __init__(self, req, link, data, **config):
        super(SimpleSwitchController, self).__init__(req, link, data, **config)
        self.simpl_switch_spp = data[simple_switch_instance_name]

    @route('simpleswitch', url, methods=['GET'], requirements={'dpid': dpid_lib.DPID_PATTERN})
    def show_queue_status(self, req, **kwargs):

        simple_switch = self.simpl_switch_spp
        dpid = dpid_lib.str_to_dpid(kwargs['dpid'])

        table = open('file.txt', 'r')
	print 'dpid is "%s"' %dpid
        i = 0
	method = 'GET'#tmp
        for line in table.readlines():
            if line.split(';')[0] == str(dpid):
                drv = line.split(';')[1]
                drv_list.gotodrv(drv, method, url)
                #print line.split(';')[1]#debug
                i += 1

        table.close()

        if i==0:
            print 'not found'#return Response(status=404)
        elif i==1:
            print 'done'#return Response(status=200)
        else:
            print 'table err'#return Response(status=500)
