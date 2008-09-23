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

filename = "%%%{PBXFilePath}%%%"

command = "/usr/local/bin/git bbdiff " + filename

print( command )
status, output = commands.getstatusoutput( command )
print( output )

if output.count( "has no differences." ) > 0:
	# We need to sleep for a bit after each beep to allow
	# the sound to play or else it sounds jacked up.
	AppKit.NSBeep()
	time.sleep(0.17)
	AppKit.NSBeep()
	time.sleep(0.17)
