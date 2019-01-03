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
        print (mensaje + " VAPP Name: " + vapp.name)
        print
       
        for vm in vms:
            print (mensaje2 + " VM Name: " + vm.name + " State VM: " + vm.state)

            code, nics = collection(vm, 'nics', 'nics')
            check_response(200, code, nics)
            for nic in nics:
                print mensaje3, "NIC: ", nic.mac

            code, disks = collection(vm, 'harddisks', 'harddisks')
            check_response(200, code, disks)
            for disk in disks:
                print (mensaje3 + " UUID DISK: " + disk.uuid) 

code2, dcs = api.admin.datacenters.get(headers={
    'accept':'application/vnd.abiquo.datacenters+json'
})
check_response(200, code, dcs)
print ("Response code dcs: %s" % code2)

for dc in dcs:
    code2, dsts = collection(dc, 'datastoretiers', 'datastoretiers')
    check_response(200, code, dsts)
    code2, racks = collection(dc, 'racks', 'racks')
    check_response(200, code, racks)
    print
    print ("Datacenter: " + dc.name)

    for rack in racks:
        code2, hypers = collection(rack, 'machines', 'machines')
        check_response(200, code, hypers)
        print
        print ("Rack: " + rack.name)

        for hyper in hypers:
            print ("Hypervisor: " + hyper.name)

    for dst in dsts:
        code2, dss = collection(dst, 'datastores', 'datastores')
        check_response(200, code, dss)
        print
        print ("Datastore Tier: " + dst.name) 

        for ds in dss:
            print ("Datastore: " + ds.name)