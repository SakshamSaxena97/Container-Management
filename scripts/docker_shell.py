#!/usr/bin/python2

import commands
import cgi

print "content-type: text/html"
print

cName=cgi.FormContent()['x'][0]

ipStatus=commands.getoutput("sudo docker inspect {0} | jq '.[].NetworkSettings.Networks.bridge.IPAddress'".format(cName))


shellInstall=commands.getstatusoutput("sudo docker exec {0} yum install shellinabox".format(cName))
if shellInstall[0] == 0:
	print "Installed"
	commands.getoutput("/usr/sbin/shellinaboxd")
	commands.getoutput("https://{0}:4200".format(ipStatus))
else:
	print "Try Again"



