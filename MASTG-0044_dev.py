import os
import subprocess
from termcolor import colored
import re

#file_to_check = input("Enter the file to check: ")

#open the file and its subfolders/files
f= os.walk('/home/kali/ANDROID_PT/Ebantis_stag/ebantis_stag/lib/')
''
#loop through the dirs and execute code - Rabin
print('\n')
print(colored("RESULTS FOR RABIN2 COMMAND", 'red', 'on_white', attrs=['blink', 'bold']))
for dirpath, dirnames, filenames in f:
	print("\n")
	#print(colored(dirpath, 'blue', attrs=['bold']))
	for fn in filenames:
		full_path= os.path.join(dirpath, fn)
		#print(colored(fn, 'yellow'))
		rbn = subprocess.run(f"rabin2 -I {full_path}|grep -E 'canary|pic'", shell=True, capture_output=True, text=True, check=True)
		#find false values
		false_values = []
		for line in rbn.stdout.splitlines():
			if 'false' in line:
				print(filenames)
				print(line)


'''
print("\n")
print(colored("RESULTS FOR STRINGS COMMAND(CANARY CHECK ONLY)",'red','on_white',attrs=['blink','bold']))
for dirpaths ,dirnames, filenames in f:
	print("\n")
	print(colored(dirpaths, 'blue', attrs=['bold']))
	for fn in filenames:
		full_path=os.path.join(dirpaths,fn)
		print('\n',colored(fn, 'yellow'))
		str= subprocess.run(f"strings {full_path}| grep -i 'stack_chk'", shell=True, capture_output=True, text=True, check=False)
		if str.stdout.strip():
			print(str.stdout)
		else:
			print('\n',colored("Canary Not Present",'red','on_light_yellow',attrs=['bold']))
'''

