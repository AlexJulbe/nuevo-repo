#! /usr/bin/python

import json

from abiquo.client import Abiquo
from abiquo.client import check_response

def collection(resource, rel, media):
    return resource.follow(rel).get(headers={
        'accept':'application/vnd.abiquo.%s+json'%media
    })


api = Abiquo("https://mothership.bcn.abiquo.com/api", auth=("ajulbe", "julbe1991"))
code, vdcs = api.cloud.virtualdatacenters.get(headers={
    'accept':'application/vnd.abiquo.virtualdatacenters+json'
})
check_response(200, code, vdcs)
"""print ("Response code vdcs: %s" % code)"""

for vdc in vdcs:
    code, vapps = collection(vdc,'virtualappliances','virtualappliances')
    check_response(200, code, vapps)
    print
    print vdc.name
    
    for vapp in vapps:
        code, vms = collection(vapp,'virtualmachines','virtualmachines')
        check_response(200, code, vms)
        mensaje = '*****'
        mensaje2 = '*****' * 2
        mensaje3 = '*****' * 3
        print
        print (mensaje + "VAPP Name: " + vapp.name)
        print
       
        for vm in vms:
            code, disks = collection(vm, 'harddisks', 'harddisks')
            check_response(200, code, disks)
            print (mensaje2 + "VM Name: " + vm.name)

            for disk in disks:
                print (mensaje3 + "UUID DISK: " + disk.uuid) 