



'''
	python3 status.proc.py 'paths/directory/find_and_replace_string/_status/1/status_1.py'
'''


import time
from fractions import Fraction
import shutil

import ships.paths.directory.find_and_replace_string as find_and_replace_string
import ships.cycle as cycle


def prepare ():
	import pathlib
	from os.path import dirname, join, normpath
	this_folder = pathlib.Path (__file__).parent.resolve ()
		
	from pathlib import Path
	temp = normpath (join (this_folder, "temp/1"))
	
	try:
		shutil.rmtree (temp)
	except Exception as E:
		print ("temp wasn't removed", E)
	
	shutil.copytree (
		normpath (join (this_folder, "cryo/1")),
		temp
	)
	
	return [ temp ]

def check_1 ():
	[ temp ] = prepare ()
	
	proceeds = find_and_replace_string.start (
		glob_string = str (temp) + "/**/*",

		find = 'html',
		replace_with = 'HTML'
	)

	assert (len (proceeds ["content_replacements"]) == 1)
	assert ('example.html' in proceeds ["content_replacements"] [0])
		
	try:
		shutil.rmtree (temp)
	except Exception as E:
		print ("temp wasn't removed", E)
	
	return;
	
checks = {
	"runs without exceptions": check_1
}




#