import os
import subprocess
from termcolor import colored



file_to_check = input("Enter the file to check: ")

#Check if the file actually exist
sys_files=["/bin","/dev","/initrd.img.old","/lib32","/lost+found","/mnt","/proc","/run","/srv","/tmp","/var","/vmlinuz.old", "/boot",  "/etc",  "/initrd.img", "/lib", "/lib64",  "/media", "/opt", "/root", "/sbin", "/sys" "/usr", "/vmlinuz"]
print(sys_files)
#file_Checker=subprocess.run(loca)
#if f == 


'''
#open the file and its subfolders/files
f= os.walk(file_to_check)

#loop through the dirs and execute code
for dirpath, dirnames, filenames in f:
	print("\n")
	print(colored(dirpath, 'blue'))
	for fn in filenames:
		full_path= os.path.join(dirpath, fn)
		print(colored(fn, 'yellow'))
		cmd = subprocess.run(f"rabin2 -I {full_path}|grep -E 'canary|pic'", shell=True, capture_output=True, text=True, check=True)
		print(cmd.stdout) 
	

'' TO DO

1. Create a logic to check if the inputted file exists - 0%
2. Print the result showing which all files have the properties false  - 0%

'''