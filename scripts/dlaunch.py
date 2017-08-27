#!/usr/bin/python2

import  dimages



print "<h2>Launch your Container : </h2>"

print "<form action='docker_launch.py'>"

print "Select ur docker image :"
dimages.docker_list()

print """
<br />
Enter ur container name: <input name='cname' />
<br />
<input type='submit' />
</form>
"""

