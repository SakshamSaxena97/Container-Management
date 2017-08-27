#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print
print """
<script>
function lw(mycname)
{
document.location='docker_shell.py?x=' + mycname;
}
</script>
"""
print """
<script>
function lw1(mycname)
{
document.location='docker_stop.py?x=' + mycname;
}
</script>
"""
print """
<script>
function lw2(mycname)
{
document.location='docker_start.py?x=' + mycname;
}
</script>
"""
print """
<script>
function lw3(mycname)
{
document.location='docker_remove.py?x=' + mycname;
}
</script>
"""
z=1
print "<table border='5'>"
print "<tr><th>Images</th><th>ContainerName</th><th>Status</th><th>OnlineShell</th><th>Stop</th><th>Start</th><th>Remove</th></tr>"

for i in commands.getoutput("sudo docker ps -a").split('\n'):
	if z == 1:
		z=z+1
		pass
	else:
		j=i.split()
		cStatus=commands.getoutput("sudo docker inspect {} | jq '.[].State.Status'".format(j[-1]))
		print "<tr><td>" + j[1] + "</td><td>" + j[-1] + "</td><td>" + cStatus + "</td><td> <input value='{0}' type='button' onclick='lw(this.value)' /> </td><td> <input value='{0}' type='button' onclick='lw1(this.value)' /> </td><td> <input value='{0}' type='button' onclick='lw2(this.value)' /> </td><td> <input value='{0}' type='button' onclick='lw3(this.value)' /> </td></tr>".format(j[-1]) 

print "</table>"


