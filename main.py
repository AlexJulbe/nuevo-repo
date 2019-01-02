#! /usr/bin/python

import json

from abiquo.client import Abiquo
from abiquo.client import check_response

api = Abiquo("https://mothership.bcn.abiquo.com/api", auth=("ajulbe", "julbe1991"))
code, vdcs = api.cloud.virtualdatacenters.get(headers={
    'accept':'application/vnd.abiquo.virtualdatacenters+json'
})
check_response(200, code, vdcs)
"""print ("Response code vdcs: %s" % code)"""

for vdc in vdcs:
    code, vapps = vdc.follow('virtualappliances').get(headers={
        'accept' : 'application/vnd.abiquo.virtualappliances+json'
    })
    check_response(200, code, vapps)
    print
    print vdc.name
    
    for vapp in vapps:
        code, vms = vapp.follow('virtualmachines').get(headers={
        'accept' : 'application/vnd.abiquo.virtualmachines+json'
        })
        check_response(200, code, vms)
        mensaje = '*****'
        mensaje2 = '*****' * 2
        print
        print (mensaje + vapp.name)
        print
       
        for vm in vms:
            print (mensaje2 + vm.name)