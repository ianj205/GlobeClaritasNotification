#GlobeClaritasNotification#

*Send job completion messages in GLOBE Claritas using pushover*

Pushover is a simple mobile notifications application that allows you to send real-time notifications to Android and iOS devices. Pushover has a massive API, which includes scripts in just about every programming language you could care to use. 

Due to the integration GLOBE Claritas has with user-created python scripts through the `RUNPYTHON` module, you can create and use a wide variety of custom processes. Here we show a simple but effective example of sending instant messages when jobs complete.

###Pushover

To set up your pushover account, go to [www.pushover.net](Pushover) and signup. This will provide you with a User Token that identifies you when you receive messages (it is your ID). You will need to enter this into the python script.

In the ‘Your Applications’ section  of your account you can ‘Create’ an application easily, which will give you an Application Token (again you will need this to enter into the script). 

This script uses the seismic.controlState variable to identify if a job has completed (see the help documentation for other controlStates).

To add this in GLOBE Claritas add a RUNPYTHON module at at the end of your flow using the following settings:

* `PYTHONFILE`: RunpythonPushover.py
* `FUNCTION`: helperMethods


###To be done

* Add contextual messages for warning and error messages
*  
