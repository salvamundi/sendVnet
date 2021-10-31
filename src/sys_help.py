import platform
import os

#returns os_name, os_ver
def get_system_info():
    os_name = platform.system() #Windows
    os_ver = platform.release() #10
    return os_name, os_ver

#clears screen
#works for "cls" and "clear" commands
#I'm used to be comfortable with clear command more than with cls ;)
def clear():
    s_i = get_system_info()

    if s_i.os_name == "Windows":
        os.system("cls")
    if s_i.os_name == "Linux":
        os.system("clear")