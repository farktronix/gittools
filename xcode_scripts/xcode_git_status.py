#! /usr/bin/python
# -*- coding: utf-8 -*-

#
# This script is intended to be used from the xcode script menu, rather than from the terminal. Open the script editor in
# xcode and add the script file with the settings below.
#
# When run from the script menu, this script will display the git log for the frontmost file.
#
#	Suggested settings:
#		Input:		No Input
#		Directory:	Selection
#		Output:		Open in New Document
#		Errors:		Merge with Script Output
#

import commands

command = "/usr/local/bin/git status"

status, output = commands.getstatusoutput( command )
print( output )
