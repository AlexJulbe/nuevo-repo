#! /usr/bin/python

import json

from abiquo.client import Abiquo    
from abiquo.client import check_response

api = Abiquo("https://mothership.bcn.abiquo.com/api", auth=("ajulbe", "julbe1991"))
code, vdcs = api.cloud.virtualdatacenters.get(headers={
    'accept':'application/vnd.abiquo.virtualdatacenters+json'
})
code2, vapp = api.cloud.virtualappliances.get(headers={
    'accept' : 'application/vnd.abiquo.virtualappliances+json'
})
    
check_response(200, code, vdcs)
print ("Response code vdcs: %s" % code)
print ("Response code vapps: %s" % code2)