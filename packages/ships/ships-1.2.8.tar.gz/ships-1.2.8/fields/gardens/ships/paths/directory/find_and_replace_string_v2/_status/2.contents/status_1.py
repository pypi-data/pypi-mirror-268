



'''
	python3 status.proc.py 'paths/directory/find_and_replace_string_v2_v2/_status/2.contents/status_1.py'
'''


import time
from fractions import Fraction
import shutil

import ships.paths.directory.find_and_replace_string_v2 as find_and_replace_string_v2
import ships.cycle as cycle
import ships.paths.directory.check_equality as check_equality
	

def prepare ():
	import pathlib
	from os.path import dirname, join, normpath
	this_folder = pathlib.Path (__file__).parent.resolve ()
		
	from pathlib import Path
	temp = normpath (join (this_folder, "temp"))
	cryo = normpath (join (this_folder, "cryo"))
	
	try:
		shutil.rmtree (temp)
	except Exception as E:
		print ("temp wasn't removed", E)

	
	shutil.copytree (
		cryo,
		temp
	)
	
	return [ cryo, temp ]

def check_1 ():
	[ cryo, temp ] = prepare ()
	
	proceeds = find_and_replace_string_v2.start (
		the_path = str (temp),

		find = 'html',
		replace_with = 'HTML'
	)

	assert (len (proceeds ["content_replacements"]) == 1)
	assert ('example.html' in proceeds ["content_replacements"] [0])
	
	report = check_equality.start (
		cryo,
		temp
	)	
	assert (
		report ==
		{'1': {'1/example.html': 'f'}, '2': {'1/example.HTML': 'f'}}
	), report
	
	try:
		shutil.rmtree (temp)
	except Exception as E:
		print ("temp wasn't removed", E)
	
	return;
	
checks = {
	"runs without exceptions": check_1
}




#