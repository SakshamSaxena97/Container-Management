#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"


cName=cgi.FormContent()['x'][0]
cstartstatus=commands.getstatusoutput("sudo docker start {}".format(cName))

if cstartstatus[0] == 0:
        print "location: docker_manage.py"
        print

else:
        print "Not Started"

