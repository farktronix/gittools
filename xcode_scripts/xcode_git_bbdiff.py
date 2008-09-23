#! /usr/bin/python
# -*- coding: utf-8 -*-

#
# This script is intended to be used from the xcode script menu, rather than from the terminal. Open the script editor in
# xcode and add the script file with the settings below.

# This script will open the frontmost file using git-bbdiff. If there are no differences, it will beep twice.
#
#	Suggested settings:
#		Input:		No Input
#		Directory:	Selection
#		Output:		Discard Output
#		Errors:		Display in Alert
#

import commands
import AppKit
import time

#----------------------------------------------------------------------------------------------------------------------------
#	beepError
#----------------------------------------------------------------------------------------------------------------------------

def beepError( inTimes = 2 ):
	i = 0
	while i < inTimes:
		AppKit.NSBeep()
		time.sleep(0.17)
		i = i + 1

#----------------------------------------------------------------------------------------------------------------------------
#	main script
#----------------------------------------------------------------------------------------------------------------------------

filename = "%%%{PBXFilePath}%%%"

command = "/usr/local/bin/git bbdiff " + filename

print( command )
status, output = commands.getstatusoutput( command )
if status != 0:
	beepError()
print( output )

if output.count( "has no differences." ) > 0:
	versions = []
	command = "/usr/local/bin/git log " + filename
	status, output = commands.getstatusoutput( command )
	if status != 0:
		beepError()
	
	for line in output.splitlines():
		if line.startswith( "commit " ):
			versions.append( line.replace( "commit ", "" )[0:8] )
			
	command = "/usr/local/bin/git bbdiff -r %s %s" % (versions[1], filename)
	status, output = commands.getstatusoutput( command )
	if status != 0:
		beepError()
