#!/usr/bin/python2

import commands

print "content-type: text/html"
print


def docker_list():
	
	z=1
	print "<select name='imagename'>"
	for i in commands.getoutput("sudo docker images").split('\n'):
		if z == 1:
			z=z+1
			pass
		else:
			j=i.split()
			print "<option>" + j[0] + ":" + j[1] + "</option>"

	print "</select>"


