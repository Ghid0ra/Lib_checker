import os
import subprocess
from termcolor import colored


#file_to_check = input("Enter the file to check: ")

#open the file and its subfolders/files
#f= os.walk('file_to_check')
f= os.walk("/home/kali/ANDROID_PT/Ebantis_stag/ebantis_stag/lib/")
#s= subprocess.capture_output

#loop through the dirs and execute code
for dirpath, dirnames, filenames in f:
	print(dirpath)
	print(dirnames)
	print("\n")
	print(colored(dirpath, 'blue'))
	for fn in filenames:
		full_path= os.path.join(dirpath, fn)
		print(colored(fn, 'yellow'))
		cmd = subprocess.run(f"strings {full_path}| grep -i 'stack_chk'", shell=True, capture_output=True, text=True, check=True)
		print(cmd.stdout) 
	

'''TO DO

2. Print the result showing which all files have the properties false  - 0%

'''
