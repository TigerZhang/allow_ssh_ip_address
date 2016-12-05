#!/usr/bin/python

#
# Access this CGI from the remote browser, this script will add the
# remote address to allow list in the iptables
#

import os
from subprocess import call

print "Content-type: text/html\r\n\r\n";
# print "<font size=+1>Environment</font><br>";
# for param in os.environ.keys():
#     print "<b>%20s</b>: %s<br>" % (param, os.environ[param])
REMOTE_ADDR = os.environ['REMOTE_ADDR']
print 'REMOTE_ADDR:', REMOTE_ADDR, "<br>"

# append remote addr to /etc/iptables/rules.v4
# between:
### Appended by CGI Script Begin
### Appended by CGI Script End
# sed -i '/Line to insert after/ i Line one to insert \
#        second new line to insert \
#        third new line to insert' file
command = "sudo /home/yunba/allow-ssh-ip-address %s" % REMOTE_ADDR
print "exec:", call(command.split())
