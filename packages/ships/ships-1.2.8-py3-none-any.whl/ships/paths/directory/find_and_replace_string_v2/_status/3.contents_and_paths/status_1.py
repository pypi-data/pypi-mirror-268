






'''
	python3 status.proc.py 'paths/directory/find_and_replace_string_v2_v2/_status/3.contents_and_paths/status_1.py'
'''


import time
from fractions import Fraction
import shutil
import rich

import ships.paths.directory.find_and_replace_string_v2 as find_and_replace_string_v2
import ships.cycle as cycle
import ships.paths.directory.check_equality as check_equality



def prepare ():
	import pathlib
	from os.path import dirname, join, normpath
	this_folder = pathlib.Path (__file__).parent.resolve ()
		
	from pathlib import Path
	temp = str (normpath (join (this_folder, "temp")))
	cryo = str (normpath (join (this_folder, "cryo")))
	cryo_proceeds = str (normpath (join (this_folder, "cryo_proceeds")))
	
	try:
		shutil.rmtree (temp)
	except Exception as E:
		print ("temp wasn't removed", E)

	
	shutil.copytree (
		cryo,
		temp
	)
	
	return [ cryo, cryo_proceeds, temp ]

def demo (temp):
	try:
		shutil.rmtree (temp)
	except Exception as E:
		print ("temp wasn't removed", E)

def check_1 ():
	[ cryo, cryo_proceeds, temp ] = prepare ()
	
	proceeds = find_and_replace_string_v2.start (
		the_path = temp,

		find = 'txt',
		replace_with = 'the_txt'
	)
	
	rich.print_json (data = proceeds)

	report = check_equality.start (
		cryo_proceeds,
		temp
	)	
	assert (
		report ==
		{'1': {}, '2': {}}
	), report
	
	
	report = check_equality.start (
		cryo,
		temp
	)
	
	rich.print_json (data = report)
	
	assert (
		report ==
		{
			"1": {
				"1.txt": "f",
				"symlink_to_1.txt": "s",
				"txt": "d",
				"2/2.txt": "f",
				"2/55/55.txt": "f",
				"3/3.txt": "f",
				"3/9/9.txt": "f"
			},
			"2": {
				"1.the_txt": "f",
				"symlink_to_1.the_txt": "f",
				"the_txt": "d",
				"2/2.the_txt": "f",
				"2/55/55.the_txt": "f",
				"3/3.the_txt": "f",
				"3/9/9.the_txt": "f"
			}
		}
	), report
	
	#demo (temp)
	
checks = {
	"runs without exceptions": check_1
}




#