#!/usr/bin/env python
#
#This is an example of a python script for Claritas
#It utilises Pushover (www.pushover.net) to send a push notification 
#The current script is set up to inform you of end of job
#
#In order to use this you need to register a pushover account
#set one up to find out your user token, to get the application token 
#you will have to set up a new application 
#
#Edit EnterToken with your application token
#Edit EnterUser with your user token
#
import httplib, urllib

def endOfJobAction(seismic):
    """ run an action at the end of job"""
    if seismic.controlState is 3:
        return
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "EnterToken",
    "user": "EnterUser",
    "message": "your claritas job has finished",
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
exit()
