#! /usr/bin/python

import json

from abiquo.client import Abiquo
from abiquo.client import check_response

mensaje = '*****'
mensaje2 = '*****' * 2
mensaje3 = '*****' * 3

def collection(resource, media):
    code, resources = resource.get(headers={
        'accept':'application/vnd.abiquo.%s+json'%media
    })
    check_response(200, code, resources)
    return resources

def showNIC(nic):
    print mensaje3, "NIC:", nic.mac

def showDisk(disk):
    print mensaje3 ,"UUID DISK:" , disk.uuid

def showVM(vm):
    print (mensaje2 + " VM Name: " + vm.name + " State VM: " + vm.state)
    map(showDisk, collection(vm.follow('harddisks'), 'harddisks'))
    map(showNIC, collection(vm.follow('nics'), 'nics'))

def showVapp(vapp):
    print (mensaje + " VAPP Name: " + vapp.name)
    map(showVM, collection(vapp.follow('virtualmachines'),'virtualmachines'))

def showVDC(vdc):
    print vdc.name   
    map (showVapp, collection(vdc.follow('virtualappliances'),'virtualappliances'))

def showHyper(hyper):
    print mensaje2, "Hypervisor Name:", hyper.name 

def showRack(rack):
    print (mensaje + "Rack Name:" + rack.name)
    map(showHyper, collection(rack.follow('machines'), 'machines'))

def showDatastore(ds):
    print (mensaje2 + "Datastore: " + ds.name)

def showDatastoretiers(dst):
    print (mensaje + "Datastoretier Name:" + dst.name)
    map(showDatastore, collection(dst.follow('datastores'), 'datastores'))

def showDC(dc):
    print ("Datacenter Name:" + dc.name)
    map (showRack, collection(dc.follow('racks'), 'racks'))
    map (showDatastoretiers, collection(dc.follow('datastoretiers'), 'datastoretiers'))

api = Abiquo("https://mothership.bcn.abiquo.com/api", auth=("ajulbe", "julbe1991"))

map(showVDC, collection(api.cloud.virtualdatacenters, "virtualdatacenters"))

map(showDC, collection(api.admin.datacenters, 'datacenters'))