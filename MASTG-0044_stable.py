import os
import subprocess
from termcolor import colored
import re 

file_to_check = input("Enter the file to check: ")

#open the file and its subfolders/files
f= os.walk(file_to_check)
#loop through the dirs and execute code - Rabin
print('\n')
print(colored("RESULTS FOR RABIN2 COMMAND", 'red', 'on_white', attrs=['blink', 'bold']))
for dirpath, dirnames, filenames in f:
	print("\n")
	print(colored(dirpath, 'blue', attrs=['bold']))
	for fn in filenames:
		full_path= os.path.join(dirpath, fn)
		print(colored(fn, 'yellow'))
		rbn = subprocess.run(f"rabin2 -I {full_path}|grep -E 'canary|pic'", shell=True, capture_output=True, text=True, check=True)
		print(rbn.stdout) 



