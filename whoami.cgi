#!/usr/bin/python

import cgi
import os
from subprocess import call

# for form access
import cgitb; cgitb.enable()

form = cgi.FieldStorage()

# get username
execution = os.popen('whoami', 'r', 0)
whoami = "".join(execution.readlines())
execution.close()

# print header
print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers

# print html
print "<html>"
print "  <head>"
print "    <title>Whoami</title>"
print "  </head>"
print "  <body>"
print "    <h1>Whoami</h1>"
print "    "+whoami
print "<br>"
print "  </body>"
print "</html>"
