#! /usr/bin/python

import json

from abiquo.client import Abiquo
from abiquo.client import check_response
from sys import argv 

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
        break

if role == None:
    print 'Role not found'

nick = raw_input("Ingresa nick de usuario: ")

# 'href': role._extract_link('edit')['href']
# 'href': role.follow('edit').url
for e in enterprises:
    print "Creating User in enterprise %s" % (e.name)
    code, user = e.follow('users').post(
        data=json.dumps({
            'name'     : 'New user1',
            'password' : '12qwaszx',
            'nick'     :  nick,
            'surname'  : 'myuser',
            'email'    : 'm@m.com',
            'locale'   : 'es',
            'active'   : True,
            'links':[
                {
                    'href': role._extract_link('edit')['href'],
                    'rel' : 'role'
                }
            ]
        }),
        headers={
            'accept':'application/vnd.abiquo.user+json',
            'content-type':'application/vnd.abiquo.user+json'
        }
    )

    check_response(201, code, user)
    print user.json