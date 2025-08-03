import sys
import time
import os

os.system("clear")
print("\n\n\n\n")
s= "\t\they buddy wait system is loading.........."
for m in s:
	sys.stdout.write(m)
	sys.stdout.flush()
	time.sleep(0.1)
print("\n\n\n\n")

time.sleep(2)
os.system("clear")

print("\n\n\n")
s= "\t\t\033[1;32mconection successfull!! well done."
for m in s:
	sys.stdout.write(m)
	sys.stdout.flush()
	time.sleep(0.1)
	
time.sleep(1.6)
os.system("clear")
	
print("\n\n\n\n")
pas = ["SH9"]
password = input("\033[1;34mEnter password: ")
if password in pas:
    s = "\n\t\t\033[1;32mwelcome to my tool"
    for m in s:
        sys.stdout.write(m)
        sys.stdout.flush()
        time.sleep(0.1)
else:
    s = "\n\033[91mwrong password!! you are not allowed my tool."
    for m in s:
        sys.stdout.write(m)
        sys.stdout.flush()
        time.sleep(0.1)
    time.sleep(1.5)
    sys.exit()

time.sleep(2)
os.system("clear")
 
print("""\033[1;33m


  _    _ _    _ _   _ _______ ______ _____  
 | |  | | |  | | \\ | |__   __|  ____|  __ \\ 
 | |__| | |  | |  \\| |  | |  | |__  | |__) |
 |  __  | |  | | . ` |  | |  |  __| |  _  / 
 | |  | | |__| | |\\  |  | |  | |____| | \\ \\ 
 |_|  |_|\\____/|_| \\_|  |_|  |______|_|  \\_\\
                                            
                                 
\033[1;32m==========================================
\033[1;36mOWNER :   SABBIR 
Github:   https://github.com/SabbirSH9 
Facebook :https://www.facebook.com/sabbir.hossein.66278 
use only legal purposes 
\033[1;32m==========================================
""")
print("\033[1;33m      TERMUX SETUP BASIC TOOL'S      \033[0m")
print("\033[1;36m====================================\033[0m")

print("1. Install all basic packages")
print("2. Exit")

choice = input("Select option 1/2: ")

if choice == "1":
    os.system("termux-setup-storage")
    os.system("pkg update -y")
    os.system("pkg upgrade -y")
    os.system("pkg install git -y")
    os.system("pkg install python -y")
    os.system("pkg install python2 -y")
    os.system("pkg install nodejs -y")
    os.system("pkg install wget -y")
    os.system("pkg install curl -y")
    os.system("pkg install nano -y")
    os.system("pkg install bash -y")
    os.system("pip install requests -y")
    
    print("\033[1;32mAll packages installed successfully!\033[0m")
elif choice == "2":
    print("Program exited")
else:
    print("\033[1;31mInvalid choice! Please enter 1 or 2\033[0m")
