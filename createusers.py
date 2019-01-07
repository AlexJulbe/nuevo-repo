#! /usr/bin/python

import json

from abiquo.client import Abiquo
from abiquo.client import check_response

import urllib3
urllib3.disable_warnings()

api = Abiquo("https://alex44.bcn.abiquo.com/api", auth=("admin", "xabiquo"), verify=False)

code, enterprises = api.admin.enterprises.get(
    headers={'Accept':'application/vnd.abiquo.enterprises+json'
    })
print "Response code enterprise is: %s" % code

code2, roles = api.admin.roles.get(
    headers={'Accept':'application/vnd.abiquo.roles+json'
    })    
print "Response code role is: %s" % code2

roleName = "USER"
for r in roles:
    if r.name == roleName:
        role = r
        print r.links
        break

for e in enterprises:
    print "Creating User in enterprise %s" % (e.name)
    code, user = e.follow('users').post(
            data=json.dumps({
                'name': 'New user',
                'links':[
                    role.follow('edit')
            ]}),
            headers={'accept':'application/vnd.abiquo.user+json',
                     'content-type':'application/vnd.abiquo.user+json'
                     })
        
    check_response(200, code2, user)
    print user.name



"""
for role in roles:
    code2, role = roles.follow('').post(
    data=json.dumps({'name': 'USER'}),
            headers={'accept':'application/vnd.abiquo.role+json',
                     'content-type':'application/vnd.abiquo.role+json'
                     })
    
    check_response(200, code2, role)                
    print "Response code role is: %s" % code2
    print "Created Role: %s for USER [%s]" % (role.name, user.name)
"""