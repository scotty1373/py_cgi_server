#!/usr/bin/python
# -*- coding: UTF-8 -*-

print "Content-Type:text/html\n\n"
print

import cgi
import cgitb; cgitb.enable()
import serial
import sys
sys.stderr = sys.stdout

ser = serial.Serial("/dev/ttyUSB0",115200,timeout=5)
ser2 = serial.Serial("/dev/ttyUSB1",115200,timeout=5)
data = ser.readline()
data2 = ser2.readline()

print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>arm based IoT server</title>'
print '</head>'
print '<body>'
print '<h1>IoT remote control web server</h1>'
print '<h2>Environmental data print</h2>'
print '<h3>%s</h3>'%data
print '<hr />'
print '<p> </p>'
print '<h3>%s</h3>'%data2
print '<hr />'
print '<p> </p>'
print '<h3>Smoke: (null) </h3>'
print '<hr />'
print '<p> </p>'
print '<h6>05161161 Xiao Qianhao</h6>'
print'<h6>Final Project</h6>'
print '</body>'
print '</html>'
