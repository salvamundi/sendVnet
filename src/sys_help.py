import platform
import os
#at first sys_info.py, then changed to sys_help.py
#returns os_name, os_ver
def get_system_info():
    os_name = platform.system() #Windows
    os_ver = platform.release() #10
    return os_name, os_ver

#clears screen
#works for "cls" and "clear" commands
#I'm used to be comfortable with clear command more than with cls ;)
def clear():
    os_name, os_ver = get_system_info()

    if os_name == "Windows":
        os.system("cls")
    if os_name == "Linux":
        os.system("clear")
